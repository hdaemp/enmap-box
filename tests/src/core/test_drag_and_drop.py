"""
This is a template to create an EnMAP-Box test
"""
import unittest

from PyQt5.QtCore import QMimeData, QUrl, Qt, QEvent, QPointF
from PyQt5.QtGui import QDropEvent
from PyQt5.QtWidgets import QWidget

from enmapbox.gui.enmapboxgui import EnMAPBox
from qgis.PyQt.QtWidgets import QApplication
from qgis.core import QgsApplication, QgsRasterLayer, QgsVectorLayer
from enmapbox.testing import EnMAPBoxTestCase, TestObjects
from enmapbox import EnMAPBox


class EnMAPBoxTestCaseExample(EnMAPBoxTestCase):

    def test_drop_from_external(self):
        from enmapbox.exampledata import enmap, landcover_polygon, enmap_srf_library, library_sli

        EMB = EnMAPBox(load_core_apps=False, load_other_apps=False)
        file_sets = [[enmap],
                     [landcover_polygon],
                     [enmap_srf_library],
                     [library_sli],
                     [enmap, landcover_polygon, library_sli]
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

    def test_drop_from_qgis(self):
        pass

    def test_drop_from_other_layertree(self):
        pass

    def test_drop_from_same_layertree(self):
        pass


if __name__ == '__main__':
    unittest.main(buffer=False)
