'''
Created on 26 jun. 2014

@author: sjuul
'''
from txGoogle.asyncUtils import mapFunToItems
from txGoogle.asyncUtils import addPrintCbs
from txGoogle.asyncUtils import mapFunToItemsSequentially
from txGoogle.services.bigquery_ import Bigquery
from txGoogle.services.bigquery_ import Tables
from txGoogle.services.bigquery_ import Datasets
from txGoogle.services.bigquery_ import Jobs
from txGoogle.services.bigquery_ import Tabledata
from txGoogle.services.bigquery_ import Projects
from txGoogle.wrappers.bigQueryResponseHandler import BigQueryResponseHandler

'''
Reference: https://developers.google.com/bigquery/docs/reference/v2/
'''

DEFAULT_BQ_CHUNK_SIZE = 1000


def splitRecordsToChuncks(records):
    for i in xrange(0, len(records), DEFAULT_BQ_CHUNK_SIZE):
        yield records[i:i + DEFAULT_BQ_CHUNK_SIZE]


class TablesWrapper(Tables):

    def copy(self, srcProjectId, srcDatasetId, srcTableId, dstProjectId, dstDatasetId, dstTableId):
        jobData = {
             'projectId': srcProjectId,
             'configuration': {
                'copy': {
                    'sourceTable': {
                    'projectId': srcProjectId,
                    'datasetId': srcDatasetId,
                    'tableId': srcTableId
                  },
                    'destinationTable': {
                    'projectId': dstProjectId,
                    'datasetId': dstDatasetId,
                    'tableId': dstTableId
                  }
               }
            }
        }
        queryParams = {
            'projectId': projectId,
            'method': 'POST',
            'httpBodyParams': jobData,
            'resultType': 'job',
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/jobs'
        }
        return self._request(queryParams)

    def rename(self, projectId, datasetId, oldTableId, newTableId):
        dfd = self.copyTable(projectId, datasetId, oldTableId, projectId, datasetId, newTableId)

        @dfd.addCallback
        def onTableCopied(dummy):
            self.deleteTable(projectId, datasetId, oldTableId)
        return dfd

    def _extractTableIds(self, result):
        return [table['tableReference']['tableId'] for table in result.get('tables', [])]

    def getIds(self, projectId, datasetId):
        dfd = self.list(projectId=projectId, datasetId=datasetId)
        dfd.addCallback(self._extractTableIds)
        return dfd


class TabledataWrapper(Tabledata):

    def streamParallel(self, projectId, datasetId, tableId, records):
        if len(records) > DEFAULT_BQ_CHUNK_SIZE:
            return mapFunToItems(splitRecordsToChuncks(records), self.insertRows, projectId=projectId, datasetId=datasetId, tableId=tableId)
        else:
            return self._abq.tabledata.insertRows(records, self._projectId, datasetId, tableId)

    def streamSequential(self, projectId, datasetId, tableId, records):
        if len(records) > DEFAULT_BQ_CHUNK_SIZE:
            return mapFunToItemsSequentially(splitRecordsToChuncks(records), self.insertRows, projectId=projectId, datasetId=datasetId, tableId=tableId)
        else:
            return self._abq.tabledata.insertRows(records, self._projectId, datasetId, tableId)

    def insertRows(self, rows, projectId, datasetId, tableId):
        rows = [{"json": record} for record in rows]
        return self.insertAll(projectId=projectId, tableId=tableId, datasetId=datasetId, rows=rows, kind='bigquery#tableDataInsertAllRequest')


class JobsWrapper(Jobs):

    def _extractRows(self, inp):
        return inp.get('rows', [])

    def query(self, projectId, query, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, timeoutMs=None, kind=None, dryRun=None, useQueryCache=None, projectId_=None, datasetId=None, maxResults=None, preserveNulls=None):
        dfd = Jobs.query(self, projectId, query, prettyPrint, fields, quotaUser, oauth_token, key, userIp, alt, timeoutMs, kind, dryRun, useQueryCache, projectId_, datasetId, maxResults, preserveNulls)
        dfd.addCallback(self._extractRows)
        return dfd


