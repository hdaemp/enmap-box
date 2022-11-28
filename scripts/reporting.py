"""
This scripts generates some reports stats related to the EnMAP-Box repository
"""
import csv
import datetime
import json
import os
import pathlib
import re

import pandas as pd
from xlsxwriter.workbook import Workbook

import enmapbox.testing
from enmapbox import DIR_REPO_TMP, EnMAPBox
from enmapbox import initAll
from enmapbox.algorithmprovider import EnMAPBoxProcessingProvider
from enmapbox.testing import start_app
from qgis.core import QgsProcessingOutputRasterLayer, QgsProcessingParameterBoolean, QgsProcessingOutputHtml, \
    QgsProcessingParameterFeatureSink, QgsProcessingOutputFile, QgsProcessingParameterFeatureSource, \
    QgsProcessingOutputVectorLayer, QgsProcessingParameterFolderDestination, QgsProcessingOutputFolder, \
    QgsProcessingParameterMultipleLayers, QgsProcessing
from qgis.core import QgsProcessingAlgorithm, QgsProcessingParameterRasterLayer, QgsProcessingParameterVectorLayer, \
    QgsProcessingParameterMapLayer, QgsProcessingParameterEnum, QgsProcessingParameterRasterDestination, \
    QgsProcessingParameterVectorDestination, QgsProcessingParameterFile, QgsProcessingParameterFileDestination

"""
Syntax github issue request:
https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests

author:jakimowb type:issue created:>=2022-07-01 created:<=2022-12-31

"""


