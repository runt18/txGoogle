from txGoogle.service import Service
from urllib import quote as urlibQuoteEncode
from txGoogle.resource import Resource


class Datasets(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Datasets, self).__init__(service, conn, *args, **kwargs)

    def allocateIds(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, keys=None):
        '''Allocate IDs for incomplete keys (useful for referencing an entity before it is inserted).'''
        queryParams = {
            'url': 'https://www.googleapis.com/datastore/v1beta2/datasets/{datasetId}/allocateIds',
            'method': 'POST',
            'resultType': 'AllocateIdsResponse',
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
                'keys': keys,
            },
        }
        return self._request(queryParams)

    def rollback(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, transaction=None):
        '''Roll back a transaction.'''
        queryParams = {
            'url': 'https://www.googleapis.com/datastore/v1beta2/datasets/{datasetId}/rollback',
            'method': 'POST',
            'resultType': 'RollbackResponse',
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
                'transaction': transaction,
            },
        }
        return self._request(queryParams)

    def beginTransaction(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, isolationLevel=None):
        '''Begin a new transaction.'''
        queryParams = {
            'url': 'https://www.googleapis.com/datastore/v1beta2/datasets/{datasetId}/beginTransaction',
            'method': 'POST',
            'resultType': 'BeginTransactionResponse',
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
                'isolationLevel': isolationLevel,
            },
        }
        return self._request(queryParams)

    def lookup(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, keys=None, transaction=None, readConsistency=None):
        '''Look up some entities by key.'''
        queryParams = {
            'url': 'https://www.googleapis.com/datastore/v1beta2/datasets/{datasetId}/lookup',
            'method': 'POST',
            'resultType': 'LookupResponse',
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
                'keys': keys,
                'readOptions': {
                    'transaction': transaction,
                    'readConsistency': readConsistency,
                },
            },
        }
        return self._request(queryParams)

    def commit(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ignoreReadOnly=None, transaction=None, mode=None, insert=None, force=None, insertAutoId=None, update=None, delete=None, upsert=None):
        '''Commit a transaction, optionally creating, deleting or modifying some entities.'''
        queryParams = {
            'url': 'https://www.googleapis.com/datastore/v1beta2/datasets/{datasetId}/commit',
            'method': 'POST',
            'resultType': 'CommitResponse',
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
                'ignoreReadOnly': ignoreReadOnly,
                'transaction': transaction,
                'mode': mode,
                'mutation': {
                    'insert': insert,
                    'force': force,
                    'insertAutoId': insertAutoId,
                    'update': update,
                    'delete': delete,
                    'upsert': upsert,
                },
            },
        }
        return self._request(queryParams)

    def runQuery(self, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, startCursor=None, kinds=None, projection=None, groupBy=None, operator=None, filters=None, operator_=None, name=None, properties=None, path=None, namespace=None, key_partitionId_datasetId=None, doubleValue=None, blobKeyValue=None, meaning=None, dateTimeValue=None, path_=None, partitionId_namespace=None, partitionId_datasetId=None, blobValue=None, indexed=None, stringValue=None, listValue=None, booleanValue=None, integerValue=None, limit=None, offset=None, endCursor=None, order=None, namespace_=None, datasetId_=None, allowLiteral=None, nameArgs=None, queryString=None, numberArgs=None, transaction=None, readConsistency=None):
        '''Query for entities.'''
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
                    'filter': {
                        'compositeFilter': {
                            'operator': operator,
                            'filters': filters,
                        },
                        'propertyFilter': {
                            'operator': operator_,
                            'property': {
                                'name': name,
                            },
                            'value': {
                                'entityValue': {
                                    'properties': properties,
                                    'key': {
                                        'path': path,
                                        'partitionId': {
                                            'namespace': namespace,
                                            'datasetId': key_partitionId_datasetId,
                                        },
                                    },
                                },
                                'doubleValue': doubleValue,
                                'integerValue': integerValue,
                                'meaning': meaning,
                                'dateTimeValue': dateTimeValue,
                                'keyValue': {
                                    'path': path_,
                                    'partitionId': {
                                        'namespace': partitionId_namespace,
                                        'datasetId': partitionId_datasetId,
                                    },
                                },
                                'stringValue': stringValue,
                                'indexed': indexed,
                                'blobValue': blobValue,
                                'listValue': listValue,
                                'booleanValue': booleanValue,
                                'blobKeyValue': blobKeyValue,
                            },
                        },
                    },
                    'limit': limit,
                    'offset': offset,
                    'endCursor': endCursor,
                    'groupBy': groupBy,
                },
                'partitionId': {
                    'namespace': namespace_,
                    'datasetId': datasetId_,
                },
                'gqlQuery': {
                    'queryString': queryString,
                    'nameArgs': nameArgs,
                    'allowLiteral': allowLiteral,
                    'numberArgs': numberArgs,
                },
                'readOptions': {
                    'transaction': transaction,
                    'readConsistency': readConsistency,
                },
            },
        }
        return self._request(queryParams)


class Datastore(Service):
    '''API for accessing Google Cloud Datastore.'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/userinfo.email', u'https://www.googleapis.com/auth/datastore', u'https://www.googleapis.com/auth/cloud-platform']

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Datastore, self).__init__(conn, *args, **kwargs)
        self.datasets = Datasets(self, conn, *args, **kwargs)
