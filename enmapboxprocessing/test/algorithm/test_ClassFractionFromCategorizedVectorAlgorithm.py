import numpy as np
from qgis._core import QgsRasterLayer, QgsVectorLayer, QgsPalettedRasterRenderer

from enmapbox.exampledata import enmap, landcover_polygons
from enmapboxprocessing.algorithm.classfractionfromcategorizedvectoralgorithm import \
    ClassFractionFromCategorizedVectorAlgorithm
from enmapboxprocessing.algorithm.rasterizecategorizedvectoralgorithm import RasterizeCategorizedVectorAlgorithm
from enmapboxprocessing.rasterreader import RasterReader
from enmapboxprocessing.test.algorithm.testcase import TestCase
from enmapboxprocessing.utils import Utils
from enmapboxtestdata import (landcover_polygons_3classes_epsg4326, landcover_polygons_3classes_id,
                              landcover_points_multipart_epsg3035)


class TestClassFractionFromCategorizedVectorAlgorithm(TestCase):

    def test_numberClassAttribute(self):
        alg = ClassFractionFromCategorizedVectorAlgorithm()
        alg.initAlgorithm()
        parameters = {
            alg.P_CATEGORIZED_VECTOR: landcover_polygons_3classes_id,
            alg.P_GRID: enmap,
            alg.P_OUTPUT_FRACTION_RASTER: self.filename('fractions_polygons.tif')
        }
        self.runalg(alg, parameters)
        reader = RasterReader(parameters[alg.P_OUTPUT_FRACTION_RASTER])
        self.assertListEqual(['roof', 'tree', 'water'], [reader.bandName(bandNo) for bandNo in reader.bandNumbers()])
        self.assertAlmostEqual(248.142, np.mean(reader.array()), 3)

    def test_stringClassAttribute(self):
        alg = ClassFractionFromCategorizedVectorAlgorithm()
        alg.initAlgorithm()
        parameters = {
            alg.P_CATEGORIZED_VECTOR: QgsVectorLayer(landcover_polygons),
            alg.P_GRID: QgsRasterLayer(enmap),
            alg.P_OUTPUT_FRACTION_RASTER: self.filename('fractions_polygons.tif')
        }
        self.runalg(alg, parameters)
        reader = RasterReader(parameters[alg.P_OUTPUT_FRACTION_RASTER])
        self.assertListEqual(
            ['roof', 'pavement', 'low vegetation', 'tree', 'soil', 'water'],
            [reader.bandName(bandNo) for bandNo in reader.bandNumbers()]
        )
        self.assertAlmostEqual(247.589, np.mean(reader.array()), 3)

    def test_band(self):
        alg = ClassFractionFromCategorizedVectorAlgorithm()
        alg.initAlgorithm()
        parameters = {
            alg.P_CATEGORIZED_VECTOR: QgsVectorLayer(landcover_polygons),
            alg.P_GRID: QgsRasterLayer(enmap),
            alg.P_OUTPUT_FRACTION_RASTER: self.filename('fractions_polygons.tif')
        }
        self.runalg(alg, parameters)
        reader = RasterReader(parameters[alg.P_OUTPUT_FRACTION_RASTER])
        self.assertListEqual(
            ['roof', 'pavement', 'low vegetation', 'tree', 'soil', 'water'],
            [reader.bandName(bandNo) for bandNo in reader.bandNumbers()]
        )
        self.assertAlmostEqual(247.589, np.mean(reader.array()), 3)

