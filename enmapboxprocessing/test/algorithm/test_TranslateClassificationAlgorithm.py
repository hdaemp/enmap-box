import numpy as np
from qgis._core import QgsRasterLayer, QgsProcessingContext

import processing
from enmapbox.exampledata import enmap
from enmapboxprocessing.algorithm.translatecategorizedrasteralgorithm import TranslateCategorizedRasterAlgorithm
from enmapboxprocessing.rasterreader import RasterReader
from enmapboxprocessing.test.algorithm.testcase import TestCase
from enmapboxtestdata import landcover_raster_30m_epsg3035


class TestTranslateClassificationAlgorithm(TestCase):

    def test_default(self):
        alg = TranslateCategorizedRasterAlgorithm()
        alg.initAlgorithm()
        parameters = {
            alg.P_CATEGORIZED_RASTER: QgsRasterLayer(landcover_raster_30m_epsg3035),
            alg.P_GRID: QgsRasterLayer(enmap),
            alg.P_OUTPUT_CATEGORIZED_RASTER: self.filename('landcover.tif')
        }
        result = self.runalg(alg, parameters)
        self.assertEqual(5126, np.sum(RasterReader(result[alg.P_OUTPUT_CATEGORIZED_RASTER]).array()))
