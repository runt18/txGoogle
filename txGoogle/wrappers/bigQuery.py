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
        return [table['tableReference']['tableId'] for table in result]

    def getIds(self, projectId, datasetId):
        dfd = self.list(projectId=projectId, datasetId=datasetId)
        dfd.addCallback(self._extractTableIds)
        return dfd

    def extractPropery(self, item, property):
        if property in item:
            return item[property]

    def getSize(self, projectId, datasetId, tableId):
        dfd = self.get(projectId=projectId, tableId=tableId, datasetId=datasetId, fields='numBytes')
        dfd.addCallback(self.extractPropery, 'numBytes')
        return dfd


class TabledataWrapper(Tabledata):

    def streamParallel(self, projectId, datasetId, tableId, records):
        if len(records) > DEFAULT_BQ_CHUNK_SIZE:
            return mapFunToItems(splitRecordsToChuncks(records), self.insertRows, projectId=projectId, datasetId=datasetId, tableId=tableId)
        else:
            return self.insertRows(records, projectId, datasetId, tableId)

    def streamSequential(self, projectId, datasetId, tableId, records):
        if len(records) > DEFAULT_BQ_CHUNK_SIZE:
            return mapFunToItemsSequentially(splitRecordsToChuncks(records), self.insertRows, projectId=projectId, datasetId=datasetId, tableId=tableId)
        else:
            return self.insertRows(records, projectId, datasetId, tableId)

    def insertRows(self, rows, projectId, datasetId, tableId):
        rows = [{"json": record} for record in rows]
        return self.insertAll(projectId=projectId, tableId=tableId, datasetId=datasetId, rows=rows, kind='bigquery#tableDataInsertAllRequest')


class JobsWrapper(Jobs):

    def query(self, projectId, query, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, timeoutMs=None, kind=None, dryRun=None, useQueryCache=None, projectId_=None, datasetId=None, maxResults=None, preserveNulls=None):
        dfd = Jobs.query(self, projectId, query, prettyPrint, fields, quotaUser, oauth_token, key, userIp, alt, timeoutMs, kind, dryRun, useQueryCache, projectId_, datasetId, maxResults, preserveNulls)
        return dfd


class DatasetsWrapper(Datasets):

    def getSize(self, projectId, datasetId):
        def getTableSize(tableId):
            return self._service.tables.getSize(projectId, datasetId, tableId)

        dfd = self._service.tables.getIds(projectId, datasetId)
        dfd.addCallback(mapFunToItems, getTableSize)
        dfd.addCallback(self._total)
        return dfd

    def _total(self, gen):
        total = 0
        for item in gen:
            if item[1] is not None:
                total += int(item[1])
        return total


class BigQueryWrapper(Bigquery):

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        kwargs['responseCls'] = BigQueryResponseHandler
        super(Bigquery, self).__init__(conn, *args, **kwargs)
        self.tables = TablesWrapper(self, conn, *args, **kwargs)
        self.datasets = DatasetsWrapper(self, conn, *args, **kwargs)
        self.jobs = JobsWrapper(self, conn, *args, **kwargs)
        self.tabledata = TabledataWrapper(self, conn, *args, **kwargs)
        self.projects = Projects(self, conn, *args, **kwargs)


if __name__ == '__main__':
    from txGoogle.sharedConnection import SharedConnection
    from txGoogle.asyncUtils import printCb
    from twisted.internet import reactor
    conn = SharedConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/asyncBqCredentials.json')
    abq = BigQueryWrapper(conn)
    conn.connect()
    dfd = abq.jobs.query(projectId='detect-analyze-notify-01a', datasetId='samples', query='SELECT * FROM [publicdata:samples.shakespeare] limit 10', maxResults=100)
    dfd.addCallback(printCb)
    dfd.addErrback(printCb)
    reactor.run()
