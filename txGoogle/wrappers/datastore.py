'''
Created on 21 aug. 2014

@author: sjuul
'''
from txGoogle.services.datastore_ import Datastore
from txGoogle.services.datastore_ import Datasets
from txGoogle.sharedConnection import SharedConnection
from txGoogle.wrappers.gcdResponseHandler import GcdResponseHandler
from txGoogle.wrappers.gcd import checkKindsFormat
from txGoogle.wrappers.gcd import trySerialize
from urllib import quote as urlibQuoteEncode
from txGoogle.resource import Resource
from twisted.internet.task import LoopingCall
from txGoogle.wrappers.gcd import Key
from txGoogle.utils import chunks
import time
from twisted.python import log
import logging


MAX_ITEMS_PER_COMMIT = 500


class DatasetsWrapper(Datasets):

    def lookup(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, keys=None, transaction=None, readConsistency=None):
        if keys is not None:
            keys = [trySerialize(keyElem) for keyElem in keys]
        return Datasets.lookup(self, datasetId, prettyPrint=prettyPrint, fields=fields, quotaUser=quotaUser, oauth_token=oauth_token, key=key, userIp=userIp, alt=alt, keys=keys, transaction=transaction, readConsistency=readConsistency)

    def runQuery(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, startCursor=None, kinds=None, projection=None, groupBy=None, filters=None, indexed=None, limit=None, offset=None, endCursor=None, order=None, gqlQuery=None, transaction=None, readConsistency=None):
        assert datasetId is not None
        '''Query for entities.'''

        print 'Qry Kinds:{} Filter:{} Projection:{}'.format(kinds, filters, projection)

        if kinds:
            kinds = [checkKindsFormat(kind) for kind in kinds]

        ''''partitionId': {
            'namespace': namespace,
            'datasetId': datasetId,
        },'''
        queryParams = {
            'url': 'https://www.googleapis.com/datastore/v1beta2/datasets/{datasetId}/runQuery',
            'method': 'POST',
            'resultType': 'RunQueryResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
                'query': {
                    'startCursor': startCursor,
                    'kinds': kinds,
                    'projection': projection,
                    'order': order,
                    'filter': filters,
                    'limit': limit,
                    'offset': offset,
                    'endCursor': endCursor,
                    'groupBy': groupBy,
                },
                'gqlQuery': gqlQuery,
                'readOptions': {
                    'transaction': transaction,
                    'readConsistency': readConsistency,
                },
            },
        }
        return self._request(queryParams)

    def query(self, datasetId, kinds, queryFilter=None, readConsistency=None, properties=None, limit=None):
        # assert kinds is not None
        if queryFilter and hasattr(queryFilter, 'serialize'):
            queryFilter = queryFilter.serialize()
        if properties:
            projection = [{'property': {'name': prt}} for prt in properties]
        else:
            projection = None
        return self.runQuery(datasetId, kinds=kinds, filters=queryFilter, readConsistency=readConsistency, projection=projection, limit=limit)

    def commit(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ignoreReadOnly=None, transaction=None, mode=None, insert=None, force=None, insertAutoId=None, update=None, delete=None, upsert=None):
        if key is not None and not isinstance(key, (basestring, Key)):
            raise Exception('got non key')
        if datasetId is None:
            raise Exception('datasetId cannot be None')
        if update:
            update = [trySerialize(obj) for obj in update]
        if upsert:
            upsert = [trySerialize(obj) for obj in upsert]
        if delete:
            delete = [trySerialize(obj) for obj in delete]
        if insertAutoId:
            insertAutoId = [trySerialize(obj) for obj in insertAutoId]
        if insert:
            insert = [trySerialize(obj) for obj in insert]
        if not mode:
            mode = 'NON_TRANSACTIONAL'
        return Datasets.commit(self, datasetId, prettyPrint=prettyPrint, fields=fields, quotaUser=quotaUser, oauth_token=oauth_token, key=key, userIp=userIp, alt=alt, ignoreReadOnly=ignoreReadOnly, transaction=transaction, mode=mode, insert=insert, force=force, insertAutoId=insertAutoId, update=update, delete=delete, upsert=upsert)


