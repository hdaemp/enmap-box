from unittest import TestCase

from _classic.hubdsm.algorithm.importprismal2c import isPrismaL2CProduct, importPrismaL2C


class TestImportEnmapL2A(TestCase):

    def test_isEnmapL2AProduct(self):
        filenameHe5 = r'C:\Users\janzandr\Downloads\PRS_L2C_STD_20200209102459_20200209102503_0001\PRS_L2C_STD_20200209102459_20200209102503_0001.he5'
        self.assertTrue(isPrismaL2CProduct(filenameHe5=filenameHe5))
        self.assertFalse(isPrismaL2CProduct(filenameHe5=''))

    def test(self):
        dsSpectral = importPrismaL2C(
            filenameHe5=r'C:\Users\janzandr\Downloads\PRS_L2C_STD_20200209102459_20200209102503_0001\PRS_L2C_STD_20200209102459_20200209102503_0001.he5'
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
            [379, 426, 291, 341, 327, 321, 352, 354, 360, 372, 359, 385, 405, 390, 363, 424, 397, 411, 465, 497, 448,
             531, 542, 592, 591, 600, 626, 658, 627, 653, 651, 662, 682, 662, 669, 705, 714, 724, 703, 708, 708, 710,
             710, 707, 702, 695, 725, 773, 876, 1034, 1215, 1404, 1622, 1753, 1966, 2258, 2529, 2766, 2910, 3012, 3208,
             3239, 3272, 3253, 3210, 3232, 3156, 3195, 3240, 3363, 3485, 3530, 3455, 3493, 3503, 3514, 3380, 3303, 3297,
             3145, 3178, 3223, 3192, 3070, 2615, 2394, 2429, 2457, 2554, 2666, 2819, 3018, 3112, 3226, 3236, 3433, 3462,
             3614, 3658, 3732, 3836, 3899, 3979, 4031, 4027, 3925, 3763, 3374, 2673, 2297, 2474, 2763, 3150, 3273, 3281,
             3301, 3341, 3454, 3571, 3633, 3663, 3679, 3614, 3375, 3163, 2855, 2345, 1784, 2142, 14998, 11865, 1180,
             1462, 1639, 1751, 1851, 1934, 2018, 2077, 2146, 2207, 2238, 2269, 2317, 2326, 2388, 2404, 2371, 2463, 2440,
             2327, 2267, 2256, 2229, 2179, 2099, 1963, 1774, 306, 425, 633, 848, 855, 918, 1001, 1006, 1135, 1225, 1250,
             1274, 1291, 1292, 1311, 1374, 1396, 1391, 1434, 1436, 1472, 1483, 1495, 1510, 1507, 1594, 1559, 1559, 1577,
             1586, 1553, 1541, 1599, 1603, 1546, 1519, 1508, 1481, 1442, 1425, 1398, 1388, 1349, 1348, 1337, 1271, 1280,
             1258, 1250, 1215, 1174, 1106, 1092, 1075, 1097, 1000, 899, 889, 976, 864]

        )
        self.assertListEqual(
            profileScaled,
            [0.0379, 0.0426, 0.0291, 0.0341, 0.0327, 0.0321, 0.0352, 0.0354, 0.036, 0.0372, 0.0359, 0.0385, 0.0405,
             0.039, 0.0363, 0.0424, 0.0397, 0.0411, 0.0465, 0.0497, 0.0448, 0.0531, 0.0542, 0.0592, 0.0591, 0.06,
             0.0626, 0.0658, 0.0627, 0.0653, 0.0651, 0.0662, 0.0682, 0.0662, 0.0669, 0.0705, 0.0714, 0.0724, 0.0703,
             0.0708, 0.0708, 0.071, 0.071, 0.0707, 0.0702, 0.0695, 0.0725, 0.0773, 0.0876, 0.1034, 0.1215, 0.1404,
             0.1622, 0.1753, 0.1966, 0.2258, 0.2529, 0.2766, 0.291, 0.3012, 0.3208, 0.3239, 0.3272, 0.3253, 0.321,
             0.3232, 0.3156, 0.3195, 0.324, 0.3363, 0.3485, 0.353, 0.3455, 0.3493, 0.3503, 0.3514, 0.338, 0.3303,
             0.3297, 0.3145, 0.3178, 0.3223, 0.3192, 0.307, 0.2615, 0.2394, 0.2429, 0.2457, 0.2554, 0.2666, 0.2819,
             0.3018, 0.3112, 0.3226, 0.3236, 0.3433, 0.3462, 0.3614, 0.3658, 0.3732, 0.3836, 0.3899, 0.3979, 0.4031,
             0.4027, 0.3925, 0.3763, 0.3374, 0.2673, 0.2297, 0.2474, 0.2763, 0.315, 0.3273, 0.3281, 0.3301, 0.3341,
             0.3454, 0.3571, 0.3633, 0.3663, 0.3679, 0.3614, 0.3375, 0.3163, 0.2855, 0.2345, 0.1784, 0.2142, 1.4998,
             1.1865, 0.118, 0.1462, 0.1639, 0.1751, 0.1851, 0.1934, 0.2018, 0.2077, 0.2146, 0.2207, 0.2238, 0.2269,
             0.2317, 0.2326, 0.2388, 0.2404, 0.2371, 0.2463, 0.244, 0.2327, 0.2267, 0.2256, 0.2229, 0.2179, 0.2099,
             0.1963, 0.1774, 0.0306, 0.0425, 0.0633, 0.0848, 0.0855, 0.0918, 0.1001, 0.1006, 0.1135, 0.1225, 0.125,
             0.1274, 0.1291, 0.1292, 0.1311, 0.1374, 0.1396, 0.1391, 0.1434, 0.1436, 0.1472, 0.1483, 0.1495, 0.151,
             0.1507, 0.1594, 0.1559, 0.1559, 0.1577, 0.1586, 0.1553, 0.1541, 0.1599, 0.1603, 0.1546, 0.1519, 0.1508,
             0.1481, 0.1442, 0.1425, 0.1398, 0.1388, 0.1349, 0.1348, 0.1337, 0.1271, 0.128, 0.1258, 0.125, 0.1215,
             0.1174, 0.1106, 0.1092, 0.1075, 0.1097, 0.1, 0.0899, 0.0889, 0.0976, 0.0864]
        )
