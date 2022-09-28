import pickle
import typing
import uuid
from os.path import basename
from typing import List

from enmapbox import debugLog
from qgis.PyQt.QtCore import QMimeData, QUrl, QByteArray
from qgis.PyQt.QtXml import QDomNamedNodeMap, QDomDocument
from qgis.core import QgsLayerTreeModel
from qgis.core import QgsLayerItem
from qgis.core import QgsMapLayer, QgsRasterLayer, QgsProject, QgsReadWriteContext, \
    QgsMimeDataUtils, QgsLayerTree
from .datasources.datasources import DataSource
from ..qgispluginsupport.qps.layerproperties import defaultRasterRenderer
from ..qgispluginsupport.qps.speclib.core import is_spectral_library
from ..qgispluginsupport.qps.speclib.core.spectrallibrary import SpectralLibrary

MDF_RASTERBANDS = 'application/enmapbox.rasterbanddata'

MDF_DATASOURCETREEMODELDATA = 'application/enmapbox.datasourcetreemodeldata'
MDF_DATASOURCETREEMODELDATA_XML = 'data_source_tree_model_data'

MDF_ENMAPBOX_SOURCE_WIDGET = 'application/enmapbox.source_widget'
MDF_ENMAPBOX_LAYERTREEMODELDATA = 'application/enmapbox.layertreemodeldata'
QGIS_LAYERTREEMODELDATA = 'application/qgis.layertreemodeldata'
MDF_QGIS_LAYERTREEMODELDATA_XML = 'layer_tree_model_data'

MDF_PYTHON_OBJECTS = 'application/enmapbox/objectreference'
MDF_SPECTRALLIBRARY = 'application/hub-spectrallibrary'

MDF_URILIST = 'text/uri-list'
MDF_TEXT_HTML = 'text/html'
MDF_TEXT_PLAIN = 'text/plain'

QGIS_STYLE = 'application/qgis.style'
QGIS_URILIST_MIMETYPE = 'application/x-vnd.qgis.qgis.uri'
QGIS_LAYERTREE_LAYERDEFINITION = 'application/qgis.layertree.layerdefinitions'


def attributesd2dict(attributes: QDomNamedNodeMap) -> str:
    d = {}
    assert isinstance(attributes, QDomNamedNodeMap)
    for i in range(attributes.count()):
        attribute = attributes.item(i)
        d[attribute.nodeName()] = attribute.nodeValue()
    return d


def setEnMAPBoxID(mimeData: QMimeData, obj: object = None):
    if isinstance(obj, object):
        mimeData.setData(MDF_ENMAPBOX_SOURCE_WIDGET, obj.__class__.__name__.encode())
    mimeData.setData('application/qgis.application.pid', '-9999'.encode())


def fromDataSourceList(dataSources, project: QgsProject = None):
    if not isinstance(dataSources, list):
        dataSources = [dataSources]

    from enmapbox.gui.datasources.datasources import DataSource

    # create a temporary layer tree and use its own mimeData() routine
    tmpLayers: List[QgsMapLayer] = []
    uris: List[QgsMimeDataUtils.Uri] = []
    for ds in dataSources:
        assert isinstance(ds, DataSource)
        dataItem = ds.dataItem()
        if isinstance(dataItem, QgsLayerItem):
            lyr = ds.asMapLayer(project=project)
            if isinstance(lyr, QgsMapLayer):
                tmpLayers.append(lyr)

        elif isinstance(ds, DataSource):
            uri = QgsMimeDataUtils.Uri()
            uri.name = dataItem.name()
            uri.filePath = dataItem.path()
            uri.uri = dataItem.path()
            uri.providerKey = dataItem.providerKey()
            uris.append(uri)

    mimeData: QMimeData = QMimeData()
    if len(tmpLayers) > 0:
        root = QgsLayerTree()
        m = QgsLayerTreeModel(root)
        for lyr in tmpLayers:
            root.addLayer(lyr)
        indices = [m.node2index(n) for n in root.findLayers()]
        mdLayers: QMimeData = m.mimeData(indices)

        for f in mdLayers.formats():
            mimeData.setData(f, mdLayers.data(f))

    if len(uris) > 0:
        mdUris: QMimeData = QgsMimeDataUtils.encodeUriList(uris)
        for f in mdUris.formats():
            mimeData.setData(f, mdUris.data(f))
    return mimeData


