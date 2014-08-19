from txGoogle.utils import leaveOutNulls
class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
                'messageId': messageId,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

class Messages():
    def __init__(self, conn):
        self._conn = conn
        self.attachments = Attachments(conn)

    def insert(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
            },
            'httpBodyParams': {
                'historyId': historyId,
                'payload': {
                    'body': {
                        'data': data,
                        'attachmentId': attachmentId,
                        'size': size,
                    },
                    'mimeType': mimeType,
                    'partId': partId,
                    'filename': filename,
                    'headers': headers,
                    'parts': parts,
                },
                'snippet': snippet,
                'raw': raw,
                'sizeEstimate': sizeEstimate,
                'threadId': threadId,
                'labelIds': labelIds,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def untrash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/untrash',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
                'format': format,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, maxResults=None, q=None, pageToken=None, includeSpamTrash=None, labelIds=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'maxResults': maxResults,
                'q': q,
                'pageToken': pageToken,
                'includeSpamTrash': includeSpamTrash,
                'labelIds': labelIds,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def modify(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, addLabelIds=None, removeLabelIds=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'removeLabelIds': removeLabelIds,
                'addLabelIds': addLabelIds,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/send',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
            },
            'httpBodyParams': {
                'historyId': historyId,
                'payload': {
                    'body': {
                        'data': data,
                        'attachmentId': attachmentId,
                        'size': size,
                    },
                    'mimeType': mimeType,
                    'partId': partId,
                    'filename': filename,
                    'headers': headers,
                    'parts': parts,
                },
                'snippet': snippet,
                'raw': raw,
                'sizeEstimate': sizeEstimate,
                'threadId': threadId,
                'labelIds': labelIds,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def import_(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/import',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
            },
            'httpBodyParams': {
                'historyId': historyId,
                'payload': {
                    'body': {
                        'data': data,
                        'attachmentId': attachmentId,
                        'size': size,
                    },
                    'mimeType': mimeType,
                    'partId': partId,
                    'filename': filename,
                    'headers': headers,
                    'parts': parts,
                },
                'snippet': snippet,
                'raw': raw,
                'sizeEstimate': sizeEstimate,
                'threadId': threadId,
                'labelIds': labelIds,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def trash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/trash',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}',
            'httpMethod': 'DELETE',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

class Labels():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, id=None, messageListVisibility=None, type=None, labelListVisibility=None, name=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'id': id,
                'name': name,
                'labelListVisibility': labelListVisibility,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, id_=None, messageListVisibility=None, type=None, labelListVisibility=None, name=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'httpMethod': 'PUT',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'id': id_,
                'name': name,
                'labelListVisibility': labelListVisibility,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def patch(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, id_=None, messageListVisibility=None, type=None, labelListVisibility=None, name=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'httpMethod': 'PATCH',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'id': id_,
                'name': name,
                'labelListVisibility': labelListVisibility,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'httpMethod': 'DELETE',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

class Threads():
    def __init__(self, conn):
        self._conn = conn

    def untrash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/untrash',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, maxResults=None, q=None, pageToken=None, includeSpamTrash=None, labelIds=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'maxResults': maxResults,
                'q': q,
                'pageToken': pageToken,
                'includeSpamTrash': includeSpamTrash,
                'labelIds': labelIds,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def modify(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, addLabelIds=None, removeLabelIds=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/modify',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'removeLabelIds': removeLabelIds,
                'addLabelIds': addLabelIds,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def trash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/trash',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}',
            'httpMethod': 'DELETE',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

class Drafts():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
                'format': format,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id_=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
            },
            'httpBodyParams': {
                'message': {
                    'historyId': historyId,
                    'payload': {
                        'body': {
                            'data': data,
                            'attachmentId': attachmentId,
                            'size': size,
                        },
                        'mimeType': mimeType,
                        'partId': partId,
                        'filename': filename,
                        'headers': headers,
                        'parts': parts,
                    },
                    'snippet': snippet,
                    'raw': raw,
                    'sizeEstimate': sizeEstimate,
                    'threadId': threadId,
                    'labelIds': labelIds,
                    'id': id,
                },
                'id': id_,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'userId': userId,
                'maxResults': maxResults,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, message_id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id_=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'httpMethod': 'PUT',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'message': {
                    'historyId': historyId,
                    'payload': {
                        'body': {
                            'data': data,
                            'attachmentId': attachmentId,
                            'size': size,
                        },
                        'mimeType': mimeType,
                        'partId': partId,
                        'filename': filename,
                        'headers': headers,
                        'parts': parts,
                    },
                    'snippet': snippet,
                    'raw': raw,
                    'sizeEstimate': sizeEstimate,
                    'threadId': threadId,
                    'labelIds': labelIds,
                    'id': message_id,
                },
                'id': id_,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id_=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/send',
            'httpMethod': 'POST',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
            },
            'httpBodyParams': {
                'message': {
                    'historyId': historyId,
                    'payload': {
                        'body': {
                            'data': data,
                            'attachmentId': attachmentId,
                            'size': size,
                        },
                        'mimeType': mimeType,
                        'partId': partId,
                        'filename': filename,
                        'headers': headers,
                        'parts': parts,
                    },
                    'snippet': snippet,
                    'raw': raw,
                    'sizeEstimate': sizeEstimate,
                    'threadId': threadId,
                    'labelIds': labelIds,
                    'id': id,
                },
                'id': id_,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'httpMethod': 'DELETE',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

class History():
    def __init__(self, conn):
        self._conn = conn

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, labelId=None, maxResults=None, startHistoryId=None):
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/history',
            'httpMethod': 'GET',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'userId': userId,
                'labelId': labelId,
                'maxResults': maxResults,
                'startHistoryId': startHistoryId,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

class Users():
    def __init__(self, conn):
        self._conn = conn
        self.messages = Messages(conn)
        self.labels = Labels(conn)
        self.threads = Threads(conn)
        self.drafts = Drafts(conn)
        self.history = History(conn)

class Gmail():
    def __init__(self, conn):
        self._conn = conn
        self.users = Users(conn)
