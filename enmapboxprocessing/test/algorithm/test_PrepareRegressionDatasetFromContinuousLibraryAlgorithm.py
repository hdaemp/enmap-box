from enmapbox.exampledata import library_gpkg
from enmapboxprocessing.algorithm.prepareregressiondatasetfromcontinuouslibraryalgorithm import \
    PrepareRegressionDatasetFromContinuousLibraryAlgorithm
from enmapboxprocessing.test.algorithm.testcase import TestCase
from enmapboxprocessing.typing import RegressorDump
from enmapboxprocessing.utils import Utils


class TestPrepareClassificationDatasetFromCategorizedLibrary(TestCase):

    def test(self):
        alg = PrepareRegressionDatasetFromContinuousLibraryAlgorithm()
        parameters = {
            alg.P_CONTINUOUS_LIBRARY: library_gpkg,  # todo use better dataset (wait for #1036)
            alg.P_TARGET_FIELDS: ['fid'],
            alg.P_OUTPUT_DATASET: self.filename('sample.pkl')
        }
        self.runalg(alg, parameters)
        dump = RegressorDump.fromDict(Utils.pickleLoad(parameters[alg.P_OUTPUT_DATASET]))
        self.assertEqual((75, 177), dump.X.shape)
        self.assertEqual((75, 1), dump.y.shape)
        self.assertEqual(177, len(dump.features))

        # todo implement more tests, wait for issue #1036


"""    def test_selectBinaryField(self):
        alg = PrepareClassificationDatasetFromCategorizedLibraryAlgorithm()
        parameters = {
            alg.P_CATEGORIZED_LIBRARY: library_gpkg,
            alg.P_FIELD: 'profiles',
            alg.P_OUTPUT_DATASET: self.filename('sample.pkl')
        }
        self.runalg(alg, parameters)
        dump = ClassifierDump(**Utils.pickleLoad(parameters[alg.P_OUTPUT_DATASET]))
        self.assertEqual((75, 177), dump.X.shape)
        self.assertEqual((75, 1), dump.y.shape)
        self.assertEqual(177, len(dump.features))

    def test_wrongCategoryField(self):
        alg = PrepareClassificationDatasetFromCategorizedLibraryAlgorithm()
        parameters = {
            alg.P_CATEGORIZED_LIBRARY: library_gpkg,
            # alg.P_FIELD: 'profiles',
            alg.P_CATEGORY_FIELD: 'profiles',
            alg.P_OUTPUT_DATASET: self.filename('sample.pkl')
        }
        try:
            self.runalg(alg, parameters)
        except QgsProcessingException as error:
            self.assertEqual('Unable to derive categories from field: profiles', str(error))

    def test_wrongProfileField(self):
        alg = PrepareClassificationDatasetFromCategorizedLibraryAlgorithm()
        parameters = {
            alg.P_CATEGORIZED_LIBRARY: library_gpkg,
            alg.P_FIELD: 'level_1',
            alg.P_OUTPUT_DATASET: self.filename('sample.pkl')
        }
        try:
            self.runalg(alg, parameters)
        except QgsProcessingException as error:
            self.assertEqual('Profiles field must be Binary: level_1', str(error))
"""
