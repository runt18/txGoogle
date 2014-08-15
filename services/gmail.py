from txGoogle.asyncUtils import leaveOutNulls


class Threads(object):
    def __init__(self, connection, *args, **kwargs):
        self._conn = connection

    def untrash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Removes the specified thread from the trash."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/untrash",
            "userId": userId,
            "id": id,
            "resultType": "Thread",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Gets the specified thread."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}",
            "userId": userId,
            "id": id,
            "resultType": "Thread",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, maxResults=None, q=None, pageToken=None, includeSpamTrash=None, labelIds=None):
        "Lists the threads in the user's mailbox."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "q": q,
                "prettyPrint": prettyPrint,
                "labelIds": labelIds,
                "fields": fields,
                "maxResults": maxResults,
                "quotaUser": quotaUser,
                "pageToken": pageToken,
                "oauth_token": oauth_token,
                "key": key,
                "includeSpamTrash": includeSpamTrash,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/threads",
            "userId": userId,
            "resultType": "multi",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def modify(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, addLabelIds=None, removeLabelIds=None):
        "Modifies the labels applied to the thread. This applies to all messages in the thread."
        queryParams = {
            "httpBodyParams": {
                "addLabelIds": addLabelIds,
                "removeLabelIds": removeLabelIds
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/modify",
            "userId": userId,
            "id": id,
            "resultType": "Thread",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def trash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Moves the specified thread to the trash."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}/trash",
            "userId": userId,
            "id": id,
            "resultType": "Thread",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Immediately and permanently deletes the specified thread. This operation cannot be undone. Prefer threads.trash instead."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/threads/{id}",
            "userId": userId,
            "id": id,
            "resultType": "empty",
            "method": "DELETE"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))