class BatchOperationTimeHandler(object):

    def __init__(self, service, projectId, loopTime):
        if projectId is None:
            raise Exception('Batchoperations require a projectId')
        self._loopingCall = LoopingCall(self._commit)
        self._loopTime = loopTime
        self._OrmOperations = {}
        self._service = service
        self._projectId = projectId

    def _getChunks(self):
        return chunks(self._OrmOperations.items(), MAX_ITEMS_PER_COMMIT)

    def _commit(self):
        if self._OrmOperations:
            for chunk in self._getChunks():
                ops = {}
                cnt = 0
                for obj, operation in chunk:
                    if operation not in ops:
                        ops[operation] = []
                    ops[operation].append(obj)
                    cnt += 1
                if ops:
                    startTs = time.time()
                    try:
                        dfd = self._service.datasets.commit(self._projectId, **ops)
                        dfd.addCallback(self._onSuccess, cnt, startTs)
                        dfd.addErrback(self._onFail)
                    except:
                        log.err()
        self._OrmOperations = {}

    def _onSuccess(self, result, cnt, startTs):
        delta = time.time() - startTs
        indexUpdates = result.get('mutationResult', {}).get('indexUpdates', 0)
        msg = 'updates: {} indexUpdates: {} execution time: {:.3f} sec'.format(cnt, indexUpdates, delta)
        print msg
        log.msg(msg, logLevel=logging.INFO)

    def _onFail(self, fail):
        log.err(fail)

    def add(self, obj, operation):
        self._OrmOperations[obj] = operation
        if not self._loopingCall.running:
            self._loopingCall.start(self._loopTime, now=False)

    def extractAll(self):
        all = self._OrmOperations
        self._OrmOperations = {}
        return all

    def stop(self):
        if self._loopingCall.running:
            self._loopingCall.stop()


class BatchOperations(Resource):
    def __init__(self, service, conn, loopTimes=None, projectId=None, *args, **kwargs):
        super(BatchOperations, self).__init__(service, conn, *args, **kwargs)
        self._batchOperationTimeHandlers = {}
        if loopTimes is None:
            loopTimes = [1, 20, 60, 300]
        for loopTime in loopTimes:
            self._batchOperationTimeHandlers[loopTime] = BatchOperationTimeHandler(service, projectId, loopTime)

    def upsert(self, entity, loopTime=1):
        self._addOperation(entity, loopTime, 'upsert')

    def update(self, entity, loopTime=1):
        self._addOperation(entity, loopTime, 'update')

    def delete(self, key, loopTime=1):
        if not isinstance(key, Key):
            raise Exception('Key expected in delete')
        self._addOperation(key, loopTime, 'delete')

    def insertAutoId(self, entity, loopTime=1):
        self._addOperation(entity, loopTime, 'insertAutoId')

    def insert(self, entity, loopTime=1):
        self._addOperation(entity, loopTime, 'insert')

    def _addOperation(self, obj, loopTime, operation):
        if loopTime not in self._batchOperationTimeHandlers:
            raise Exception('Explicitly declare the loopIntervals in advance, {} sec does not exist'.format(loopTime))
        self._batchOperationTimeHandlers[loopTime].add(obj, operation)

    def extractAll(self):
        output = {}
        for handler in self._batchOperationTimeHandlers.values():
            output.update(handler.extractAll())
        return output

    def stop(self):
        for handler in self._batchOperationTimeHandlers.values():
            handler.stop()


class DatastoreWrapper(Datastore):

    def __init__(self, conn=None, scopes=None, looptimes=None, projectId=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        kwargs['responseCls'] = GcdResponseHandler
        super(Datastore, self).__init__(conn, *args, **kwargs)
        self.datasets = DatasetsWrapper(self, conn, *args, **kwargs)
        self.batchOperations = BatchOperations(self, conn, looptimes, projectId, *args, **kwargs)


if __name__ == '__main__':
    from twisted.internet import reactor
    from txGoogle.wrappers.gcd import QueryFilter
    from txGoogle.wrappers.gcd import setGlobalGcdServiceAndProjectId
    from txGoogle.asyncUtils import printCb
    conn = SharedConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/GcdCredentials.json')
    gcd = DatastoreWrapper(conn)
    conn.connect()
    # getEntities(kind='Host', keysOnly=True, parentCore_eq=coreUuid)
    setGlobalGcdServiceAndProjectId(gcd, 'over-sight')
    #dfd = gcd.datasets.query('over-sight', kinds=['Host'], queryFilter=QueryFilter().equal('parentCore', 'e6b3265a8031-f5885503208d'))
    dfd = gcd.datasets.query('over-sight', queryFilter=QueryFilter().equal('__key__', Key('Customer', 'e6b3265a8031', 'Host', 'e6b3265a8031-f5885503208d')))
    dfd.addCallback(printCb)
    dfd.addErrback(printCb)
    reactor.run()