def toDataSourceList(mimeData) -> typing.List[DataSource]:
    assert isinstance(mimeData, QMimeData)

    uriList = QgsMimeDataUtils.decodeUriList(mimeData)
    dataSources = []
    from enmapbox.gui.datasources.manager import DataSourceFactory
    for uri in uriList:
        dataSources.extend(DataSourceFactory.create(uri))
    return dataSources


def fromLayerList(mapLayers: List[QgsMapLayer]):
    """
    Converts a list of QgsMapLayers into a QMimeData object
    :param mapLayers: [list-of-QgsMapLayers]
    :return: QMimeData
    """
    for lyr in mapLayers:
        assert isinstance(lyr, QgsMapLayer)

    tree = QgsLayerTree()
    mimeData = QMimeData()

    urls = []
    for lyr in mapLayers:
        tree.addLayer(lyr)
        urls.append(QUrl.fromLocalFile(lyr.source()))
    doc = QDomDocument()
    context = QgsReadWriteContext()
    node = doc.createElement(MDF_QGIS_LAYERTREEMODELDATA_XML)
    doc.appendChild(node)
    for c in tree.children():
        c.writeXml(node, context)

    mimeData.setData(QGIS_LAYERTREEMODELDATA, doc.toByteArray())

    return mimeData


def containsMapLayers(mimeData: QMimeData) -> bool:
    """
    Checks if the mimeData contains any format suitable to describe QgsMapLayers
    :param mimeData:
    :return:
    """
    valid = [MDF_RASTERBANDS, MDF_DATASOURCETREEMODELDATA, QGIS_LAYERTREEMODELDATA, QGIS_URILIST_MIMETYPE,
             MDF_URILIST]

    for f in valid:
        if f in mimeData.formats():
            return True
    return False


