"""
This is a template to create an EnMAP-Box test
"""
import pathlib
import unittest

from PyQt5.QtCore import QMimeData, QUrl, Qt, QEvent, QPointF
from PyQt5.QtGui import QDropEvent
from PyQt5.QtWidgets import QWidget, QTreeView

from enmapbox.gui.dataviews.dockmanager import MapDockTreeNode
from enmapbox.gui.dataviews.docks import DockArea, MapDock
from enmapbox.gui.enmapboxgui import EnMAPBox
from enmapbox.qgispluginsupport.qps.testing import QgisMockup
from qgis.PyQt.QtWidgets import QApplication
from qgis._gui import QgisInterface, QgsLayerTreeView
from qgis.core import QgsApplication, QgsRasterLayer, QgsVectorLayer
from enmapbox.testing import EnMAPBoxTestCase, TestObjects
from enmapbox import EnMAPBox

from enmapbox.exampledata import enmap, landcover_polygon, enmap_srf_library
from enmapbox.qgispluginsupport.qpstestdata import envi_sli
from enmapbox.testing import start_app


class EnMAPBoxTestCaseExample(EnMAPBoxTestCase):

    def test_drop_from_external(self):

        from qgis.utils import iface

        s = ""
        EMB = EnMAPBox(load_core_apps=False, load_other_apps=False)
        file_sets = [[enmap],
                     [landcover_polygon],
                     [enmap_srf_library],
                     [envi_sli],
                     [enmap, landcover_polygon, envi_sli]  # drop 2 files
                     ]

        for files in file_sets:
            mimeData: QMimeData = QMimeData()

            urls = [QUrl.fromLocalFile(s) for s in files]

            mimeData.setUrls(urls)

            tv: QWidget = EMB.dataSourceManagerTreeView()

            event = QDropEvent(QPointF(0, 0), Qt.CopyAction, mimeData, Qt.LeftButton, Qt.NoModifier, QEvent.Drop)
            tv.dropEvent(event)

            sources = EMB.dataSources()
            self.assertTrue(len(sources) == len(urls))

            EMB.removeSources(sources)
            self.assertEqual(len(EMB.dataSources()), 0)

        EMB.close()

    def dataSourceMimeData(self, tv: QTreeView):
        tv.selectAll()

        mimeData: QMimeData = tv.model().mimeData(tv.selectedIndexes())
        self.assertTrue('application/qgis.layertreemodeldata' in mimeData.formats())
        return mimeData

    def test_drag_drop_from_datasource(self):

        EMB = EnMAPBox(load_core_apps=False, load_other_apps=False)
        sources = [enmap, landcover_polygon]
        sources = [pathlib.Path(s) for s in sources]
        EMB.addSources(sources)
        nSources = len(EMB.dataSources())
        self.assertEqual(nSources, 2)

        for action in [Qt.CopyAction, Qt.MoveAction]:
            mimeData = self.dataSourceMimeData(EMB.dataSourceManagerTreeView())
            event = QDropEvent(QPointF(0, 0), action, mimeData, Qt.LeftButton, Qt.NoModifier, QEvent.Drop)
            # drop on empty area
            self.assertEqual(len(EMB.docks()), 0)
            dockArea: DockArea = EMB.ui.dockArea
            dockArea.dropEvent(event)

            # this should have opened a new map with 2 layers inside
            self.assertEqual(len(EMB.docks()), 1)
            mapDock = EMB.docks()[0]
            self.assertIsInstance(mapDock, MapDock)
            tree: MapDockTreeNode = mapDock.layerTree()

            self.assertIsInstance(tree, MapDockTreeNode)
            sources2 = set([pathlib.Path(lyr.source()) for lyr in tree.mapLayers()])
            for s in sources:
                self.assertTrue(s in sources2)

            EMB.removeDock(mapDock)

            self.assertEqual(len(EMB.dataSources()), nSources,
                             msg='Drag and Drop of data sources should not remove them')

        # drop to QGIS Layer Tree
        from qgis.utils import iface
        self.assertIsInstance(iface, QgisInterface)
        self.assertIsInstance(iface, QgisMockup)
        tv: QgsLayerTreeView = iface.layerTreeView()
        for action in [Qt.CopyAction, Qt.MoveAction]:
            mimeData = self.dataSourceMimeData(EMB.dataSourceManagerTreeView())
            event = QDropEvent(QPointF(0, 0), action, mimeData, Qt.LeftButton, Qt.NoModifier, QEvent.Drop)
            self.assertEqual(tv.layerTreeModel().rowCount(), 0)
            tv.dropEvent(event)
            self.assertEqual(tv.layerTreeModel().rowCount(), 2)
            self.assertEqual(len(EMB.dataSources()), nSources)
            tv.layerTreeModel().rootGroup().removeAllChildren()

        EMB.close()

    def test_drag_drop_from_qgis(self):

        from qgis.utils import iface
        self.assertIsInstance(iface, QgisInterface)
        self.assertIsInstance(iface, QgisMockup)

        EMB = EnMAPBox(load_core_apps=False, load_other_apps=False)

        tv: QgsLayerTreeView = iface.layerTreeView()
        self.assertEqual(tv.layerTreeModel().rowCount(), 0)
        iface.addRasterLayer(enmap)
        iface.addVectorLayer(landcover_polygon)
        self.assertEqual(tv.layerTreeModel().rowCount(), 2)

        self.assertEqual(len(EMB.dataSources()), 0)

        mimeData: QMimeData = self.dataSourceMimeData(tv)
        for action in [Qt.CopyAction, Qt.MoveAction]:
            EMB.close()

    def test_drop_from_other_layertree(self):
        pass

    def test_drop_from_same_layertree(self):
        pass


if __name__ == '__main__':
    unittest.main(buffer=False)
