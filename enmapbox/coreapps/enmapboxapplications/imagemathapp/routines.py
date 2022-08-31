import numpy
from numpy import *
import numpy.random as random

inputRasterByArray = dict()
outputRasterByArray = dict()
outputNoDataValueByArray = dict()
outputMetadataByArray = dict()
outputDescriptionsByArray = dict()
outputCategoryNamesByArray = dict()
outputCategoryColorsByArray = dict()


def noDataValue(array):
    '''noDataValue(array)

    Returns the `noDataValue` of the input GDAL raster dataset that is associated with the given numpy `array`.

    Examples
    --------
    >>> noDataValue(image)
    -9999
    '''
    return inputRasterByArray[id(array)].noDataValue()


def metadata(array):
    '''metadata(array)

    Returns the `metadata` dictionary of the input GDAL raster dataset that is associated with the given `array`.

    Examples
    --------
    >>> metadata(image)
    {'ENVI':
        {'byte_order': '0',
         'data_type': '2',
         'file_type': 'ENVI Standard',
         'bands': '177',
         'lines': '80',
         'coordinate_system_string': ['PROJCS["UTM_Zone_33N"', 'GEOGCS["GCS_WGS_1984"', 'DATUM["D_WGS_1984"', 'SPHEROID["WGS_1984"', '6378137.0', '298.257223563]]', 'PRIMEM["Greenwich"', '0.0]', 'UNIT["Degree"', '0.0174532925199433]]', 'PROJECTION["Transverse_Mercator"]', 'PARAMETER["False_Easting"', '500000.0]', 'PARAMETER["False_Northing"', '0.0]', 'PARAMETER["Central_Meridian"', '15.0]', 'PARAMETER["Scale_Factor"', '0.9996]', 'PARAMETER["Latitude_Of_Origin"', '0.0]', 'UNIT["Meter"', '1.0]]'],
         'interleave': 'bsq',
         'sensor_type': 'Unknown',
         'header_offset': '0',
         'samples': '60',
         'wavelength_units': 'Micrometers',
         'wavelength': [' 0.460000', ' 0.465000', ' 0.470000', ' 0.475000', ' 0.479000', ' 0.484000', ' 0.489000', ' 0.494000', ' 0.499000', ' 0.503000', ' 0.508000', ' 0.513000', ' 0.518000', ' 0.523000', ' 0.528000', ' 0.533000', ' 0.538000', ' 0.543000', ' 0.549000', ' 0.554000', ' 0.559000', ' 0.565000', ' 0.570000', ' 0.575000', ' 0.581000', ' 0.587000', ' 0.592000', ' 0.598000', ' 0.604000', ' 0.610000', ' 0.616000', ' 0.622000', ' 0.628000', ' 0.634000', ' 0.640000', ' 0.646000', ' 0.653000', ' 0.659000', ' 0.665000', ' 0.672000', ' 0.679000', ' 0.685000', ' 0.692000', ' 0.699000', ' 0.706000', ' 0.713000', ' 0.720000', ' 0.727000', ' 0.734000', ' 0.741000', ' 0.749000', ' 0.756000', ' 0.763000', ' 0.771000', ' 0.778000', ' 0.786000', ' 0.793000', ' 0.801000', ' 0.809000', ' 0.817000', ' 0.824000', ' 0.832000', ' 0.840000', ' 0.848000', ' 0.856000', ' 0.864000', ' 0.872000', ' 0.880000', ' 0.888000', ' 0.896000', ' 0.915000', ' 0.924000', ' 0.934000', ' 0.944000', ' 0.955000', ' 0.965000', ' 0.975000', ' 0.986000', ' 0.997000', ' 1.007000', ' 1.018000', ' 1.029000', ' 1.040000', ' 1.051000', ' 1.063000', ' 1.074000', ' 1.086000', ' 1.097000', ' 1.109000', ' 1.120000', ' 1.132000', ' 1.144000', ' 1.155000', ' 1.167000', ' 1.179000', ' 1.191000', ' 1.203000', ' 1.215000', ' 1.227000', ' 1.239000', ' 1.251000', ' 1.263000', ' 1.275000', ' 1.287000', ' 1.299000', ' 1.311000', ' 1.323000', ' 1.522000', ' 1.534000', ' 1.545000', ' 1.557000', ' 1.568000', ' 1.579000', ' 1.590000', ' 1.601000', ' 1.612000', ' 1.624000', ' 1.634000', ' 1.645000', ' 1.656000', ' 1.667000', ' 1.678000', ' 1.689000', ' 1.699000', ' 1.710000', ' 1.721000', ' 1.731000', ' 1.742000', ' 1.752000', ' 1.763000', ' 1.773000', ' 1.783000', ' 2.044000', ' 2.053000', ' 2.062000', ' 2.071000', ' 2.080000', ' 2.089000', ' 2.098000', ' 2.107000', ' 2.115000', ' 2.124000', ' 2.133000', ' 2.141000', ' 2.150000', ' 2.159000', ' 2.167000', ' 2.176000', ' 2.184000', ' 2.193000', ' 2.201000', ' 2.210000', ' 2.218000', ' 2.226000', ' 2.234000', ' 2.243000', ' 2.251000', ' 2.259000', ' 2.267000', ' 2.275000', ' 2.283000', ' 2.292000', ' 2.300000', ' 2.308000', ' 2.315000', ' 2.323000', ' 2.331000', ' 2.339000', ' 2.347000', ' 2.355000', ' 2.363000', ' 2.370000', ' 2.378000', ' 2.386000', ' 2.393000', ' 2.401000', ' 2.409000'],
         'band_names': ['band 8', ' band 9', ' band 10', ' band 11', ' band 12', ' band 13', ' band 14', ' band 15', ' band 16', ' band 17', ' band 18', ' band 19', ' band 20', ' band 21', ' band 22', ' band 23', ' band 24', ' band 25', ' band 26', ' band 27', ' band 28', ' band 29', ' band 30', ' band 31', ' band 32', ' band 33', ' band 34', ' band 35', ' band 36', ' band 37', ' band 38', ' band 39', ' band 40', ' band 41', ' band 42', ' band 43', ' band 44', ' band 45', ' band 46', ' band 47', ' band 48', ' band 49', ' band 50', ' band 51', ' band 52', ' band 53', ' band 54', ' band 55', ' band 56', ' band 57', ' band 58', ' band 59', ' band 60', ' band 61', ' band 62', ' band 63', ' band 64', ' band 65', ' band 66', ' band 67', ' band 68', ' band 69', ' band 70', ' band 71', ' band 72', ' band 73', ' band 74', ' band 75', ' band 76', ' band 77', ' band 91', ' band 92', ' band 93', ' band 94', ' band 95', ' band 96', ' band 97', ' band 98', ' band 99', ' band 100', ' band 101', ' band 102', ' band 103', ' band 104', ' band 105', ' band 106', ' band 107', ' band 108', ' band 109', ' band 110', ' band 111', ' band 112', ' band 113', ' band 114', ' band 115', ' band 116', ' band 117', ' band 118', ' band 119', ' band 120', ' band 121', ' band 122', ' band 123', ' band 124', ' band 125', ' band 126', ' band 127', ' band 144', ' band 145', ' band 146', ' band 147', ' band 148', ' band 149', ' band 150', ' band 151', ' band 152', ' band 153', ' band 154', ' band 155', ' band 156', ' band 157', ' band 158', ' band 159', ' band 160', ' band 161', ' band 162', ' band 163', ' band 164', ' band 165', ' band 166', ' band 167', ' band 168', ' band 195', ' band 196', ' band 197', ' band 198', ' band 199', ' band 200', ' band 201', ' band 202', ' band 203', ' band 204', ' band 205', ' band 206', ' band 207', ' band 208', ' band 209', ' band 210', ' band 211', ' band 212', ' band 213', ' band 214', ' band 215', ' band 216', ' band 217', ' band 218', ' band 219', ' band 220', ' band 221', ' band 222', ' band 223', ' band 224', ' band 225', ' band 226', ' band 227', ' band 228', ' band 229', ' band 230', ' band 231', ' band 232', ' band 233', ' band 234', ' band 235', ' band 236', ' band 237', ' band 238', ' band 239'],
         'z_plot_titles': ['wavelength [!7l!3m]!N', ' reflectance [* 10000]'],
         'fwhm': [' 0.005800', ' 0.005800', ' 0.005800', ' 0.005800', ' 0.005800', ' 0.005800', ' 0.005800', ' 0.005800', ' 0.005800', ' 0.005800', ' 0.005900', ' 0.005900', ' 0.006000', ' 0.006000', ' 0.006100', ' 0.006100', ' 0.006200', ' 0.006200', ' 0.006300', ' 0.006400', ' 0.006400', ' 0.006500', ' 0.006600', ' 0.006600', ' 0.006700', ' 0.006800', ' 0.006900', ' 0.006900', ' 0.007000', ' 0.007100', ' 0.007200', ' 0.007300', ' 0.007300', ' 0.007400', ' 0.007500', ' 0.007600', ' 0.007700', ' 0.007800', ' 0.007900', ' 0.007900', ' 0.008000', ' 0.008100', ' 0.008200', ' 0.008300', ' 0.008400', ' 0.008400', ' 0.008500', ' 0.008600', ' 0.008700', ' 0.008700', ' 0.008800', ' 0.008900', ' 0.008900', ' 0.009000', ' 0.009100', ' 0.009100', ' 0.009200', ' 0.009300', ' 0.009300', ' 0.009400', ' 0.009400', ' 0.009500', ' 0.009500', ' 0.009600', ' 0.009600', ' 0.009600', ' 0.009600', ' 0.009700', ' 0.009700', ' 0.009700', ' 0.011800', ' 0.011900', ' 0.012100', ' 0.012200', ' 0.012400', ' 0.012500', ' 0.012700', ' 0.012800', ' 0.012900', ' 0.013100', ' 0.013200', ' 0.013300', ' 0.013400', ' 0.013500', ' 0.013600', ' 0.013700', ' 0.013800', ' 0.013900', ' 0.014000', ' 0.014000', ' 0.014100', ' 0.014100', ' 0.014200', ' 0.014200', ' 0.014300', ' 0.014300', ' 0.014300', ' 0.014400', ' 0.014400', ' 0.014400', ' 0.014400', ' 0.014400', ' 0.014400', ' 0.014400', ' 0.014400', ' 0.014400', ' 0.014400', ' 0.013700', ' 0.013600', ' 0.013600', ' 0.013500', ' 0.013500', ' 0.013400', ' 0.013400', ' 0.013300', ' 0.013200', ' 0.013200', ' 0.013100', ' 0.013100', ' 0.013000', ' 0.012900', ' 0.012900', ' 0.012800', ' 0.012800', ' 0.012700', ' 0.012700', ' 0.012600', ' 0.012500', ' 0.012500', ' 0.012400', ' 0.012400', ' 0.012300', ' 0.010900', ' 0.010800', ' 0.010800', ' 0.010700', ' 0.010700', ' 0.010600', ' 0.010600', ' 0.010500', ' 0.010500', ' 0.010400', ' 0.010400', ' 0.010400', ' 0.010300', ' 0.010300', ' 0.010200', ' 0.010200', ' 0.010100', ' 0.010100', ' 0.010100', ' 0.010000', ' 0.010000', ' 0.009900', ' 0.009900', ' 0.009900', ' 0.009800', ' 0.009800', ' 0.009700', ' 0.009700', ' 0.009700', ' 0.009600', ' 0.009600', ' 0.009600', ' 0.009500', ' 0.009500', ' 0.009400', ' 0.009400', ' 0.009400', ' 0.009300', ' 0.009300', ' 0.009300', ' 0.009200', ' 0.009200', ' 0.009100', ' 0.009100', ' 0.009100'],
         'data_ignore_value': '-99'}}
    '''

    return inputRasterByArray[id(array)].metadataDict()