class TestReporting(enmapbox.testing.TestCase):

    def test_report_processingalgorithms(self):
        """
        Lists the names of all QgsProcessingAlgorithms in a XLSX.
        """
        path_xlsx = pathlib.Path(DIR_REPO_TMP) / 'processingalgorithms.xlsx'
        os.makedirs(path_xlsx.parent, exist_ok=True)
        app = start_app()
        initAll()
        emb = EnMAPBox()
        provider: EnMAPBoxProcessingProvider = emb.processingProvider()


        DATA = {k:[] for k in ['group', 'name', 'in', 'out', 'id', 'description', 'help']}

        NOT_HANDLED = set()
        LUT_LAYERTYPE = {QgsProcessing.SourceType.TypeMapLayer: ['R','V'],
                         QgsProcessing.SourceType.TypeFile: ['F'],
                         QgsProcessing.SourceType.TypeRaster: ['R'],
                         }
        for t in [QgsProcessing.SourceType.TypeVector, QgsProcessing.SourceType.TypeVectorAnyGeometry,
                  QgsProcessing.SourceType.TypeVectorPoint,
                  QgsProcessing.SourceType.TypeVectorLine,
                  QgsProcessing.SourceType.TypeVectorPolygon]:
            LUT_LAYERTYPE[t] = ['V']
        def dataString(parameters) -> str:
            data_sources = set()
            for p in parameters:
                if isinstance(p, (QgsProcessingParameterRasterLayer, QgsProcessingParameterRasterDestination,
                                  QgsProcessingOutputRasterLayer)):
                    data_sources.add('R')
                elif isinstance(p, (QgsProcessingParameterVectorLayer, QgsProcessingOutputVectorLayer,
                                    QgsProcessingParameterVectorDestination,
                                    QgsProcessingParameterFeatureSource, QgsProcessingParameterFeatureSink)):
                    data_sources.add('V')
                elif isinstance(p, QgsProcessingParameterMapLayer):
                    data_sources.add('V')
                    data_sources.add('R')
                elif isinstance(p, QgsProcessingParameterMultipleLayers):
                    t = p.layerType()
                    if t in LUT_LAYERTYPE.keys():
                        data_sources.update(LUT_LAYERTYPE[t])

                elif isinstance(p, (QgsProcessingParameterFile, QgsProcessingParameterFileDestination,
                                    QgsProcessingOutputFile,
                                    QgsProcessingParameterFolderDestination, QgsProcessingOutputFolder)):
                    data_sources.add('F')
                elif isinstance(p, (QgsProcessingOutputHtml,)):
                    data_sources.add('H')
                elif isinstance(p, (QgsProcessingParameterEnum, QgsProcessingParameterBoolean)):
                    pass
                else:
                    NOT_HANDLED.add(p.__class__.__name__)
            return ''.join(sorted(data_sources))


        for a in provider.algorithms():
            a: QgsProcessingAlgorithm
            DATA['id'].append(a.id())
            DATA['name'].append(a.name())
            DATA['group'].append(a.group())
            DATA['description'].append(re.sub('\n', ' ', a.shortDescription()))
            DATA['help'].append(a.shortHelpString())
            DATA['in'].append(dataString(a.parameterDefinitions()))
            DATA['out'].append(dataString(a.outputDefinitions()))

        df = pd.DataFrame.from_records(DATA)
        column_order = ['group', 'name', 'in', 'out', 'description', 'id', 'help']
        df = df.reindex(columns=column_order)

        df.sort_values(by=['group', 'name'], inplace=True)

        if len(NOT_HANDLED) > 0:
            print('Not handled data types:')
            for p in NOT_HANDLED:
                print(p)
        with pd.ExcelWriter(path_xlsx.as_posix()) as writer:
            df.to_excel(writer, sheet_name='EnMAPBox_PAs')

        s = ""

    def test_report_bitbucket_issues(self):
        # 1. open bitbucket,
        # goto repository settings -> issues -> Import & export
        # 2. export issues, extract zip file and copy db-2.0.json to JSON_DIR (defaults to <repo>/tmp)
        # 3. set report period with start_date / end_date
        JSON_DIR = pathlib.Path(__file__).parents[1] / 'tmp'
        start_date = datetime.date(2022, 1, 1)
        end_date = datetime.date(2022, 6, 30)

        PATH_DB_JSON = JSON_DIR / 'db-2.0.json'
        PATH_CSV_REPORT = JSON_DIR / f'issue_report_{start_date}_{end_date}.csv'
        assert PATH_DB_JSON.is_file(), 'No db-2.0.json, no stats!'
        assert start_date < end_date

        def csv2xlsx(path_csv):
            path_csv = pathlib.Path(path_csv)
            path_xlsx = path_csv.parent / f'{os.path.splitext(path_csv.name)[0]}.xlsx'
            workbook = Workbook(path_xlsx)
            # float_format = workbook.add_format({'num_format': ''})
            worksheet = workbook.add_worksheet()
            rxIsInt = re.compile(r'^\d+$')
            rxIsFloat = re.compile(r'^\d+([.,]\d*)?$')
            with open(path_csv, 'rt', encoding='utf8') as f:
                reader = csv.reader(f)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        if rxIsInt.match(col):
                            col = int(col)
                        elif rxIsFloat.match(col):
                            col = float(col)
                        worksheet.write(r, c, col)
            workbook.close()

        with open(PATH_DB_JSON, 'r', encoding='utf-8') as f:
            DB = json.load(f)

        # DS = pd.read_json(PATH_DB_JSON.as_posix())
        ISSUES = DB['issues']

        CREATED_ISSUES = [i for i in ISSUES if start_date
                          <= datetime.datetime.fromisoformat(i['created_on']).date()
                          <= end_date]
        UPDATED_ISSUES = [i for i in ISSUES if start_date
                          <= datetime.datetime.fromisoformat(i['updated_on']).date()
                          <= end_date]

        def byKey(ISSUES: list, key: str) -> dict:
            R = dict()
            for issue in ISSUES:
                k = issue[key]
                L = R.get(k, [])
                L.append(issue)
                R[k] = L
            return R

        CREATED_BY_STATUS = byKey(CREATED_ISSUES, 'status')
        UPDATED_BY_STATUS = byKey(UPDATED_ISSUES, 'status')

        print(f'Created: {len(CREATED_ISSUES)}')
        for k in sorted(CREATED_BY_STATUS.keys()):
            print(f'\t{k}: {len(CREATED_BY_STATUS[k])}')

        print(f'Updated: {len(UPDATED_ISSUES)}')
        for k in sorted(UPDATED_BY_STATUS.keys()):
            print(f'\t{k}: {len(UPDATED_BY_STATUS[k])}')

        with open(PATH_CSV_REPORT, 'w', encoding='utf-8', newline='') as f:
            states = ['new', 'open', 'on hold', 'resolved', 'closed', 'duplicate', 'wontfix', 'invalid']
            fieldnames = ['action', 'total'] + states
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            total_created = total_updated = 0
            ROW1 = {'action': 'created'}
            ROW2 = {'action': 'updated'}

            for s in states:
                total_created += len(CREATED_BY_STATUS.get(s, []))
                total_updated += len(UPDATED_BY_STATUS.get(s, []))
                ROW1[s] = len(CREATED_BY_STATUS.get(s, []))
                ROW2[s] = len(UPDATED_BY_STATUS.get(s, []))
            ROW1['total'] = total_created
            ROW2['total'] = total_updated
            writer.writerow(ROW1)
            writer.writerow(ROW2)

        csv2xlsx(PATH_CSV_REPORT)