def extractMapLayers(mimeData: QMimeData,
                     project: QgsProject = QgsProject.instance()) -> List[QgsMapLayer]:
    """
    Extracts QgsMapLayers from QMimeData
    :param mimeData:
    :param project:
    :return: A list if QgsMapLayers
    """
    assert isinstance(mimeData, QMimeData)

    from enmapbox.gui.datasources.datasources import DataSource
    from enmapbox.gui.datasources.datasources import SpatialDataSource
    from enmapbox.gui.datasources.manager import DataSourceFactory

    newMapLayers = []

    QGIS_LAYERTREE_FORMAT = None
    if MDF_ENMAPBOX_LAYERTREEMODELDATA in mimeData.formats():
        QGIS_LAYERTREE_FORMAT = MDF_ENMAPBOX_LAYERTREEMODELDATA
    elif QGIS_LAYERTREEMODELDATA in mimeData.formats():
        QGIS_LAYERTREE_FORMAT = QGIS_LAYERTREEMODELDATA

    def printDebugInfo(format):
        if len(newMapLayers) > 0:
            debugLog(f'Extracted {len(newMapLayers)} layers from {format}')

    if QGIS_LAYERTREE_FORMAT in mimeData.formats():
        doc = QDomDocument()
        doc.setContent(mimeData.data(QGIS_LAYERTREE_FORMAT))
        node = doc.firstChildElement(MDF_QGIS_LAYERTREEMODELDATA_XML)
        context = QgsReadWriteContext()
        # context.setPathResolver(QgsProject.instance().pathResolver())
        layerTree = QgsLayerTree.readXml(node, context)

        for layerId in layerTree.findLayerIds():
            lyr = project.mapLayer(layerId)
            if isinstance(lyr, QgsMapLayer):
                newMapLayers.append(lyr)

        printDebugInfo(QGIS_LAYERTREE_FORMAT)

    if len(newMapLayers) == 0 and MDF_RASTERBANDS in mimeData.formats():
        data = pickle.loads(mimeData.data(MDF_RASTERBANDS))

        for t in data:
            uri, baseName, providerKey, band = t
            lyr = QgsRasterLayer(uri, baseName=baseName, providerType=providerKey)
            lyr.setRenderer(defaultRasterRenderer(lyr, bandIndices=[band]))
            newMapLayers.append(lyr)

        printDebugInfo(MDF_RASTERBANDS)

    if len(newMapLayers) == 0 and MDF_DATASOURCETREEMODELDATA in mimeData.formats():
        # this drop comes from the datasource tree
        dsUUIDs = pickle.loads(mimeData.data(MDF_DATASOURCETREEMODELDATA))

        for uuid4 in dsUUIDs:
            assert isinstance(uuid4, uuid.UUID)
            dataSource = DataSource.fromUUID(uuid4)

            if isinstance(dataSource, SpatialDataSource):
                lyr = dataSource.asMapLayer()
                if isinstance(lyr, QgsMapLayer):
                    if isinstance(lyr, QgsRasterLayer):
                        lyr.setRenderer(defaultRasterRenderer(lyr))
                    newMapLayers.append(lyr)

        printDebugInfo(MDF_DATASOURCETREEMODELDATA)

    if len(newMapLayers) == 0 and QGIS_URILIST_MIMETYPE in mimeData.formats():
        for uri in QgsMimeDataUtils.decodeUriList(mimeData):
            uri: QgsMimeDataUtils.Uri
            error = f'Unable to extract {uri.data()} from mimeData'
            lyr = None
            success = False
            if uri.layerType == 'raster':
                lyr, success = uri.rasterLayer(error)
            elif uri.layerType == 'vector':
                lyr, success = uri.vectorLayer(error)

            if lyr is None:
                lyr = project.mapLayer(uri.layerId)

            if isinstance(lyr, QgsMapLayer) and lyr.isValid():
                # if isinstance(lyr, QgsRasterLayer):
                #    lyr.setRenderer(defaultRasterRenderer(lyr))
                newMapLayers.append(lyr)

        printDebugInfo(QGIS_URILIST_MIMETYPE)

    if len(newMapLayers) == 0 and MDF_URILIST in mimeData.formats():
        for url in mimeData.urls():

            if basename(url.url()) == 'MTD_MSIL2A.xml':  # resolves GitHub issue #42
                dataSources = [None]
            else:
                dataSources = DataSourceFactory.create(url)

            for dataSource in dataSources:
                if isinstance(dataSource, SpatialDataSource):
                    lyr = dataSource.asMapLayer()
                    if isinstance(lyr, QgsMapLayer):
                        if isinstance(lyr, QgsRasterLayer):
                            lyr.setRenderer(defaultRasterRenderer(lyr))
                        newMapLayers.append(lyr)
                else:
                    # check if URL is associated with an external product,
                    # if so, the product is created by running the appropriate processing algorithm
                    from enmapboxprocessing.algorithm.importproductsdraganddropsupport import tryToImportSensorProducts
                    filename = url.toLocalFile()
                    mapLayers = tryToImportSensorProducts(filename)
                    newMapLayers.extend(mapLayers)

        printDebugInfo(MDF_URILIST)

    if len(newMapLayers) == 0:
        debugLog('Could not extract map layers from mimedata')

    return newMapLayers


def extractSpectralLibraries(mimeData: QMimeData) -> list:
    """Reads spectral libraries that may be defined in mimeData"""
    results = []
    slib = SpectralLibrary.readFromMimeData(mimeData)
    if is_spectral_library(slib):
        results.append(slib)

    return results


def textToByteArray(text):
    """
    Converts input into a QByteArray
    :param text: bytes or str
    :return: QByteArray
    """

    if isinstance(text, QDomDocument):
        return textToByteArray(text.toString())
    else:
        data = QByteArray()
        data.append(text)
        return data


def textFromByteArray(data):
    """
    Decodes a QByteArray into a str
    :param data: QByteArray
    :return: str
    """
    assert isinstance(data, QByteArray)
    s = data.data().decode()
    return s
