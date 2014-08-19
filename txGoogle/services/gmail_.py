from txGoogle.utils import leaveOutNulls

class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'empty',
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

class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Directly inserts a message into only this user's mailbox. Does not send a message.'''
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
        '''Removes the specified message from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/untrash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        '''Gets the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Lists the messages in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Modifies the labels on the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify',
            'method': 'POST',
            'resultType': 'ModifyMessageRequest',
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
        '''Directly imports a message into only this user's mailbox, similar to receiving via SMTP. Does not send a message.'''
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
        '''Moves the specified message to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/trash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Gets the specified label.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
                'userId': userId,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Lists all labels in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels',
            'method': 'GET',
            'resultType': 'empty',
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

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def patch(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Removes the specified thread from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/untrash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Lists the threads in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Modifies the labels applied to the thread. This applies to all messages in the thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/modify',
            'method': 'POST',
            'resultType': 'ModifyThreadRequest',
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
        '''Moves the specified thread to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/trash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Gets the specified draft.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'method': 'GET',
            'resultType': 'empty',
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

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        '''Lists the drafts in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts',
            'method': 'GET',
            'resultType': 'empty',
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

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, message_id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
        '''Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/send',
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/history',
            'method': 'GET',
            'resultType': 'empty',
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

class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'empty',
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

class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Directly inserts a message into only this user's mailbox. Does not send a message.'''
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
        '''Removes the specified message from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/untrash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        '''Gets the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Lists the messages in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Modifies the labels on the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify',
            'method': 'POST',
            'resultType': 'ModifyMessageRequest',
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
        '''Directly imports a message into only this user's mailbox, similar to receiving via SMTP. Does not send a message.'''
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
        '''Moves the specified message to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/trash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Gets the specified label.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
                'userId': userId,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Lists all labels in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels',
            'method': 'GET',
            'resultType': 'empty',
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

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def patch(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Removes the specified thread from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/untrash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Lists the threads in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Modifies the labels applied to the thread. This applies to all messages in the thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/modify',
            'method': 'POST',
            'resultType': 'ModifyThreadRequest',
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
        '''Moves the specified thread to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/trash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Gets the specified draft.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'method': 'GET',
            'resultType': 'empty',
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

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        '''Lists the drafts in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts',
            'method': 'GET',
            'resultType': 'empty',
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

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, message_id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
        '''Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/send',
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/history',
            'method': 'GET',
            'resultType': 'empty',
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

class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'empty',
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

class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Directly inserts a message into only this user's mailbox. Does not send a message.'''
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
        '''Removes the specified message from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/untrash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        '''Gets the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Lists the messages in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Modifies the labels on the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify',
            'method': 'POST',
            'resultType': 'ModifyMessageRequest',
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
        '''Directly imports a message into only this user's mailbox, similar to receiving via SMTP. Does not send a message.'''
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
        '''Moves the specified message to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/trash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Gets the specified label.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
                'userId': userId,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Lists all labels in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels',
            'method': 'GET',
            'resultType': 'empty',
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

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def patch(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Removes the specified thread from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/untrash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Lists the threads in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Modifies the labels applied to the thread. This applies to all messages in the thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/modify',
            'method': 'POST',
            'resultType': 'ModifyThreadRequest',
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
        '''Moves the specified thread to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/trash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Gets the specified draft.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'method': 'GET',
            'resultType': 'empty',
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

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        '''Lists the drafts in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts',
            'method': 'GET',
            'resultType': 'empty',
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

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, message_id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
        '''Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/send',
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/history',
            'method': 'GET',
            'resultType': 'empty',
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

class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'empty',
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

class Attachments():
    def __init__(self, conn):
        self._conn = conn

    def get(self, userId, id, messageId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified message attachment.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Directly inserts a message into only this user's mailbox. Does not send a message.'''
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
        '''Removes the specified message from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/untrash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        '''Gets the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Lists the messages in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Modifies the labels on the specified message.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify',
            'method': 'POST',
            'resultType': 'ModifyMessageRequest',
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
        '''Directly imports a message into only this user's mailbox, similar to receiving via SMTP. Does not send a message.'''
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
        '''Moves the specified message to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/trash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Gets the specified label.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
                'userId': userId,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Lists all labels in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/labels',
            'method': 'GET',
            'resultType': 'empty',
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

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def patch(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, labelListVisibility=None, type=None, id=None, name=None):
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
                'type': type,
                'messageListVisibility': messageListVisibility,
                'labelListVisibility': labelListVisibility,
                'name': name,
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Removes the specified thread from the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/untrash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Lists the threads in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads',
            'method': 'GET',
            'resultType': 'empty',
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
        '''Modifies the labels applied to the thread. This applies to all messages in the thread.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/modify',
            'method': 'POST',
            'resultType': 'ModifyThreadRequest',
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
        '''Moves the specified thread to the trash.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/trash',
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
                'userId': userId,
                'id': id,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Gets the specified draft.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}',
            'method': 'GET',
            'resultType': 'empty',
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

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        '''Lists the drafts in the user's mailbox.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts',
            'method': 'GET',
            'resultType': 'empty',
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

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, message_id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, historyId=None, id=None, snippet=None, raw=None, sizeEstimate=None, threadId=None, labelIds=None, attachmentId=None, data=None, size=None, mimeType=None, partId=None, filename=None, headers=None, parts=None, id=None):
        '''Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/drafts/send',
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
                'id': id,
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

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
        '''Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).'''
        queryParams = {
            'url': 'https://www.googleapis.com/gmail/v1/users/{userId}/history',
            'method': 'GET',
            'resultType': 'empty',
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
    '''The Gmail REST API.'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/gmail.compose', u'https://mail.google.com/', u'https://www.googleapis.com/auth/gmail.modify', u'https://www.googleapis.com/auth/gmail.readonly']
    
    def __init__(self, conn=None, scopes=None):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        self.users = Users(conn)
