from unittest import TestCase

from _classic.hubdsm.algorithm.importenmapl1c import importEnmapL1C, isEnmapL1CProduct


class TestImportEnmapL1C(TestCase):

    def test_isEnmapL1CProduct(self):
        filenameMetadataXml = r'C:\Users\janzandr\Downloads\L1C_Alps_1\ENMAP01-____L1C-DT000326721_20170626T102020Z_001_V000204_20200406T180016Z-METADATA.XML'
        self.assertTrue(isEnmapL1CProduct(filenameMetadataXml=filenameMetadataXml))
        self.assertFalse(isEnmapL1CProduct(filenameMetadataXml=''))

    def test(self):
        dsSpectral = importEnmapL1C(
            filenameMetadataXml=r'C:\Users\janzandr\Downloads\L1C_Alps_1\ENMAP01-____L1C-DT000326721_20170626T102020Z_001_V000204_20200406T180016Z-METADATA.XML'
        )

        self.assertEqual(
            dsSpectral.GetMetadataItem('wavelength', 'ENVI'),
            '{423.03, 428.8, 434.29, 439.58, 444.72, 449.75, 454.7, 459.59, 464.43, 469.25, 474.05, 478.84, 483.63, 488.42, 493.23, 498.05, 502.9, 507.77, 512.67, 517.6, 522.57, 527.58, 532.63, 537.72, 542.87, 548.06, 553.3, 558.6, 563.95, 569.36, 574.83, 580.36, 585.95, 591.6, 597.32, 603.1, 608.95, 614.86, 620.84, 626.9, 633.02, 639.21, 645.47, 651.8, 658.2, 664.67, 671.21, 677.83, 684.51, 691.26, 698.08, 704.97, 711.92, 718.95, 726.03, 733.19, 740.4, 747.68, 755.01, 762.41, 769.86, 777.37, 784.93, 792.54, 800.2, 807.91, 815.67, 823.46, 831.3, 839.18, 847.1, 855.05, 863.03, 871.05, 879.09, 887.16, 895.25, 903.36, 904.78, 911.49, 914.44, 919.64, 924.23, 927.8, 934.16, 935.98, 944.17, 944.23, 952.37, 954.42, 960.57, 964.74, 968.78, 975.17, 976.99, 985.21, 985.73, 996.4, 1007.2, 1018.1, 1029.1, 1040.2, 1051.3, 1062.6, 1074, 1085.4, 1096.9, 1108.5, 1120.1, 1131.8, 1143.5, 1155.3, 1167.1, 1179, 1190.9, 1202.8, 1214.8, 1226.7, 1238.7, 1250.7, 1262.7, 1274.7, 1286.7, 1298.7, 1310.7, 1322.7, 1334.7, 1346.6, 1358.5, 1370.4, 1382.3, 1487.8, 1499.4, 1510.9, 1522.3, 1533.7, 1545.1, 1556.4, 1567.7, 1578.9, 1590.1, 1601.2, 1612.3, 1623.3, 1634.3, 1645.3, 1656.2, 1667, 1677.8, 1688.5, 1699.2, 1709.9, 1720.5, 1731, 1741.5, 1752, 1762.4, 1772.7, 1941.5, 1951, 1960.5, 1969.9, 1979.3, 1988.7, 1998, 2007.2, 2016.4, 2025.6, 2034.8, 2043.9, 2052.9, 2061.9, 2070.9, 2079.9, 2088.8, 2097.6, 2106.4, 2115.2, 2124, 2132.7, 2141.3, 2150, 2158.6, 2167.1, 2175.7, 2184.2, 2192.6, 2201, 2209.4, 2217.8, 2226.1, 2234.4, 2242.6, 2250.8, 2259, 2267.2, 2275.3, 2283.4, 2291.4, 2299.4, 2307.4, 2315.4, 2323.3, 2331.2, 2339.1, 2346.9, 2354.7, 2362.5, 2370.2, 2377.9, 2385.6, 2393.3, 2400.9, 2408.5, 2416.1, 2423.6, 2431.1, 2438.6}'
        )

        profile = list(dsSpectral.ReadAsArray(188, 20, 1, 1).flatten())
        profileScaled = [
            round(v * dsSpectral.GetRasterBand(i + 1).GetScale() + dsSpectral.GetRasterBand(i + 1).GetOffset(), 4)
            for i, v in enumerate(profile)]
        self.assertListEqual(
            profile,
            [6221, 6179, 5803, 6224, 6208, 5988, 6002, 6004, 5877, 5862, 5675, 5729, 5733, 5649, 5445, 5649, 5514, 5524,
             5871, 6087, 5831, 6455, 6397, 6740, 6680, 6696, 6783, 6921, 6672, 6746, 6672, 6612, 6692, 6548, 6486, 6557,
             6526, 6502, 6288, 6243, 6166, 6057, 6023, 5941, 5775, 5688, 5747, 6025, 6730, 7941, 9224, 10432, 11851,
             13194, 14741, 16137, 17202, 18295, 18997, 20004, 20805, 20880, 21251, 21486, 21438, 21775, 22263, 22588,
             22562, 22846, 23386, 23611, 23198, 23555, 23734, 24133, 24411, 24469, 26238, 24385, 26450, 24625, 26297,
             24951, 26735, 25004, 24904, 26873, 25152, 26915, 25194, 26660, 24674, 26375, 25029, 25068, 26626, 26884,
             27135, 27647, 27801, 27655, 27876, 27934, 28100, 28191, 28264, 28558, 29361, 29271, 28678, 27848, 27566,
             27556, 27751, 27913, 28271, 28450, 28631, 28783, 28758, 28902, 28973, 29144, 29026, 28829, 28759, 26437,
             20731, 23195, 12741, 16556, 17800, 18965, 19492, 19893, 20355, 20948, 21497, 22116, 22195, 22494, 22614,
             22957, 22989, 23036, 23228, 23044, 23104, 23099, 22639, 22506, 22308, 21917, 21798, 21783, 21653, 20707,
             6129, 7538, 9219, 11428, 11793, 12207, 12394, 10527, 12141, 13841, 14350, 14391, 14288, 14398, 14553,
             15226, 15686, 15844, 16109, 16160, 16339, 16271, 16354, 16729, 16479, 17083, 17285, 17599, 17896, 17881,
             17567, 17512, 17727, 17747, 17483, 17489, 17728, 17842, 17643, 17802, 17686, 17724, 17269, 17498, 17453,
             16566, 16972, 17175, 17129, 16668, 16631, 16502, 16777, 15950, 16464, 15757, 14903, 14944, 16186, 15525]
        )
        self.assertListEqual(
            profileScaled,
            [0.0617, 0.0561, 0.0535, 0.0582, 0.0603, 0.0628, 0.0633, 0.0623, 0.0619, 0.0609, 0.0594, 0.0587, 0.0564,
             0.0526, 0.0527, 0.0532, 0.0496, 0.0501, 0.0503, 0.0481, 0.0481, 0.0508, 0.0506, 0.0509, 0.0496, 0.0499,
             0.0501, 0.0489, 0.0472, 0.0468, 0.0459, 0.0461, 0.0456, 0.0426, 0.0431, 0.0441, 0.0436, 0.0427, 0.0415,
             0.0403, 0.0401, 0.0401, 0.0388, 0.0376, 0.0369, 0.0374, 0.038, 0.0393, 0.0403, 0.0424, 0.0504, 0.0575,
             0.0643, 0.06, 0.0639, 0.0777, 0.0918, 0.1008, 0.0964, 0.066, 0.0971, 0.1085, 0.1071, 0.1025, 0.0996,
             0.0967, 0.0809, 0.0799, 0.0853, 0.0934, 0.0964, 0.0943, 0.0926, 0.0926, 0.0921, 0.0899, 0.0743, 0.0642,
             0.0636, 0.0576, 0.0585, 0.0609, 0.0557, 0.0465, 0.0253, 0.02, 0.0218, 0.022, 0.025, 0.0274, 0.0339, 0.0422,
             0.0497, 0.0555, 0.0563, 0.0665, 0.067, 0.0729, 0.0724, 0.0727, 0.0732, 0.0728, 0.072, 0.0699, 0.0675,
             0.0628, 0.0532, 0.0355, 0.013, 0.0094, 0.0127, 0.0196, 0.0333, 0.0371, 0.0377, 0.0379, 0.0395, 0.0424,
             0.0443, 0.043, 0.0375, 0.0376, 0.0394, 0.0345, 0.0276, 0.0202, 0.0117, 0.0038, 0.0003, 0.0002, 0.0001,
             0.0045, 0.0082, 0.0107, 0.0125, 0.0137, 0.0144, 0.015, 0.0145, 0.0144, 0.0152, 0.0146, 0.0145, 0.0155,
             0.0151, 0.0149, 0.0149, 0.0143, 0.0144, 0.014, 0.0129, 0.012, 0.0115, 0.0106, 0.0097, 0.0091, 0.0079,
             0.006, 0.0001, 0.0001, 0.0003, 0.0011, 0.0017, 0.002, 0.0013, 0.0005, 0.0009, 0.0021, 0.0031, 0.0029,
             0.0021, 0.0021, 0.0024, 0.0031, 0.0034, 0.0035, 0.0037, 0.0036, 0.0037, 0.0038, 0.0038, 0.0036, 0.0034,
             0.0035, 0.0035, 0.0034, 0.0034, 0.0032, 0.0033, 0.0033, 0.0034, 0.0033, 0.0031, 0.003, 0.0028, 0.0027,
             0.0026, 0.0025, 0.0023, 0.0022, 0.0023, 0.0021, 0.002, 0.002, 0.0018, 0.0016, 0.0015, 0.0016, 0.0013,
             0.0012, 0.0011, 0.0012, 0.0012, 0.0009, 0.0006, 0.0008, 0.0009, 0.0007]
        )