class BigQueryWrapper(Bigquery):

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        kwargs['responseCls'] = BigQueryResponseHandler
        super(Bigquery, self).__init__(conn, *args, **kwargs)
        self.tables = TablesWrapper(conn, *args, **kwargs)
        self.datasets = Datasets(conn, *args, **kwargs)
        self.jobs = JobsWrapper(conn, *args, **kwargs)
        self.tabledata = TabledataWrapper(conn, *args, **kwargs)
        self.projects = Projects(conn, *args, **kwargs)


if __name__ == '__main__':
    from txGoogle.sharedConnection import SharedConnection
    from twisted.internet import reactor
    conn = SharedConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/asyncBqCredentials.json')
    abq = BigQueryWrapper(conn)
    conn.connect()

    prod = True
    if prod:
        projectId = 'detect-analyze-notify-01a'
        datasetId = 'cust_711f9f25ed85'
        tableId = 'perf_201406_005056ad452d'
    else:
        projectId = 'over-sight'
        datasetId = 'cust_e6b3265a8031'
        tableId = 'log_201407'

    # queryStr = "SELECT probeName, checkName, type, itemName, propertyName, value, timestamp\n        FROM TABLE_QUERY(cust_23eb8fd09fbc, 'table_id CONTAINS \"perf_\" AND table_id CONTAINS \"_1e0895f63693\" AND INTEGER(SUBSTR(table_id, 6, 6)) >= 201408 AND INTEGER(SUBSTR(table_id, 6, 6)) <= 201408')\n        WHERE timestamp > 1407315364000000\n        AND timestamp < 1408006564000000\n        ORDER BY probeName, checkName, type, itemName, propertyName, timestamp"
    queryStr = "SELECT * FROM TABLE_QUERY(cust_23eb8fd09fbc, 'table_id CONTAINS \"log_\" AND INTEGER(SUBSTR(table_id, 5, 6)) >= 201308 AND INTEGER(SUBSTR(table_id, 5, 6)) <= 201408') WHERE (LogType = 8)"
    dfds = []
    #dfds.append(aBq.getJob(projectId, 'job_VJo4zEhFOUNZ5lmPGonPcOp1OJE'))
    dfds.append(abq.jobs.query(projectId=projectId, query=queryStr))
    #dfds.append(aBq.query(projectId, datasetId, queryStr))
    #dfds.append(aBq.getTableData(projectId, datasetId, tableId))
    # dfds.append(aBq.getTables(projectId, datasetId))
    #dfds.append(aBq.getTable(projectId, datasetId, tableId))
    #dfds.append(aBq.getTables(projectId, datasetId))
    # dfds.append(aBq.createTable(projectId, datasetId, tableId, fields, expirationMiliTs, friendlyName, description))

    # dfds.append(aBq.copyTable(projectId, datasetId, tableId, projectId, datasetId, tableId + '_2'))
    # dfds.append(aBq.deleteTable(projectId, datasetId, tableId + '_2'))
    # dfds.append(aBq.renameTable(projectId, datasetId, tableId + '_2', tableId))

    #dfds.append(aBq.createTable(projectId, datasetId, tableId, {}))
    # records = [{'fieldname': str(a)} for a in xrange(1000)]
    #dfds.append(aBq.streamingInsertParallel(projectId, datasetId, tableId, records))
    #dfds += aBq.streamingInsertSequential(projectId, datasetId, tableId, records)
    '''from generic.osgoogle.asyncUtils import mapFunToItems
    from twisted.internet.defer import succeed

    def renameFun(tableId, projectId, datasetId):
        if 'perf_' not in tableId:
            return succeed('Skipped')
        splitted = tableId.split('_')
        newtableId = '_'.join([splitted[0], splitted[2], splitted[1]])
        return aBq.renameTable(projectId, datasetId, tableId, newtableId)
    dfdGetTables = aBq.getTableIds(projectId, datasetId)
    dfdGetTables.addCallback(mapFunToItems, renameFun, projectId, datasetId)
    dfds.append(dfdGetTables)'''
    addPrintCbs(dfds)
    reactor.run()
