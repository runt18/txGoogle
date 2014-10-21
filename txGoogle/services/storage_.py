from txGoogle.service import Service
from urllib import quote as urlibQuoteEncode
from txGoogle.resource import Resource


class DefaultObjectAccessControls(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(DefaultObjectAccessControls, self).__init__(service, conn, *args, **kwargs)

    def insert(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, domain=None, generation=None, object=None, kind=None, entity=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Creates a new default object ACL entry on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/defaultObjectAcl',
            'method': 'POST',
            'resultType': 'ObjectAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'generation': generation,
                'object': object,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def get(self, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Returns the default object ACL entry for the specified entity on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/defaultObjectAcl/{entity}',
            'method': 'GET',
            'resultType': 'ObjectAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None):
        '''Retrieves default object ACL entries on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/defaultObjectAcl',
            'method': 'GET',
            'resultType': 'ObjectAccessControls',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, domain=None, generation=None, object=None, kind=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Updates a default object ACL entry on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/defaultObjectAcl/{entity}',
            'method': 'PUT',
            'resultType': 'ObjectAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'generation': generation,
                'object': object,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def patch(self, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, domain=None, generation=None, object=None, kind=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Updates a default object ACL entry on the specified bucket. This method supports patch semantics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/defaultObjectAcl/{entity}',
            'method': 'PATCH',
            'resultType': 'ObjectAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'generation': generation,
                'object': object,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def delete(self, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Permanently deletes the default object ACL entry for the specified entity on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/defaultObjectAcl/{entity}',
            'method': 'DELETE',
            'resultType': 'empty',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class BucketAccessControls(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(BucketAccessControls, self).__init__(service, conn, *args, **kwargs)

    def insert(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, domain=None, kind=None, entity=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Creates a new ACL entry on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/acl',
            'method': 'POST',
            'resultType': 'BucketAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def get(self, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Returns the ACL entry for the specified entity on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/acl/{entity}',
            'method': 'GET',
            'resultType': 'BucketAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Retrieves ACL entries on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/acl',
            'method': 'GET',
            'resultType': 'BucketAccessControls',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, domain=None, kind=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Updates an ACL entry on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/acl/{entity}',
            'method': 'PUT',
            'resultType': 'BucketAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def patch(self, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, domain=None, kind=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Updates an ACL entry on the specified bucket. This method supports patch semantics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/acl/{entity}',
            'method': 'PATCH',
            'resultType': 'BucketAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def delete(self, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Permanently deletes the ACL entry for the specified entity on the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/acl/{entity}',
            'method': 'DELETE',
            'resultType': 'empty',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Channels(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Channels, self).__init__(service, conn, *args, **kwargs)

    def stop(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, resourceUri=None, kind=None, resourceId=None, id=None, token=None, params=None, expiration=None, address=None, type=None, payload=None):
        '''Stop watching resources through this channel'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/channels/stop',
            'method': 'POST',
            'resultType': 'empty',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
            },
            'httpBodyParams': {
                'resourceUri': resourceUri,
                'kind': kind,
                'resourceId': resourceId,
                'payload': payload,
                'token': token,
                'params': params,
                'expiration': expiration,
                'address': address,
                'type': type,
                'id': id,
            },
        }
        return self._request(queryParams)


class Objects(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Objects, self).__init__(service, conn, *args, **kwargs)

    def insert(self, bucket, name, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifGenerationMatch=None, projection=None, ifMetagenerationMatch=None, contentEncoding=None, predefinedAcl=None, ifMetagenerationNotMatch=None, ifGenerationNotMatch=None, selfLink=None, generation=None, componentCount=None, mediaLink=None, owner=None, cacheControl=None, acl=None, id=None, size=None, timeDeleted=None, md5Hash=None, crc32c=None, etag=None, metadata=None, updated=None, contentType=None, contentLanguage=None, metageneration=None, kind=None, storageClass=None, contentDisposition=None):
        '''Stores a new object and metadata.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o',
            'method': 'POST',
            'resultType': 'Object',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifGenerationMatch': ifGenerationMatch,
                'projection': projection,
                'name': name,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'contentEncoding': contentEncoding,
                'predefinedAcl': predefinedAcl,
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
                'ifGenerationNotMatch': ifGenerationNotMatch,
            },
            'httpBodyParams': {
                'generation': generation,
                'componentCount': componentCount,
                'mediaLink': mediaLink,
                'owner': owner,
                'cacheControl': cacheControl,
                'acl': acl,
                'id': id,
                'size': size,
                'timeDeleted': timeDeleted,
                'md5Hash': md5Hash,
                'crc32c': crc32c,
                'etag': etag,
                'metadata': metadata,
                'updated': updated,
                'contentType': contentType,
                'contentDisposition': contentDisposition,
                'contentLanguage': contentLanguage,
                'metageneration': metageneration,
                'kind': kind,
                'name': name,
                'bucket': bucket,
                'contentEncoding': contentEncoding,
                'storageClass': storageClass,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def watchAll(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, projection=None, versions=None, delimiter=None, maxResults=None, pageToken=None, prefix=None, resourceUri=None, kind=None, resourceId=None, id=None, token=None, params=None, expiration=None, address=None, type=None, payload=None):
        '''Watch for changes on all objects in a bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/watch',
            'method': 'POST',
            'resultType': 'Channel',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projection': projection,
                'versions': versions,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'delimiter': delimiter,
                'maxResults': maxResults,
                'pageToken': pageToken,
                'prefix': prefix,
            },
            'httpBodyParams': {
                'resourceUri': resourceUri,
                'kind': kind,
                'resourceId': resourceId,
                'payload': payload,
                'token': token,
                'params': params,
                'expiration': expiration,
                'address': address,
                'type': type,
                'id': id,
            },
        }
        return self._request(queryParams)

    def compose(self, destinationBucket, destinationObject, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifMetagenerationMatch=None, ifGenerationMatch=None, destinationPredefinedAcl=None, kind=None, selfLink=None, generation=None, componentCount=None, mediaLink=None, owner=None, cacheControl=None, acl=None, id=None, size=None, timeDeleted=None, md5Hash=None, crc32c=None, etag=None, metadata=None, updated=None, contentType=None, contentLanguage=None, metageneration=None, destination_kind=None, name=None, bucket=None, contentEncoding=None, storageClass=None, contentDisposition=None, sourceObjects=None):
        '''Concatenates a list of existing objects into a new object in the same bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{destinationBucket}/o/{destinationObject}/compose',
            'method': 'POST',
            'resultType': 'Object',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'destinationBucket': urlibQuoteEncode(destinationBucket, safe=''),
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'ifGenerationMatch': ifGenerationMatch,
                'destinationObject': urlibQuoteEncode(destinationObject, safe=''),
                'destinationPredefinedAcl': destinationPredefinedAcl,
            },
            'httpBodyParams': {
                'kind': kind,
                'destination': {
                    'generation': generation,
                    'componentCount': componentCount,
                    'mediaLink': mediaLink,
                    'owner': owner,
                    'cacheControl': cacheControl,
                    'acl': acl,
                    'id': id,
                    'size': size,
                    'timeDeleted': timeDeleted,
                    'md5Hash': md5Hash,
                    'crc32c': crc32c,
                    'etag': etag,
                    'metadata': metadata,
                    'updated': updated,
                    'contentType': contentType,
                    'contentDisposition': contentDisposition,
                    'contentLanguage': contentLanguage,
                    'metageneration': metageneration,
                    'kind': destination_kind,
                    'name': name,
                    'bucket': bucket,
                    'contentEncoding': contentEncoding,
                    'storageClass': storageClass,
                    'selfLink': selfLink,
                },
                'sourceObjects': sourceObjects,
            },
        }
        return self._request(queryParams)

    def get(self, object, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifGenerationNotMatch=None, generation=None, ifMetagenerationMatch=None, ifGenerationMatch=None, ifMetagenerationNotMatch=None, projection=None):
        '''Retrieves objects or their metadata.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}',
            'method': 'GET',
            'resultType': 'Object',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifGenerationNotMatch': ifGenerationNotMatch,
                'generation': generation,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'ifGenerationMatch': ifGenerationMatch,
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
                'projection': projection,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, projection=None, versions=None, delimiter=None, maxResults=None, pageToken=None, prefix=None):
        '''Retrieves a list of objects matching the criteria.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o',
            'method': 'GET',
            'resultType': 'Objects',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projection': projection,
                'versions': versions,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'delimiter': delimiter,
                'maxResults': maxResults,
                'pageToken': pageToken,
                'prefix': prefix,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, object, bucket, name, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifGenerationMatch=None, ifGenerationNotMatch=None, generation=None, ifMetagenerationMatch=None, predefinedAcl=None, ifMetagenerationNotMatch=None, projection=None, selfLink=None, componentCount=None, mediaLink=None, owner=None, cacheControl=None, acl=None, id=None, size=None, timeDeleted=None, md5Hash=None, crc32c=None, etag=None, metadata=None, updated=None, contentType=None, contentLanguage=None, metageneration=None, kind=None, contentEncoding=None, storageClass=None, contentDisposition=None):
        '''Updates an object's metadata.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}',
            'method': 'PUT',
            'resultType': 'Object',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifGenerationMatch': ifGenerationMatch,
                'ifGenerationNotMatch': ifGenerationNotMatch,
                'generation': generation,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'predefinedAcl': predefinedAcl,
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
                'projection': projection,
            },
            'httpBodyParams': {
                'generation': generation,
                'componentCount': componentCount,
                'mediaLink': mediaLink,
                'owner': owner,
                'cacheControl': cacheControl,
                'acl': acl,
                'id': id,
                'size': size,
                'timeDeleted': timeDeleted,
                'md5Hash': md5Hash,
                'crc32c': crc32c,
                'etag': etag,
                'metadata': metadata,
                'updated': updated,
                'contentType': contentType,
                'contentDisposition': contentDisposition,
                'contentLanguage': contentLanguage,
                'metageneration': metageneration,
                'kind': kind,
                'name': name,
                'bucket': bucket,
                'contentEncoding': contentEncoding,
                'storageClass': storageClass,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def patch(self, object, bucket, name, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifGenerationMatch=None, ifGenerationNotMatch=None, generation=None, ifMetagenerationMatch=None, predefinedAcl=None, ifMetagenerationNotMatch=None, projection=None, selfLink=None, componentCount=None, mediaLink=None, owner=None, cacheControl=None, acl=None, id=None, size=None, timeDeleted=None, md5Hash=None, crc32c=None, etag=None, metadata=None, updated=None, contentType=None, contentLanguage=None, metageneration=None, kind=None, contentEncoding=None, storageClass=None, contentDisposition=None):
        '''Updates an object's metadata. This method supports patch semantics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}',
            'method': 'PATCH',
            'resultType': 'Object',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifGenerationMatch': ifGenerationMatch,
                'ifGenerationNotMatch': ifGenerationNotMatch,
                'generation': generation,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'predefinedAcl': predefinedAcl,
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
                'projection': projection,
            },
            'httpBodyParams': {
                'generation': generation,
                'componentCount': componentCount,
                'mediaLink': mediaLink,
                'owner': owner,
                'cacheControl': cacheControl,
                'acl': acl,
                'id': id,
                'size': size,
                'timeDeleted': timeDeleted,
                'md5Hash': md5Hash,
                'crc32c': crc32c,
                'etag': etag,
                'metadata': metadata,
                'updated': updated,
                'contentType': contentType,
                'contentDisposition': contentDisposition,
                'contentLanguage': contentLanguage,
                'metageneration': metageneration,
                'kind': kind,
                'name': name,
                'bucket': bucket,
                'contentEncoding': contentEncoding,
                'storageClass': storageClass,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def copy(self, sourceObject, sourceBucket, destinationBucket, destinationObject, name, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifSourceGenerationMatch=None, ifGenerationMatch=None, ifGenerationNotMatch=None, ifSourceMetagenerationNotMatch=None, ifMetagenerationMatch=None, sourceGeneration=None, destinationPredefinedAcl=None, ifSourceGenerationNotMatch=None, ifSourceMetagenerationMatch=None, ifMetagenerationNotMatch=None, projection=None, selfLink=None, generation=None, componentCount=None, mediaLink=None, owner=None, cacheControl=None, acl=None, id=None, size=None, timeDeleted=None, md5Hash=None, crc32c=None, etag=None, metadata=None, updated=None, contentType=None, contentLanguage=None, metageneration=None, kind=None, bucket=None, contentEncoding=None, storageClass=None, contentDisposition=None):
        '''Copies an object to a specified location. Optionally overrides metadata.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{sourceBucket}/o/{sourceObject}/copyTo/b/{destinationBucket}/o/{destinationObject}',
            'method': 'POST',
            'resultType': 'Object',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifSourceGenerationMatch': ifSourceGenerationMatch,
                'sourceObject': urlibQuoteEncode(sourceObject, safe=''),
                'ifGenerationMatch': ifGenerationMatch,
                'ifGenerationNotMatch': ifGenerationNotMatch,
                'ifSourceMetagenerationNotMatch': ifSourceMetagenerationNotMatch,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'sourceGeneration': sourceGeneration,
                'destinationPredefinedAcl': destinationPredefinedAcl,
                'ifSourceGenerationNotMatch': ifSourceGenerationNotMatch,
                'sourceBucket': urlibQuoteEncode(sourceBucket, safe=''),
                'ifSourceMetagenerationMatch': ifSourceMetagenerationMatch,
                'destinationBucket': urlibQuoteEncode(destinationBucket, safe=''),
                'destinationObject': urlibQuoteEncode(destinationObject, safe=''),
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
                'projection': projection,
            },
            'httpBodyParams': {
                'generation': generation,
                'componentCount': componentCount,
                'mediaLink': mediaLink,
                'owner': owner,
                'cacheControl': cacheControl,
                'acl': acl,
                'id': id,
                'size': size,
                'timeDeleted': timeDeleted,
                'md5Hash': md5Hash,
                'crc32c': crc32c,
                'etag': etag,
                'metadata': metadata,
                'updated': updated,
                'contentType': contentType,
                'contentDisposition': contentDisposition,
                'contentLanguage': contentLanguage,
                'metageneration': metageneration,
                'kind': kind,
                'name': name,
                'bucket': bucket,
                'contentEncoding': contentEncoding,
                'storageClass': storageClass,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def delete(self, object, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifGenerationNotMatch=None, generation=None, ifMetagenerationMatch=None, ifGenerationMatch=None, ifMetagenerationNotMatch=None):
        '''Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}',
            'method': 'DELETE',
            'resultType': 'empty',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifGenerationNotMatch': ifGenerationNotMatch,
                'generation': generation,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'ifGenerationMatch': ifGenerationMatch,
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class ObjectAccessControls(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(ObjectAccessControls, self).__init__(service, conn, *args, **kwargs)

    def insert(self, object, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, generation=None, domain=None, kind=None, entity=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Creates a new ACL entry on the specified object.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}/acl',
            'method': 'POST',
            'resultType': 'ObjectAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'generation': generation,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'generation': generation,
                'object': object,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def get(self, object, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, generation=None):
        '''Returns the ACL entry for the specified entity on the specified object.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}/acl/{entity}',
            'method': 'GET',
            'resultType': 'ObjectAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'generation': generation,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, object, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, generation=None):
        '''Retrieves ACL entries on the specified object.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}/acl',
            'method': 'GET',
            'resultType': 'ObjectAccessControls',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'generation': generation,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, object, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, generation=None, domain=None, kind=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Updates an ACL entry on the specified object.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}/acl/{entity}',
            'method': 'PUT',
            'resultType': 'ObjectAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'generation': generation,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'generation': generation,
                'object': object,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def patch(self, object, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, generation=None, domain=None, kind=None, email=None, etag=None, role=None, entityId=None, projectTeam=None, id=None, selfLink=None):
        '''Updates an ACL entry on the specified object. This method supports patch semantics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}/acl/{entity}',
            'method': 'PATCH',
            'resultType': 'ObjectAccessControl',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'generation': generation,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
                'domain': domain,
                'generation': generation,
                'object': object,
                'bucket': bucket,
                'kind': kind,
                'entity': entity,
                'etag': etag,
                'role': role,
                'id': id,
                'entityId': entityId,
                'projectTeam': projectTeam,
                'email': email,
                'selfLink': selfLink,
            },
        }
        return self._request(queryParams)

    def delete(self, object, bucket, entity, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, generation=None):
        '''Permanently deletes the ACL entry for the specified entity on the specified object.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}/o/{object}/acl/{entity}',
            'method': 'DELETE',
            'resultType': 'empty',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'generation': generation,
                'object': urlibQuoteEncode(object, safe=''),
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'entity': urlibQuoteEncode(entity, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Buckets(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Buckets, self).__init__(service, conn, *args, **kwargs)

    def insert(self, project, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, predefinedAcl=None, projection=None, website=None, kind=None, logging=None, name=None, timeCreated=None, id=None, storageClass=None, projectNumber=None, acl=None, defaultObjectAcl=None, metageneration=None, versioning=None, cors=None, owner=None, etag=None, lifecycle=None, selfLink=None, location=None):
        '''Creates a new bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b',
            'method': 'POST',
            'resultType': 'Bucket',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': project,
                'predefinedAcl': predefinedAcl,
                'projection': projection,
            },
            'httpBodyParams': {
                'website': website,
                'selfLink': selfLink,
                'kind': kind,
                'logging': logging,
                'name': name,
                'timeCreated': timeCreated,
                'lifecycle': lifecycle,
                'projectNumber': projectNumber,
                'defaultObjectAcl': defaultObjectAcl,
                'metageneration': metageneration,
                'storageClass': storageClass,
                'cors': cors,
                'owner': owner,
                'etag': etag,
                'acl': acl,
                'id': id,
                'versioning': versioning,
                'location': location,
            },
        }
        return self._request(queryParams)

    def get(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, projection=None):
        '''Returns metadata for the specified bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}',
            'method': 'GET',
            'resultType': 'Bucket',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
                'projection': projection,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, project, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, projection=None, maxResults=None):
        '''Retrieves a list of buckets for a given project.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b',
            'method': 'GET',
            'resultType': 'Buckets',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': project,
                'pageToken': pageToken,
                'projection': projection,
                'maxResults': maxResults,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifMetagenerationMatch=None, predefinedAcl=None, ifMetagenerationNotMatch=None, projection=None, website=None, kind=None, logging=None, name=None, timeCreated=None, id=None, storageClass=None, projectNumber=None, acl=None, defaultObjectAcl=None, metageneration=None, versioning=None, cors=None, owner=None, etag=None, lifecycle=None, selfLink=None, location=None):
        '''Updates a bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}',
            'method': 'PUT',
            'resultType': 'Bucket',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'predefinedAcl': predefinedAcl,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
                'projection': projection,
            },
            'httpBodyParams': {
                'website': website,
                'selfLink': selfLink,
                'kind': kind,
                'logging': logging,
                'name': name,
                'timeCreated': timeCreated,
                'lifecycle': lifecycle,
                'projectNumber': projectNumber,
                'defaultObjectAcl': defaultObjectAcl,
                'metageneration': metageneration,
                'storageClass': storageClass,
                'cors': cors,
                'owner': owner,
                'etag': etag,
                'acl': acl,
                'id': id,
                'versioning': versioning,
                'location': location,
            },
        }
        return self._request(queryParams)

    def patch(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifMetagenerationMatch=None, predefinedAcl=None, ifMetagenerationNotMatch=None, projection=None, website=None, kind=None, logging=None, name=None, timeCreated=None, id=None, storageClass=None, projectNumber=None, acl=None, defaultObjectAcl=None, metageneration=None, versioning=None, cors=None, owner=None, etag=None, lifecycle=None, selfLink=None, location=None):
        '''Updates a bucket. This method supports patch semantics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}',
            'method': 'PATCH',
            'resultType': 'Bucket',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'predefinedAcl': predefinedAcl,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
                'projection': projection,
            },
            'httpBodyParams': {
                'website': website,
                'selfLink': selfLink,
                'kind': kind,
                'logging': logging,
                'name': name,
                'timeCreated': timeCreated,
                'lifecycle': lifecycle,
                'projectNumber': projectNumber,
                'defaultObjectAcl': defaultObjectAcl,
                'metageneration': metageneration,
                'storageClass': storageClass,
                'cors': cors,
                'owner': owner,
                'etag': etag,
                'acl': acl,
                'id': id,
                'versioning': versioning,
                'location': location,
            },
        }
        return self._request(queryParams)

    def delete(self, bucket, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None):
        '''Permanently deletes an empty bucket.'''
        queryParams = {
            'url': 'https://www.googleapis.com/storage/v1/b/{bucket}',
            'method': 'DELETE',
            'resultType': 'empty',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'ifMetagenerationMatch': ifMetagenerationMatch,
                'bucket': urlibQuoteEncode(bucket, safe=''),
                'ifMetagenerationNotMatch': ifMetagenerationNotMatch,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Storage(Service):
    '''Lets you store and retrieve potentially-large, immutable data objects.'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/devstorage.read_only', u'https://www.googleapis.com/auth/devstorage.read_write', u'https://www.googleapis.com/auth/devstorage.full_control']

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Storage, self).__init__(conn, *args, **kwargs)
        self.defaultObjectAccessControls = DefaultObjectAccessControls(self, conn, *args, **kwargs)
        self.bucketAccessControls = BucketAccessControls(self, conn, *args, **kwargs)
        self.channels = Channels(self, conn, *args, **kwargs)
        self.objects = Objects(self, conn, *args, **kwargs)
        self.objectAccessControls = ObjectAccessControls(self, conn, *args, **kwargs)
        self.buckets = Buckets(self, conn, *args, **kwargs)
