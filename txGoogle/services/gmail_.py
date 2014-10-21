from txGoogle.service import Service
from urllib import quote as urlibQuoteEncode
from txGoogle.resource import Resource


class Attachments(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Attachments, self).__init__(service, conn, *args, **kwargs)

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'MessagePartBody',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
                'messageId': urlibQuoteEncode(messageId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Messages(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Messages, self).__init__(service, conn, *args, **kwargs)
        self.attachments = Attachments(api, conn)

    def insert(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, internalDateSource=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None):
        '''Directly inserts a message into only this user's mailbox similar to IMAP APPEND, bypassing most scanning and classification. Does not send a message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages',
            'method': 'POST',
            'resultType': 'Message',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'internalDateSource': internalDateSource,
                'userId': urlibQuoteEncode(userId, safe=''),
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
        return self._request(queryParams)

    def untrash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Removes the specified message from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/untrash',
            'method': 'POST',
            'resultType': 'Message',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, metadataHeaders=None, format=None):
        '''Gets the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}',
            'method': 'GET',
            'resultType': 'Message',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'metadataHeaders': metadataHeaders,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
                'format': format,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, maxResults=None, q=None, pageToken=None, includeSpamTrash=None, labelIds=None):
        '''Lists the messages in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages',
            'method': 'GET',
            'resultType': 'ListMessagesResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'maxResults': maxResults,
                'q': q,
                'pageToken': pageToken,
                'includeSpamTrash': includeSpamTrash,
                'labelIds': labelIds,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def modify(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, addLabelIds=None, removeLabelIds=None):
        '''Modifies the labels on the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify',
            'method': 'POST',
            'resultType': 'Message',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
                'removeLabelIds': removeLabelIds,
                'addLabelIds': addLabelIds,
            },
        }
        return self._request(queryParams)

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None):
        '''Sends the specified message to the recipients in the To, Cc, and Bcc headers.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/send',
            'method': 'POST',
            'resultType': 'Message',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
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
        return self._request(queryParams)

    def import_(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, internalDateSource=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None):
        '''Imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. Does not send a message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/import',
            'method': 'POST',
            'resultType': 'Message',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'internalDateSource': internalDateSource,
                'userId': urlibQuoteEncode(userId, safe=''),
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
        return self._request(queryParams)

    def trash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Moves the specified message to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/trash',
            'method': 'POST',
            'resultType': 'Message',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer messages.trash instead.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}',
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
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Labels(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Labels, self).__init__(service, conn, *args, **kwargs)

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified label.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'method': 'GET',
            'resultType': 'Label',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
        '''Creates a new label.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels',
            'method': 'POST',
            'resultType': 'Label',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._request(queryParams)

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Lists all labels in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels',
            'method': 'GET',
            'resultType': 'ListLabelsResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id_=None, name=None):
        '''Updates the specified label.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'method': 'PUT',
            'resultType': 'Label',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id_,
            },
        }
        return self._request(queryParams)

    def patch(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id_=None, name=None):
        '''Updates the specified label. This method supports patch semantics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'method': 'PATCH',
            'resultType': 'Label',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id_,
            },
        }
        return self._request(queryParams)

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
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
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Threads(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Threads, self).__init__(service, conn, *args, **kwargs)

    def untrash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Removes the specified thread from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/untrash',
            'method': 'POST',
            'resultType': 'Thread',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}',
            'method': 'GET',
            'resultType': 'Thread',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, maxResults=None, q=None, pageToken=None, includeSpamTrash=None, labelIds=None):
        '''Lists the threads in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads',
            'method': 'GET',
            'resultType': 'ListThreadsResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'maxResults': maxResults,
                'q': q,
                'pageToken': pageToken,
                'includeSpamTrash': includeSpamTrash,
                'labelIds': labelIds,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def modify(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, addLabelIds=None, removeLabelIds=None):
        '''Modifies the labels applied to the thread. This applies to all messages in the thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/modify',
            'method': 'POST',
            'resultType': 'Thread',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
                'removeLabelIds': removeLabelIds,
                'addLabelIds': addLabelIds,
            },
        }
        return self._request(queryParams)

    def trash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Moves the specified thread to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/trash',
            'method': 'POST',
            'resultType': 'Thread',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Immediately and permanently deletes the specified thread. This operation cannot be undone. Prefer threads.trash instead.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}',
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
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Drafts(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Drafts, self).__init__(service, conn, *args, **kwargs)

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        '''Gets the specified draft.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'method': 'GET',
            'resultType': 'Draft',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
                'format': format,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id_=None):
        '''Creates a new draft with the DRAFT label.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts',
            'method': 'POST',
            'resultType': 'Draft',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
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
        return self._request(queryParams)

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        '''Lists the drafts in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts',
            'method': 'GET',
            'resultType': 'ListDraftsResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'userId': urlibQuoteEncode(userId, safe=''),
                'maxResults': maxResults,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id_=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, updateId=None):
        '''Replaces a draft's content.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'method': 'PUT',
            'resultType': 'Draft',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
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
                    'id': id_,
                },
                'id': updateId,
            },
        }
        return self._request(queryParams)

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id_=None):
        '''Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/send',
            'method': 'POST',
            'resultType': 'Message',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'userId': urlibQuoteEncode(userId, safe=''),
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
        return self._request(queryParams)

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Immediately and permanently deletes the specified draft. Does not simply trash it.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
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
                'userId': urlibQuoteEncode(userId, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class History(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(History, self).__init__(service, conn, *args, **kwargs)

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, labelId=None, maxResults=None, startHistoryId=None):
        '''Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/history',
            'method': 'GET',
            'resultType': 'ListHistoryResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'userId': urlibQuoteEncode(userId, safe=''),
                'labelId': labelId,
                'maxResults': maxResults,
                'startHistoryId': startHistoryId,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Users(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Users, self).__init__(service, conn, *args, **kwargs)
        self.messages = Messages(api, conn)
        self.labels = Labels(api, conn)
        self.threads = Threads(api, conn)
        self.drafts = Drafts(api, conn)
        self.history = History(api, conn)


class Gmail(Service):
    '''The Gmail REST API.'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/gmail.compose', u'https://mail.google.com/', u'https://www.googleapis.com/auth/gmail.modify', u'https://www.googleapis.com/auth/gmail.readonly']

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Gmail, self).__init__(conn, *args, **kwargs)
        self.users = Users(self, conn, *args, **kwargs)
