'''
Created on 26 jun. 2014

@author: sjuul
'''
from txGoogle.asyncUtils import mapFunToItems, addPrintCbs
from txGoogle.asyncUtils import mapFunToItemsSequentially
from txGoogle.services.bigquery_ import Bigquery
from txGoogle.wrappers.bigQueryResponseHandler import BigQueryResponseHandler

'''
Reference: https://developers.google.com/bigquery/docs/reference/v2/
'''

DEFAULT_BQ_CHUNK_SIZE = 1000


def splitRecordsToChuncks(records):
    for i in xrange(0, len(records), DEFAULT_BQ_CHUNK_SIZE):
        yield records[i:i + DEFAULT_BQ_CHUNK_SIZE]


def _copyTable(self, srcProjectId, srcDatasetId, srcTableId, dstProjectId, dstDatasetId, dstTableId):
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


def _renameTable(self, projectId, datasetId, oldTableId, newTableId):
    dfd = self.copyTable(projectId, datasetId, oldTableId, projectId, datasetId, newTableId)

    @dfd.addCallback
    def onTableCopied(dummy):
        self.deleteTable(projectId, datasetId, oldTableId)
    return dfd


def _getTableIds(self, projectId, datasetId):
    dfd = self.getTables(projectId, datasetId)
    dfd.addCallback(_extractTableIds)
    return dfd


def _extractTableIds(tables):
    return [table['tableReference']['tableId'] for table in tables]


def _streamingInsertParallel(self, projectId, datasetId, tableId, records):
    return mapFunToItems(splitRecordsToChuncks(records), self.insertAll, projectId=projectId, datasetId=datasetId, tableId=tableId)


def _streamingInsertSequential(self, projectId, datasetId, tableId, records):
    return mapFunToItemsSequentially(splitRecordsToChuncks(records), self.insertAll, projectId=projectId, datasetId=datasetId, tableId=tableId)


class BigQueryWrapper(Bigquery):

    def __init__(self, *args, **kwargs):
        kwargs['responseCls'] = BigQueryResponseHandler
        super(BigQueryWrapper, self).__init__(*args, **kwargs)
        self.tables.copy = _copyTable
        self.tables.rename = _renameTable
        self.tables.getIds = _getTableIds
        self.tabledata.streamParallel = _streamingInsertParallel
        self.tabledata.streamSequential = _streamingInsertSequential


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