class Labels(object):
    def __init__(self, connection, *args, **kwargs):
        self._conn = connection

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Gets the specified label."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}",
            "userId": userId,
            "id": id,
            "resultType": "Label",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, id=None, messageListVisibility=None, type=None, labelListVisibility=None, name=None):
        "Creates a new label."
        queryParams = {
            "httpBodyParams": {
                "id": id,
                "messageListVisibility": messageListVisibility,
                "type": type,
                "labelListVisibility": labelListVisibility,
                "name": name
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/labels",
            "userId": userId,
            "resultType": "Label",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Lists all labels in the user's mailbox."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/labels",
            "userId": userId,
            "resultType": "ListLabelsResponse",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, type=None, labelListVisibility=None, name=None):
        "Updates the specified label."
        queryParams = {
            "httpBodyParams": {
                "id": id,
                "messageListVisibility": messageListVisibility,
                "type": type,
                "labelListVisibility": labelListVisibility,
                "name": name
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}",
            "userId": userId,
            "id": id,
            "resultType": "Label",
            "method": "PUT"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def patch(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, messageListVisibility=None, type=None, labelListVisibility=None, name=None):
        "Updates the specified label. This method supports patch semantics."
        queryParams = {
            "httpBodyParams": {
                "id": id,
                "messageListVisibility": messageListVisibility,
                "type": type,
                "labelListVisibility": labelListVisibility,
                "name": name
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}",
            "userId": userId,
            "id": id,
            "resultType": "Label",
            "method": "PATCH"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/labels/{id}",
            "userId": userId,
            "id": id,
            "resultType": "empty",
            "method": "DELETE"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))


class Messages(object):
    def __init__(self, connection, *args, **kwargs):
        self._conn = connection

    def insert(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, mimeType=None, partId=None, raw=None, historyId=None, filename=None, snippet=None, headers=None, parts=None, attachmentId=None, sizeEstimate=None, threadId=None, labelIds=None, data=None, id=None, size=None):
        "Directly inserts a message into only this user's mailbox. Does not send a message."
        queryParams = {
            "httpBodyParams": {
                "historyId": historyId,
                "id": id,
                "snippet": snippet,
                "raw": raw,
                "sizeEstimate": sizeEstimate,
                "threadId": threadId,
                "labelIds": labelIds,
                "payload": {
                    "body": {
                        "attachmentId": attachmentId,
                        "data": data,
                        "size": size
                    },
                    "mimeType": mimeType,
                    "partId": partId,
                    "filename": filename,
                    "headers": headers,
                    "parts": parts
                }
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages",
            "userId": userId,
            "resultType": "Message",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def untrash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Removes the specified message from the trash."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/untrash",
            "userId": userId,
            "id": id,
            "resultType": "Message",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        "Gets the specified message."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "format": format,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}",
            "userId": userId,
            "id": id,
            "resultType": "Message",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, maxResults=None, q=None, pageToken=None, includeSpamTrash=None, labelIds=None):
        "Lists the messages in the user's mailbox."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "q": q,
                "prettyPrint": prettyPrint,
                "labelIds": labelIds,
                "fields": fields,
                "maxResults": maxResults,
                "quotaUser": quotaUser,
                "pageToken": pageToken,
                "oauth_token": oauth_token,
                "key": key,
                "includeSpamTrash": includeSpamTrash,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages",
            "userId": userId,
            "resultType": "multi",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def modify(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, addLabelIds=None, removeLabelIds=None):
        "Modifies the labels on the specified message."
        queryParams = {
            "httpBodyParams": {
                "addLabelIds": addLabelIds,
                "removeLabelIds": removeLabelIds
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify",
            "userId": userId,
            "id": id,
            "resultType": "Message",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, mimeType=None, partId=None, raw=None, historyId=None, filename=None, snippet=None, headers=None, parts=None, attachmentId=None, sizeEstimate=None, threadId=None, labelIds=None, data=None, id=None, size=None):
        "Sends the specified message to the recipients in the To, Cc, and Bcc headers."
        queryParams = {
            "httpBodyParams": {
                "historyId": historyId,
                "id": id,
                "snippet": snippet,
                "raw": raw,
                "sizeEstimate": sizeEstimate,
                "threadId": threadId,
                "labelIds": labelIds,
                "payload": {
                    "body": {
                        "attachmentId": attachmentId,
                        "data": data,
                        "size": size
                    },
                    "mimeType": mimeType,
                    "partId": partId,
                    "filename": filename,
                    "headers": headers,
                    "parts": parts
                }
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages/send",
            "userId": userId,
            "resultType": "Message",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def importMessage(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, mimeType=None, partId=None, raw=None, historyId=None, filename=None, snippet=None, headers=None, parts=None, attachmentId=None, sizeEstimate=None, threadId=None, labelIds=None, data=None, id=None, size=None):
        "Directly imports a message into only this user's mailbox, similar to receiving via SMTP. Does not send a message."
        queryParams = {
            "httpBodyParams": {
                "historyId": historyId,
                "id": id,
                "snippet": snippet,
                "raw": raw,
                "sizeEstimate": sizeEstimate,
                "threadId": threadId,
                "labelIds": labelIds,
                "payload": {
                    "body": {
                        "attachmentId": attachmentId,
                        "data": data,
                        "size": size
                    },
                    "mimeType": mimeType,
                    "partId": partId,
                    "filename": filename,
                    "headers": headers,
                    "parts": parts
                }
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages/import",
            "userId": userId,
            "resultType": "Message",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def trash(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Moves the specified message to the trash."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}/trash",
            "userId": userId,
            "id": id,
            "resultType": "Message",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer messages.trash instead."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/messages/{id}",
            "userId": userId,
            "id": id,
            "resultType": "empty",
            "method": "DELETE"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))


class Drafts(object):
    def __init__(self, connection, *args, **kwargs):
        self._conn = connection

    def get(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, format=None):
        "Gets the specified draft."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "format": format,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}",
            "userId": userId,
            "id": id,
            "resultType": "Draft",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def create(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, mimeType=None, partId=None, raw=None, historyId=None, filename=None, snippet=None, headers=None, parts=None, attachmentId=None, sizeEstimate=None, threadId=None, labelIds=None, data=None, id=None, size=None):
        "Creates a new draft with the DRAFT label."
        queryParams = {
            "httpBodyParams": {
                "message": {
                    "historyId": historyId,
                    "id": id,
                    "snippet": snippet,
                    "raw": raw,
                    "sizeEstimate": sizeEstimate,
                    "threadId": threadId,
                    "labelIds": labelIds,
                    "payload": {
                        "body": {
                            "attachmentId": attachmentId,
                            "data": data,
                            "size": size
                        },
                        "mimeType": mimeType,
                        "partId": partId,
                        "filename": filename,
                        "headers": headers,
                        "parts": parts
                    }
                },
                "id": id
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/drafts",
            "userId": userId,
            "resultType": "Draft",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        "Lists the drafts in the user's mailbox."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "maxResults": maxResults,
                "quotaUser": quotaUser,
                "pageToken": pageToken,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/drafts",
            "userId": userId,
            "resultType": "multi",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def update(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, mimeType=None, partId=None, raw=None, historyId=None, filename=None, snippet=None, headers=None, parts=None, attachmentId=None, sizeEstimate=None, threadId=None, labelIds=None, data=None, size=None):
        "Replaces a draft's content."
        queryParams = {
            "httpBodyParams": {
                "message": {
                    "historyId": historyId,
                    "id": id,
                    "snippet": snippet,
                    "raw": raw,
                    "sizeEstimate": sizeEstimate,
                    "threadId": threadId,
                    "labelIds": labelIds,
                    "payload": {
                        "body": {
                            "attachmentId": attachmentId,
                            "data": data,
                            "size": size
                        },
                        "mimeType": mimeType,
                        "partId": partId,
                        "filename": filename,
                        "headers": headers,
                        "parts": parts
                    }
                },
                "id": id
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}",
            "userId": userId,
            "id": id,
            "resultType": "Draft",
            "method": "PUT"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def send(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, mimeType=None, partId=None, raw=None, historyId=None, filename=None, snippet=None, headers=None, parts=None, attachmentId=None, sizeEstimate=None, threadId=None, labelIds=None, data=None, id=None, size=None):
        "Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers."
        queryParams = {
            "httpBodyParams": {
                "message": {
                    "historyId": historyId,
                    "id": id,
                    "snippet": snippet,
                    "raw": raw,
                    "sizeEstimate": sizeEstimate,
                    "threadId": threadId,
                    "labelIds": labelIds,
                    "payload": {
                        "body": {
                            "attachmentId": attachmentId,
                            "data": data,
                            "size": size
                        },
                        "mimeType": mimeType,
                        "partId": partId,
                        "filename": filename,
                        "headers": headers,
                        "parts": parts
                    }
                },
                "id": id
            },
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/drafts/send",
            "userId": userId,
            "resultType": "Message",
            "method": "POST"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def delete(self, userId, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        "Immediately and permanently deletes the specified draft. Does not simply trash it."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "prettyPrint": prettyPrint,
                "fields": fields,
                "quotaUser": quotaUser,
                "oauth_token": oauth_token,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/drafts/{id}",
            "userId": userId,
            "id": id,
            "resultType": "empty",
            "method": "DELETE"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))


class History(object):
    def __init__(self, connection, *args, **kwargs):
        self._conn = connection

    def list(self, userId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None, labelId=None, startHistoryId=None):
        "Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId)."
        queryParams = {
            "httpBodyParams": {},
            "httpUrlParams": {
                "labelId": labelId,
                "prettyPrint": prettyPrint,
                "fields": fields,
                "maxResults": maxResults,
                "quotaUser": quotaUser,
                "pageToken": pageToken,
                "oauth_token": oauth_token,
                "startHistoryId": startHistoryId,
                "key": key,
                "userIp": userIp,
                "alt": alt
            },
            "url": "https://www.googleapis.com/gmail/v1/users/{userId}/history",
            "userId": userId,
            "resultType": "multi",
            "method": "GET"
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))


class Gmail():
    "The Gmail REST API."
    _DEFAULT_SCOPES = ['https://mail.google.com']

    def __init__(self, conn=None, scopes=None):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        self.threads = Threads(conn)
        self.labels = Labels(conn)
        self.messages = Messages(conn)
        self.drafts = Drafts(conn)
        self.history = History(conn)
