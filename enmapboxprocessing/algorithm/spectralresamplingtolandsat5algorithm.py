from enmapboxprocessing.algorithm.spectralresamplingbyresponsefunctionconvolutionalgorithmbase import \
    SpectralResamplingByResponseFunctionConvolutionAlgorithmBase
from typeguard import typechecked


@typechecked
class SpectralResamplingToLandsat5Algorithm(SpectralResamplingByResponseFunctionConvolutionAlgorithmBase):
    A_CODE = True

    def displayName(self) -> str:
        return 'Spectral resampling (to Landsat 4/5 TM)'

    def shortDescription(self) -> str:
        link = self.htmlLink(
            'https://www.usgs.gov/core-science-systems/nli/landsat/landsat-satellite-missions',
            'Landsat')
        return super().shortDescription() + f'\nFor more information see the {link} missions website.'

    def code(self):
        from collections import OrderedDict

        responses = OrderedDict()
        responses['Blue'] = [(421, 0.001), (422, 0.001), (423, 0.001), (424, 0.001), (425, 0.001), (426, 0.002),
                             (427, 0.002), (428, 0.002), (429, 0.003), (430, 0.003), (431, 0.005), (432, 0.007),
                             (433, 0.01), (434, 0.013), (435, 0.017), (436, 0.02), (437, 0.025), (438, 0.031),
                             (439, 0.037), (440, 0.042), (441, 0.048), (442, 0.053), (443, 0.059), (444, 0.064),
                             (445, 0.07), (446, 0.083), (447, 0.121), (448, 0.172), (449, 0.273), (450, 0.372),
                             (451, 0.442), (452, 0.514), (453, 0.579), (454, 0.628), (455, 0.711), (456, 0.732),
                             (457, 0.742), (458, 0.75), (459, 0.755), (460, 0.756), (461, 0.766), (462, 0.776),
                             (463, 0.786), (464, 0.797), (465, 0.807), (466, 0.812), (467, 0.817), (468, 0.822),
                             (469, 0.827), (470, 0.829), (471, 0.831), (472, 0.833), (473, 0.835), (474, 0.838),
                             (475, 0.846), (476, 0.853), (477, 0.861), (478, 0.868), (479, 0.876), (480, 0.883),
                             (481, 0.886), (482, 0.888), (483, 0.891), (484, 0.893), (485, 0.896), (486, 0.898),
                             (487, 0.901), (488, 0.903), (489, 0.905), (490, 0.908), (491, 0.918), (492, 0.928),
                             (493, 0.938), (494, 0.948), (495, 0.952), (496, 0.956), (497, 0.961), (498, 0.965),
                             (499, 0.97), (500, 0.979), (501, 0.987), (502, 0.994), (503, 1.0), (504, 0.999),
                             (505, 0.99), (506, 0.963), (507, 0.936), (508, 0.909), (509, 0.881), (510, 0.852),
                             (511, 0.824), (512, 0.81), (513, 0.796), (514, 0.779), (515, 0.756), (516, 0.707),
                             (517, 0.596), (518, 0.497), (519, 0.413), (520, 0.329), (521, 0.245), (522, 0.137),
                             (523, 0.105), (524, 0.094), (525, 0.083), (526, 0.072), (527, 0.061), (528, 0.055),
                             (529, 0.052), (530, 0.049), (531, 0.045), (532, 0.041), (533, 0.038), (534, 0.034),
                             (535, 0.031), (536, 0.027), (537, 0.024), (538, 0.022), (539, 0.019), (540, 0.017),
                             (541, 0.015), (542, 0.013), (543, 0.011), (544, 0.01), (545, 0.009), (546, 0.007),
                             (547, 0.006), (548, 0.006), (549, 0.006), (550, 0.005), (551, 0.005), (552, 0.005),
                             (553, 0.005), (554, 0.005), (555, 0.004), (556, 0.004), (557, 0.004), (558, 0.004),
                             (559, 0.004), (560, 0.003), (561, 0.003), (562, 0.003), (563, 0.003), (564, 0.002),
                             (565, 0.002), (566, 0.002), (567, 0.002), (568, 0.002), (569, 0.001), (570, 0.001)]
        responses['Green'] = [(502, 0.002), (503, 0.003), (504, 0.007), (505, 0.009), (506, 0.011), (507, 0.014),
                              (508, 0.016), (509, 0.019), (510, 0.022), (511, 0.024), (512, 0.027), (513, 0.03),
                              (514, 0.032), (515, 0.035), (516, 0.05), (517, 0.066), (518, 0.091), (519, 0.12),
                              (520, 0.152), (521, 0.191), (522, 0.231), (523, 0.271), (524, 0.312), (525, 0.353),
                              (526, 0.392), (527, 0.43), (528, 0.468), (529, 0.507), (530, 0.537), (531, 0.561),
                              (532, 0.577), (533, 0.591), (534, 0.605), (535, 0.619), (536, 0.633), (537, 0.647),
                              (538, 0.661), (539, 0.675), (540, 0.69), (541, 0.7), (542, 0.711), (543, 0.721),
                              (544, 0.732), (545, 0.743), (546, 0.753), (547, 0.764), (548, 0.775), (549, 0.786),
                              (550, 0.797), (551, 0.803), (552, 0.809), (553, 0.815), (554, 0.821), (555, 0.826),
                              (556, 0.832), (557, 0.837), (558, 0.843), (559, 0.848), (560, 0.854), (561, 0.859),
                              (562, 0.865), (563, 0.871), (564, 0.873), (565, 0.874), (566, 0.875), (567, 0.877),
                              (568, 0.878), (569, 0.879), (570, 0.88), (571, 0.881), (572, 0.882), (573, 0.883),
                              (574, 0.884), (575, 0.885), (576, 0.886), (577, 0.887), (578, 0.891), (579, 0.896),
                              (580, 0.9), (581, 0.905), (582, 0.909), (583, 0.914), (584, 0.932), (585, 0.944),
                              (586, 0.954), (587, 0.963), (588, 0.971), (589, 0.977), (590, 0.982), (591, 0.988),
                              (592, 0.994), (593, 0.999), (594, 1.0), (595, 0.999), (596, 0.998), (597, 0.995),
                              (598, 0.98), (599, 0.964), (600, 0.949), (601, 0.927), (602, 0.894), (603, 0.862),
                              (604, 0.829), (605, 0.796), (606, 0.747), (607, 0.672), (608, 0.597), (609, 0.521),
                              (610, 0.467), (611, 0.413), (612, 0.359), (613, 0.304), (614, 0.249), (615, 0.206),
                              (616, 0.181), (617, 0.156), (618, 0.131), (619, 0.108), (620, 0.097), (621, 0.087),
                              (622, 0.076), (623, 0.066), (624, 0.055), (625, 0.052), (626, 0.049), (627, 0.045),
                              (628, 0.042), (629, 0.039), (630, 0.036), (631, 0.032), (632, 0.029), (633, 0.026),
                              (634, 0.023), (635, 0.021), (636, 0.019), (637, 0.017), (638, 0.015), (639, 0.013),
                              (640, 0.011), (641, 0.01), (642, 0.009), (643, 0.008), (644, 0.006), (645, 0.005),
                              (646, 0.003), (647, 0.002), (648, 0.001)]
        responses['Red'] = [(563, 0.001), (564, 0.001), (565, 0.001), (566, 0.001), (567, 0.001), (568, 0.001),
                            (569, 0.002), (570, 0.002), (571, 0.002), (572, 0.002), (573, 0.002), (574, 0.002),
                            (575, 0.002), (576, 0.002), (577, 0.002), (578, 0.002), (579, 0.002), (580, 0.002),
                            (581, 0.002), (582, 0.002), (583, 0.002), (584, 0.002), (585, 0.002), (586, 0.002),
                            (587, 0.002), (588, 0.002), (589, 0.002), (590, 0.003), (591, 0.003), (592, 0.003),
                            (593, 0.004), (594, 0.004), (595, 0.004), (596, 0.005), (597, 0.006), (598, 0.007),
                            (599, 0.008), (600, 0.009), (601, 0.011), (602, 0.014), (603, 0.016), (604, 0.019),
                            (605, 0.023), (606, 0.027), (607, 0.03), (608, 0.034), (609, 0.038), (610, 0.041),
                            (611, 0.045), (612, 0.062), (613, 0.081), (614, 0.101), (615, 0.12), (616, 0.14),
                            (617, 0.16), (618, 0.18), (619, 0.24), (620, 0.327), (621, 0.414), (622, 0.449),
                            (623, 0.471), (624, 0.492), (625, 0.514), (626, 0.535), (627, 0.557), (628, 0.579),
                            (629, 0.601), (630, 0.623), (631, 0.65), (632, 0.687), (633, 0.737), (634, 0.787),
                            (635, 0.803), (636, 0.818), (637, 0.835), (638, 0.849), (639, 0.86), (640, 0.871),
                            (641, 0.883), (642, 0.894), (643, 0.906), (644, 0.912), (645, 0.917), (646, 0.922),
                            (647, 0.928), (648, 0.933), (649, 0.939), (650, 0.944), (651, 0.943), (652, 0.942),
                            (653, 0.942), (654, 0.941), (655, 0.94), (656, 0.939), (657, 0.938), (658, 0.937),
                            (659, 0.936), (660, 0.935), (661, 0.937), (662, 0.939), (663, 0.943), (664, 0.948),
                            (665, 0.954), (666, 0.959), (667, 0.965), (668, 0.97), (669, 0.975), (670, 0.979),
                            (671, 0.983), (672, 0.987), (673, 0.99), (674, 0.997), (675, 0.996), (676, 0.998),
                            (677, 1.0), (678, 0.998), (679, 0.996), (680, 0.994), (681, 0.973), (682, 0.973),
                            (683, 0.974), (684, 0.964), (685, 0.945), (686, 0.927), (687, 0.908), (688, 0.871),
                            (689, 0.822), (690, 0.773), (691, 0.687), (692, 0.594), (693, 0.505), (694, 0.433),
                            (695, 0.361), (696, 0.289), (697, 0.223), (698, 0.188), (699, 0.152), (700, 0.116),
                            (701, 0.106), (702, 0.095), (703, 0.084), (704, 0.074), (705, 0.063), (706, 0.057),
                            (707, 0.054), (708, 0.051), (709, 0.048), (710, 0.045), (711, 0.042), (712, 0.039),
                            (713, 0.036), (714, 0.033), (715, 0.03), (716, 0.027), (717, 0.024), (718, 0.022),
                            (719, 0.021), (720, 0.02), (721, 0.018), (722, 0.017), (723, 0.015), (724, 0.014),
                            (725, 0.012), (726, 0.011), (727, 0.01), (728, 0.009), (729, 0.007), (730, 0.006),
                            (731, 0.006), (732, 0.005), (733, 0.005), (734, 0.005), (735, 0.005), (736, 0.004),
                            (737, 0.004), (738, 0.004), (739, 0.003), (740, 0.003), (741, 0.003), (742, 0.002),
                            (743, 0.002), (744, 0.002), (745, 0.002), (746, 0.001)]
        responses['NIR'] = [(727, 0.001), (728, 0.001), (729, 0.002), (730, 0.002), (731, 0.003), (732, 0.003),
                            (733, 0.004), (734, 0.004), (735, 0.005), (736, 0.005), (737, 0.006), (738, 0.006),
                            (739, 0.007), (740, 0.007), (741, 0.008), (742, 0.008), (743, 0.009), (744, 0.009),
                            (745, 0.01), (746, 0.012), (747, 0.014), (748, 0.016), (749, 0.018), (750, 0.02),
                            (751, 0.022), (752, 0.025), (753, 0.028), (754, 0.031), (755, 0.034), (756, 0.042),
                            (757, 0.05), (758, 0.058), (759, 0.066), (760, 0.074), (761, 0.083), (762, 0.09),
                            (763, 0.099), (764, 0.121), (765, 0.143), (766, 0.165), (767, 0.187), (768, 0.216),
                            (769, 0.251), (770, 0.286), (771, 0.322), (772, 0.357), (773, 0.393), (774, 0.428),
                            (775, 0.464), (776, 0.5), (777, 0.544), (778, 0.587), (779, 0.63), (780, 0.673),
                            (781, 0.717), (782, 0.76), (783, 0.795), (784, 0.822), (785, 0.849), (786, 0.876),
                            (787, 0.902), (788, 0.917), (789, 0.932), (790, 0.946), (791, 0.956), (792, 0.963),
                            (793, 0.97), (794, 0.976), (795, 0.983), (796, 0.986), (797, 0.99), (798, 0.993),
                            (799, 0.997), (800, 1.0), (801, 0.997), (802, 0.994), (803, 0.992), (804, 0.989),
                            (805, 0.986), (806, 0.983), (807, 0.98), (808, 0.977), (809, 0.974), (810, 0.971),
                            (811, 0.968), (812, 0.965), (813, 0.962), (814, 0.959), (815, 0.956), (816, 0.953),
                            (817, 0.95), (818, 0.947), (819, 0.945), (820, 0.942), (821, 0.939), (822, 0.936),
                            (823, 0.933), (824, 0.93), (825, 0.93), (826, 0.932), (827, 0.934), (828, 0.936),
                            (829, 0.938), (830, 0.94), (831, 0.942), (832, 0.944), (833, 0.946), (834, 0.948),
                            (835, 0.95), (836, 0.952), (837, 0.954), (838, 0.956), (839, 0.958), (840, 0.96),
                            (841, 0.962), (842, 0.964), (843, 0.966), (844, 0.968), (845, 0.97), (846, 0.972),
                            (847, 0.974), (848, 0.976), (849, 0.978), (850, 0.98), (851, 0.978), (852, 0.977),
                            (853, 0.975), (854, 0.974), (855, 0.973), (856, 0.971), (857, 0.97), (858, 0.967),
                            (859, 0.965), (860, 0.963), (861, 0.96), (862, 0.959), (863, 0.959), (864, 0.959),
                            (865, 0.96), (866, 0.961), (867, 0.962), (868, 0.963), (869, 0.964), (870, 0.965),
                            (871, 0.967), (872, 0.968), (873, 0.965), (874, 0.963), (875, 0.96), (876, 0.955),
                            (877, 0.95), (878, 0.945), (879, 0.94), (880, 0.935), (881, 0.929), (882, 0.922),
                            (883, 0.915), (884, 0.908), (885, 0.901), (886, 0.894), (887, 0.887), (888, 0.88),
                            (889, 0.873), (890, 0.866), (891, 0.865), (892, 0.864), (893, 0.858), (894, 0.846),
                            (895, 0.834), (896, 0.823), (897, 0.811), (898, 0.8), (899, 0.789), (900, 0.779),
                            (901, 0.733), (902, 0.688), (903, 0.643), (904, 0.578), (905, 0.509), (906, 0.44),
                            (907, 0.371), (908, 0.321), (909, 0.275), (910, 0.23), (911, 0.185), (912, 0.156),
                            (913, 0.13), (914, 0.105), (915, 0.084), (916, 0.074), (917, 0.064), (918, 0.054),
                            (919, 0.044), (920, 0.034), (921, 0.031), (922, 0.027), (923, 0.024), (924, 0.02),
                            (925, 0.017), (926, 0.015), (927, 0.013), (928, 0.012), (929, 0.01), (930, 0.008),
                            (931, 0.008), (932, 0.007), (933, 0.007), (934, 0.006), (935, 0.006), (936, 0.005),
                            (937, 0.005), (938, 0.005), (939, 0.004), (940, 0.004), (941, 0.003), (942, 0.003),
                            (943, 0.002), (944, 0.002), (945, 0.002), (946, 0.001)]
        responses['SWIR-1'] = [(1512, 0.001), (1513, 0.001), (1514, 0.001), (1515, 0.001), (1516, 0.001), (1517, 0.001),
                               (1518, 0.002), (1519, 0.002), (1520, 0.002), (1521, 0.002), (1522, 0.003), (1523, 0.004),
                               (1524, 0.004), (1525, 0.005), (1526, 0.006), (1527, 0.007), (1528, 0.007), (1529, 0.008),
                               (1530, 0.009), (1531, 0.01), (1532, 0.012), (1533, 0.013), (1534, 0.015), (1535, 0.016),
                               (1536, 0.018), (1537, 0.019), (1538, 0.021), (1539, 0.022), (1540, 0.024), (1541, 0.028),
                               (1542, 0.033), (1543, 0.038), (1544, 0.043), (1545, 0.048), (1546, 0.057), (1547, 0.067),
                               (1548, 0.077), (1549, 0.087), (1550, 0.098), (1551, 0.114), (1552, 0.132), (1553, 0.151),
                               (1554, 0.17), (1555, 0.189), (1556, 0.208), (1557, 0.228), (1558, 0.247), (1559, 0.267),
                               (1560, 0.287), (1561, 0.312), (1562, 0.34), (1563, 0.368), (1564, 0.396), (1565, 0.425),
                               (1566, 0.454), (1567, 0.483), (1568, 0.512), (1569, 0.541), (1570, 0.571), (1571, 0.598),
                               (1572, 0.625), (1573, 0.653), (1574, 0.68), (1575, 0.708), (1576, 0.732), (1577, 0.755),
                               (1578, 0.777), (1579, 0.8), (1580, 0.824), (1581, 0.842), (1582, 0.858), (1583, 0.874),
                               (1584, 0.89), (1585, 0.907), (1586, 0.916), (1587, 0.924), (1588, 0.93), (1589, 0.934),
                               (1590, 0.939), (1591, 0.943), (1592, 0.947), (1593, 0.946), (1594, 0.943), (1595, 0.94),
                               (1596, 0.937), (1597, 0.934), (1598, 0.933), (1599, 0.933), (1600, 0.933), (1601, 0.931),
                               (1602, 0.929), (1603, 0.928), (1604, 0.928), (1605, 0.928), (1606, 0.928), (1607, 0.928),
                               (1608, 0.928), (1609, 0.933), (1610, 0.94), (1611, 0.944), (1612, 0.947), (1613, 0.949),
                               (1614, 0.952), (1615, 0.955), (1616, 0.958), (1617, 0.961), (1618, 0.963), (1619, 0.966),
                               (1620, 0.969), (1621, 0.972), (1622, 0.975), (1623, 0.978), (1624, 0.98), (1625, 0.983),
                               (1626, 0.985), (1627, 0.988), (1628, 0.989), (1629, 0.989), (1630, 0.988), (1631, 0.987),
                               (1632, 0.986), (1633, 0.985), (1634, 0.984), (1635, 0.983), (1636, 0.981), (1637, 0.98),
                               (1638, 0.979), (1639, 0.978), (1640, 0.977), (1641, 0.976), (1642, 0.975), (1643, 0.974),
                               (1644, 0.973), (1645, 0.972), (1646, 0.971), (1647, 0.97), (1648, 0.969), (1649, 0.969),
                               (1650, 0.968), (1651, 0.967), (1652, 0.967), (1653, 0.968), (1654, 0.97), (1655, 0.971),
                               (1656, 0.973), (1657, 0.975), (1658, 0.977), (1659, 0.979), (1660, 0.98), (1661, 0.982),
                               (1662, 0.983), (1663, 0.985), (1664, 0.986), (1665, 0.988), (1666, 0.988), (1667, 0.987),
                               (1668, 0.986), (1669, 0.985), (1670, 0.984), (1671, 0.984), (1672, 0.983), (1673, 0.983),
                               (1674, 0.982), (1675, 0.982), (1676, 0.981), (1677, 0.981), (1678, 0.98), (1679, 0.98),
                               (1680, 0.979), (1681, 0.979), (1682, 0.978), (1683, 0.978), (1684, 0.977), (1685, 0.977),
                               (1686, 0.976), (1687, 0.976), (1688, 0.975), (1689, 0.975), (1690, 0.974), (1691, 0.975),
                               (1692, 0.977), (1693, 0.978), (1694, 0.98), (1695, 0.982), (1696, 0.983), (1697, 0.985),
                               (1698, 0.987), (1699, 0.988), (1700, 0.99), (1701, 0.99), (1702, 0.991), (1703, 0.992),
                               (1704, 0.993), (1705, 0.993), (1706, 0.994), (1707, 0.995), (1708, 0.995), (1709, 0.996),
                               (1710, 0.997), (1711, 0.998), (1712, 0.998), (1713, 0.999), (1714, 0.999), (1715, 1.0),
                               (1716, 0.999), (1717, 0.998), (1718, 0.996), (1719, 0.995), (1720, 0.993), (1721, 0.992),
                               (1722, 0.99), (1723, 0.988), (1724, 0.986), (1725, 0.974), (1726, 0.982), (1727, 0.98),
                               (1728, 0.978), (1729, 0.976), (1730, 0.975), (1731, 0.973), (1732, 0.971), (1733, 0.969),
                               (1734, 0.967), (1735, 0.965), (1736, 0.963), (1737, 0.961), (1738, 0.96), (1739, 0.958),
                               (1740, 0.956), (1741, 0.955), (1742, 0.954), (1743, 0.953), (1744, 0.953), (1745, 0.952),
                               (1746, 0.951), (1747, 0.95), (1748, 0.95), (1749, 0.949), (1750, 0.948), (1751, 0.951),
                               (1752, 0.954), (1753, 0.957), (1754, 0.961), (1755, 0.964), (1756, 0.965), (1757, 0.964),
                               (1758, 0.962), (1759, 0.961), (1760, 0.96), (1761, 0.957), (1762, 0.953), (1763, 0.948),
                               (1764, 0.944), (1765, 0.94), (1766, 0.931), (1767, 0.92), (1768, 0.909), (1769, 0.898),
                               (1770, 0.887), (1771, 0.868), (1772, 0.846), (1773, 0.823), (1774, 0.801), (1775, 0.779),
                               (1776, 0.752), (1777, 0.723), (1778, 0.695), (1779, 0.666), (1780, 0.637), (1781, 0.607),
                               (1782, 0.577), (1783, 0.547), (1784, 0.516), (1785, 0.486), (1786, 0.456), (1787, 0.425),
                               (1788, 0.395), (1789, 0.365), (1790, 0.334), (1791, 0.313), (1792, 0.296), (1793, 0.279),
                               (1794, 0.262), (1795, 0.245), (1796, 0.228), (1797, 0.211), (1798, 0.194), (1799, 0.177),
                               (1800, 0.16), (1801, 0.149), (1802, 0.141), (1803, 0.133), (1804, 0.125), (1805, 0.117),
                               (1806, 0.109), (1807, 0.101), (1808, 0.093), (1809, 0.085), (1810, 0.077), (1811, 0.072),
                               (1812, 0.069), (1813, 0.066), (1814, 0.063), (1815, 0.06), (1816, 0.057), (1817, 0.054),
                               (1818, 0.051), (1819, 0.048), (1820, 0.045), (1821, 0.042), (1822, 0.04), (1823, 0.038),
                               (1824, 0.036), (1825, 0.033), (1826, 0.031), (1827, 0.029), (1828, 0.027), (1829, 0.025),
                               (1830, 0.022), (1831, 0.021), (1832, 0.021), (1833, 0.02), (1834, 0.02), (1835, 0.019),
                               (1836, 0.019), (1837, 0.018), (1838, 0.018), (1839, 0.017), (1840, 0.016), (1841, 0.016),
                               (1842, 0.015), (1843, 0.015), (1844, 0.014), (1845, 0.014), (1846, 0.013), (1847, 0.013),
                               (1848, 0.012), (1849, 0.012), (1850, 0.011), (1851, 0.01), (1852, 0.01), (1853, 0.01),
                               (1854, 0.009), (1855, 0.009), (1856, 0.009), (1857, 0.008), (1858, 0.008), (1859, 0.008),
                               (1860, 0.007), (1861, 0.007), (1862, 0.007), (1863, 0.006), (1864, 0.006), (1865, 0.005),
                               (1866, 0.005), (1867, 0.005), (1868, 0.004), (1869, 0.004), (1870, 0.004), (1871, 0.003),
                               (1872, 0.003), (1873, 0.003), (1874, 0.002), (1875, 0.002), (1876, 0.002), (1877, 0.001)]
        responses['SWIR-2'] = [(1956, 0.001), (1957, 0.001), (1958, 0.001), (1959, 0.002), (1960, 0.002), (1961, 0.002),
                               (1962, 0.002), (1963, 0.002), (1964, 0.002), (1965, 0.003), (1966, 0.003), (1967, 0.003),
                               (1968, 0.003), (1969, 0.003), (1970, 0.004), (1971, 0.004), (1972, 0.004), (1973, 0.004),
                               (1974, 0.004), (1975, 0.004), (1976, 0.005), (1977, 0.005), (1978, 0.005), (1979, 0.005),
                               (1980, 0.005), (1981, 0.006), (1982, 0.006), (1983, 0.006), (1984, 0.006), (1985, 0.006),
                               (1986, 0.007), (1987, 0.007), (1988, 0.007), (1989, 0.007), (1990, 0.007), (1991, 0.008),
                               (1992, 0.008), (1993, 0.008), (1994, 0.008), (1995, 0.008), (1996, 0.009), (1997, 0.009),
                               (1998, 0.009), (1999, 0.009), (2000, 0.009), (2001, 0.01), (2002, 0.01), (2003, 0.011),
                               (2004, 0.011), (2005, 0.012), (2006, 0.012), (2007, 0.013), (2008, 0.013), (2009, 0.014),
                               (2010, 0.014), (2011, 0.015), (2012, 0.015), (2013, 0.016), (2014, 0.016), (2015, 0.017),
                               (2016, 0.017), (2017, 0.018), (2018, 0.018), (2019, 0.019), (2020, 0.019), (2021, 0.021),
                               (2022, 0.023), (2023, 0.024), (2024, 0.026), (2025, 0.027), (2026, 0.029), (2027, 0.031),
                               (2028, 0.032), (2029, 0.034), (2030, 0.036), (2031, 0.037), (2032, 0.039), (2033, 0.041),
                               (2034, 0.042), (2035, 0.044), (2036, 0.046), (2037, 0.047), (2038, 0.049), (2039, 0.051),
                               (2040, 0.052), (2041, 0.054), (2042, 0.056), (2043, 0.057), (2044, 0.059), (2045, 0.061),
                               (2046, 0.062), (2047, 0.064), (2048, 0.066), (2049, 0.068), (2050, 0.069), (2051, 0.072),
                               (2052, 0.075), (2053, 0.078), (2054, 0.081), (2055, 0.084), (2056, 0.087), (2057, 0.09),
                               (2058, 0.093), (2059, 0.096), (2060, 0.1), (2061, 0.105), (2062, 0.109), (2063, 0.115),
                               (2064, 0.12), (2065, 0.125), (2066, 0.13), (2067, 0.135), (2068, 0.14), (2069, 0.145),
                               (2070, 0.15), (2071, 0.16), (2072, 0.17), (2073, 0.18), (2074, 0.19), (2075, 0.2),
                               (2076, 0.211), (2077, 0.221), (2078, 0.231), (2079, 0.241), (2080, 0.251), (2081, 0.265),
                               (2082, 0.28), (2083, 0.294), (2084, 0.308), (2085, 0.323), (2086, 0.337), (2087, 0.352),
                               (2088, 0.366), (2089, 0.38), (2090, 0.395), (2091, 0.409), (2092, 0.424), (2093, 0.438),
                               (2094, 0.453), (2095, 0.467), (2096, 0.482), (2097, 0.496), (2098, 0.511), (2099, 0.526),
                               (2100, 0.54), (2101, 0.556), (2102, 0.571), (2103, 0.586), (2104, 0.602), (2105, 0.617),
                               (2106, 0.633), (2107, 0.648), (2108, 0.664), (2109, 0.679), (2110, 0.695), (2111, 0.71),
                               (2112, 0.726), (2113, 0.742), (2114, 0.758), (2115, 0.773), (2116, 0.789), (2117, 0.805),
                               (2118, 0.821), (2119, 0.837), (2120, 0.853), (2121, 0.864), (2122, 0.876), (2123, 0.887),
                               (2124, 0.898), (2125, 0.91), (2126, 0.915), (2127, 0.92), (2128, 0.925), (2129, 0.931),
                               (2130, 0.936), (2131, 0.939), (2132, 0.941), (2133, 0.944), (2134, 0.947), (2135, 0.95),
                               (2136, 0.95), (2137, 0.95), (2138, 0.95), (2139, 0.95), (2140, 0.951), (2141, 0.95),
                               (2142, 0.95), (2143, 0.95), (2144, 0.949), (2145, 0.949), (2146, 0.946), (2147, 0.944),
                               (2148, 0.941), (2149, 0.938), (2150, 0.936), (2151, 0.937), (2152, 0.939), (2153, 0.941),
                               (2154, 0.942), (2155, 0.944), (2156, 0.944), (2157, 0.945), (2158, 0.945), (2159, 0.946),
                               (2160, 0.946), (2161, 0.947), (2162, 0.947), (2163, 0.947), (2164, 0.948), (2165, 0.948),
                               (2166, 0.951), (2167, 0.953), (2168, 0.956), (2169, 0.959), (2170, 0.962), (2171, 0.965),
                               (2172, 0.967), (2173, 0.97), (2174, 0.973), (2175, 0.976), (2176, 0.979), (2177, 0.982),
                               (2178, 0.985), (2179, 0.988), (2180, 0.991), (2181, 0.994), (2182, 0.996), (2183, 0.997),
                               (2184, 0.997), (2185, 0.998), (2186, 0.998), (2187, 0.998), (2188, 0.999), (2189, 0.999),
                               (2190, 0.999), (2191, 1.0), (2192, 1.0), (2193, 0.999), (2194, 0.999), (2195, 0.998),
                               (2196, 0.998), (2197, 0.997), (2198, 0.997), (2199, 0.996), (2200, 0.995), (2201, 0.995),
                               (2202, 0.995), (2203, 0.995), (2204, 0.994), (2205, 0.994), (2206, 0.994), (2207, 0.993),
                               (2208, 0.993), (2209, 0.993), (2210, 0.993), (2211, 0.992), (2212, 0.992), (2213, 0.992),
                               (2214, 0.991), (2215, 0.991), (2216, 0.991), (2217, 0.99), (2218, 0.99), (2219, 0.99),
                               (2220, 0.989), (2221, 0.989), (2222, 0.989), (2223, 0.988), (2224, 0.988), (2225, 0.987),
                               (2226, 0.981), (2227, 0.975), (2228, 0.969), (2229, 0.962), (2230, 0.956), (2231, 0.955),
                               (2232, 0.953), (2233, 0.952), (2234, 0.95), (2235, 0.949), (2236, 0.947), (2237, 0.946),
                               (2238, 0.945), (2239, 0.943), (2240, 0.942), (2241, 0.94), (2242, 0.938), (2243, 0.936),
                               (2244, 0.934), (2245, 0.932), (2246, 0.93), (2247, 0.928), (2248, 0.926), (2249, 0.924),
                               (2250, 0.922), (2251, 0.922), (2252, 0.921), (2253, 0.92), (2254, 0.92), (2255, 0.919),
                               (2256, 0.919), (2257, 0.918), (2258, 0.917), (2259, 0.917), (2260, 0.916), (2261, 0.915),
                               (2262, 0.914), (2263, 0.914), (2264, 0.913), (2265, 0.912), (2266, 0.911), (2267, 0.91),
                               (2268, 0.909), (2269, 0.908), (2270, 0.906), (2271, 0.905), (2272, 0.903), (2273, 0.901),
                               (2274, 0.9), (2275, 0.898), (2276, 0.896), (2277, 0.895), (2278, 0.893), (2279, 0.892),
                               (2280, 0.89), (2281, 0.883), (2282, 0.876), (2283, 0.87), (2284, 0.863), (2285, 0.856),
                               (2286, 0.849), (2287, 0.842), (2288, 0.836), (2289, 0.829), (2290, 0.822), (2291, 0.816),
                               (2292, 0.809), (2293, 0.803), (2294, 0.796), (2295, 0.79), (2296, 0.783), (2297, 0.777),
                               (2298, 0.77), (2299, 0.764), (2300, 0.757), (2301, 0.751), (2302, 0.746), (2303, 0.74),
                               (2304, 0.734), (2305, 0.728), (2306, 0.728), (2307, 0.728), (2308, 0.734), (2309, 0.741),
                               (2310, 0.747), (2311, 0.754), (2312, 0.76), (2313, 0.766), (2314, 0.772), (2315, 0.778),
                               (2316, 0.784), (2317, 0.79), (2318, 0.793), (2319, 0.802), (2320, 0.808), (2321, 0.819),
                               (2322, 0.83), (2323, 0.841), (2324, 0.852), (2325, 0.857), (2326, 0.863), (2327, 0.868),
                               (2328, 0.874), (2329, 0.874), (2330, 0.874), (2331, 0.874), (2332, 0.875), (2333, 0.868),
                               (2334, 0.861), (2335, 0.854), (2336, 0.836), (2337, 0.819), (2338, 0.801), (2339, 0.748),
                               (2340, 0.695), (2341, 0.669), (2342, 0.642), (2343, 0.616), (2344, 0.59), (2345, 0.564),
                               (2346, 0.537), (2347, 0.511), (2348, 0.484), (2349, 0.458), (2350, 0.431), (2351, 0.409),
                               (2352, 0.386), (2353, 0.364), (2354, 0.342), (2355, 0.319), (2356, 0.296), (2357, 0.274),
                               (2358, 0.251), (2359, 0.229), (2360, 0.206), (2361, 0.193), (2362, 0.18), (2363, 0.167),
                               (2364, 0.154), (2365, 0.141), (2366, 0.128), (2367, 0.115), (2368, 0.102), (2369, 0.089),
                               (2370, 0.076), (2371, 0.072), (2372, 0.068), (2373, 0.063), (2374, 0.059), (2375, 0.055),
                               (2376, 0.05), (2377, 0.046), (2378, 0.042), (2379, 0.037), (2380, 0.033), (2381, 0.031),
                               (2382, 0.029), (2383, 0.026), (2384, 0.024), (2385, 0.022), (2386, 0.02), (2387, 0.018),
                               (2388, 0.015), (2389, 0.013), (2390, 0.011), (2391, 0.01), (2392, 0.01), (2393, 0.009),
                               (2394, 0.009), (2395, 0.008), (2396, 0.008), (2397, 0.007), (2398, 0.007), (2399, 0.006),
                               (2400, 0.005), (2401, 0.005), (2402, 0.004), (2403, 0.004), (2404, 0.003), (2405, 0.003),
                               (2406, 0.002), (2407, 0.002), (2408, 0.001)]

        return responses
