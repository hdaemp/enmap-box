from typing import Dict

from qgis.PyQt.QtXml import QDomDocument, QDomElement
from qgis.core import QgsXmlUtils
from qgis.gui import QgsDockWidget


class EnMAPBoxProjectSettings(object):
    # (adopted from Data Plotly plugin)

    def writeToProject(self, document: QDomDocument):
        parent_element = document.createElement('EnMAP-Box')
        element = self.writeXml(document, parent_element)
        parent_element.appendChild(element)

        root_node = document.elementsByTagName("qgis").item(0)
        root_node.appendChild(parent_element)

    def readFromProject(self, document: QDomDocument):
        root_node = document.elementsByTagName("qgis").item(0)
        enmapBoxElement = root_node.toElement().firstChildElement('EnMAP-Box')
        element = enmapBoxElement.toElement()
        return self.readXml(element.firstChildElement(), document, enmapBoxElement)

    def writeXml(self, document: QDomDocument, enmapBoxElement: QDomElement):
        settings = self.settings(document, enmapBoxElement)
        element = QgsXmlUtils.writeVariant(settings, document)
        return element

    def readXml(self, element: QDomElement, document: QDomDocument, enmapBoxElement: QDomElement):
        settings = QgsXmlUtils.readVariant(element)
        self.setSettings(settings, document, enmapBoxElement)

    def settings(self, document: QDomDocument, enmapBoxElement: QDomElement) -> Dict:
        from qgis.utils import iface
        from enmapbox import EnMAPBox
        enmapBox = EnMAPBox.instance()

        settings = dict()

        # QGIS GUI
        qgisMainWindow = iface.mapCanvas().parent().parent().parent()
        for dockWidget in qgisMainWindow.findChildren(QgsDockWidget):
            if hasattr(dockWidget, 'projectSettings'):
                key = dockWidget.projectSettingsKey()
                values = dockWidget.projectSettings(document, enmapBoxElement)
                settings[f'EO4Q/{key}'] = values

        # EnMAP-Box GUI
        if enmapBox is not None:
            enmapBoxMainWindow = enmapBox.ui
            for dockWidget in enmapBoxMainWindow.findChildren(QgsDockWidget):
                if hasattr(dockWidget, 'projectSettings'):
                    key = dockWidget.projectSettingsKey()
                    values = dockWidget.projectSettings(document, enmapBoxElement)
                    settings[key] = values

            # EnMAP-Box Apps
            for app in enmapBox.applicationRegistry.applications():
                key = app.projectSettingsKey()
                values = app.projectSettings(document, enmapBoxElement)
                if len(values) > 0:
                    settings[key] = values

        return settings

    def setSettings(self, settings: Dict, document: QDomDocument, enmapBoxElement: QDomElement):
        from qgis.utils import iface
        from enmapbox import EnMAPBox
        enmapBox = EnMAPBox.instance()

        # QGIS GUI
        qgisMainWindow = iface.mapCanvas().parent().parent().parent()
        # - EO4Q apps (inside QGIS)
        for dockWidget in qgisMainWindow.findChildren(QgsDockWidget):
            if hasattr(dockWidget, 'projectSettings'):
                key = dockWidget.projectSettingsKey()
                values = settings[f'EO4Q/{key}']
                dockWidget.setProjectSettings(values, document, enmapBoxElement)

        # EnMAP-Box GUI
        if enmapBox is not None:
            enmapBoxMainWindow = enmapBox.ui
            for dockWidget in enmapBoxMainWindow.findChildren(QgsDockWidget):
                if hasattr(dockWidget, 'projectSettings'):
                    key = dockWidget.projectSettingsKey()
                    values = settings[key]
                    dockWidget.setProjectSettings(values, document, enmapBoxElement)

            # EnMAP-Box Apps
            for app in enmapBox.applicationRegistry.applications():
                key = app.projectSettingsKey()
                values = settings.get(key)
                if values is not None:
                    app.setProjectSettings(values, document, enmapBoxElement)