def descriptions(array):
    '''descriptions(array)

    Returns the band descriptions (aka. band names) list of the input GDAL raster dataset that is associated with the given `array`.

    Examples
    --------
    >>> descriptions(image)
    ['band 8', ' band 9', ' band 10', ' band 11', ' band 12', ' band 13', ' band 14', ' band 15', ' band 16', ' band 17', ' band 18', ' band 19', ' band 20', ' band 21', ' band 22', ' band 23', ' band 24', ' band 25', ' band 26', ' band 27', ' band 28', ' band 29', ' band 30', ' band 31', ' band 32', ' band 33', ' band 34', ' band 35', ' band 36', ' band 37', ' band 38', ' band 39', ' band 40', ' band 41', ' band 42', ' band 43', ' band 44', ' band 45', ' band 46', ' band 47', ' band 48', ' band 49', ' band 50', ' band 51', ' band 52', ' band 53', ' band 54', ' band 55', ' band 56', ' band 57', ' band 58', ' band 59', ' band 60', ' band 61', ' band 62', ' band 63', ' band 64', ' band 65', ' band 66', ' band 67', ' band 68', ' band 69', ' band 70', ' band 71', ' band 72', ' band 73', ' band 74', ' band 75', ' band 76', ' band 77', ' band 91', ' band 92', ' band 93', ' band 94', ' band 95', ' band 96', ' band 97', ' band 98', ' band 99', ' band 100', ' band 101', ' band 102', ' band 103', ' band 104', ' band 105', ' band 106', ' band 107', ' band 108', ' band 109', ' band 110', ' band 111', ' band 112', ' band 113', ' band 114', ' band 115', ' band 116', ' band 117', ' band 118', ' band 119', ' band 120', ' band 121', ' band 122', ' band 123', ' band 124', ' band 125', ' band 126', ' band 127', ' band 144', ' band 145', ' band 146', ' band 147', ' band 148', ' band 149', ' band 150', ' band 151', ' band 152', ' band 153', ' band 154', ' band 155', ' band 156', ' band 157', ' band 158', ' band 159', ' band 160', ' band 161', ' band 162', ' band 163', ' band 164', ' band 165', ' band 166', ' band 167', ' band 168', ' band 195', ' band 196', ' band 197', ' band 198', ' band 199', ' band 200', ' band 201', ' band 202', ' band 203', ' band 204', ' band 205', ' band 206', ' band 207', ' band 208', ' band 209', ' band 210', ' band 211', ' band 212', ' band 213', ' band 214', ' band 215', ' band 216', ' band 217', ' band 218', ' band 219', ' band 220', ' band 221', ' band 222', ' band 223', ' band 224', ' band 225', ' band 226', ' band 227', ' band 228', ' band 229', ' band 230', ' band 231', ' band 232', ' band 233', ' band 234', ' band 235', ' band 236', ' band 237', ' band 238', ' band 239']
    '''

    return inputRasterByArray[id(array)].descriptions()


def categoryNames(array):
    '''categoryNames(array)

    Returns the category names (aka. class names) list of the input GDAL raster dataset that is associated with the given `array`.

    Examples
    --------
    >>> categoryNames(image)
    ['unclassified', 'class 1', 'class 2', 'class 3']
    '''

    return inputRasterByArray[id(array)].categoryNames(0)


def categoryColors(array):
    '''categoryColors(array)

    Returns the category colors (aka. class lookup) RGBA-tuple list of the input GDAL raster dataset that is associated with the given `array`.

    Examples
    --------
    >>> categoryColors(image)
    [(0, 0, 0, 255), (230, 0, 0, 255), (152, 230, 0, 255), (38, 115, 0, 255)]
    '''

    return inputRasterByArray[id(array)].categoryColors(0)



def setNoDataValue(array, noDataValue):
    '''setNoDataValue(array, noDataValue)

    Sets the `noDataValue` of the output GDAL raster dataset that is associated with the given `array`.

    Parameters
    ----------
    array : numpy array
    noDataValue : number

    Examples
    --------
    >>> setMetadata(image, -9999)
    '''

    outputNoDataValueByArray[id(array)] = noDataValue


def setMetadata(array, metadata):
    '''setMetadata(array, metadata):

    Sets the `metadata` dictionary of the output GDAL raster dataset that is associated with the given `array`.

    Parameters
    ----------
    array : numpy array
    metadata : dictionary containing nested dictionaries, one for each metadata domain

    Examples
    --------
    >>> metadata = {'': {'my key': 'Hello World'}, 'ENVI': {'band_names': ['band 1', 'band 2', 'band 3']}
    >>> setMetadata(image, metadata)
    '''

    outputMetadataByArray[id(array)] = metadata


def setDescriptions(array, descriptions):
    '''setDescriptions(array, descriptions):

    Sets the band `descriptions` list of the output GDAL raster dataset that is associated with the given `array`.

    Parameters
    ----------
    array : numpy array
    descriptions : list of strings, one for each band

    Examples
    --------
    >>> descriptions = ['band 1', 'band 2', 'band 3']
    >>> setMetadata(image, descriptions)
    '''

    outputDescriptionsByArray[id(array)] = descriptions


def setCategoryNames(array, categoryNames):
    '''setCategoryNames(array, categoryNames):

    Sets the `categoryNames` list of the output GDAL raster dataset that is associated with the given `array`.

    Parameters
    ----------
    array : numpy array
    categoryNames : list of strings, one for each category

    Examples
    --------
    >>> categoryNames = ['unclassified', 'class 1', 'class 2', 'class 3']
    >>> setCategoryNames(image, categoryNames)
    '''

    outputCategoryNamesByArray[id(array)] = categoryNames


def setCategoryColors(array, categoryColors):
    '''setCategoryColors(array, categoryColors):

    Sets the `categoryColors` list of the output GDAL raster dataset that is associated with the given `array`.

    Parameters
    ----------
    array : numpy array
    categoryColors : list of RGBA color tuples, one for each category

    Examples
    --------
    >>> categoryColors = [(0, 0, 0, 255), (230, 0, 0, 255), (152, 230, 0, 255), (38, 115, 0, 255)]
    >>> setCategoryColors(image, categoryColors)
    '''

    outputCategoryColorsByArray[id(array)] = categoryColors
