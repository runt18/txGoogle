from txGoogle.service import Service
from urllib import quote as urlibQuoteEncode
from txGoogle.resource import Resource


class Topics(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Topics, self).__init__(service, conn, *args, **kwargs)

    def create(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, name=None):
        '''Creates the given topic with the given name.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/topics',
            'method': 'POST',
            'resultType': 'Topic',
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
                'name': name,
            },
        }
        return self._request(queryParams)

    def get(self, topic, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the configuration of a topic. Since the topic only has the name attribute, this method is only useful to check the existence of a topic. If other attributes are added in the future, they will be returned here.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/topics/{+topic}',
            'method': 'GET',
            'resultType': 'Topic',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'topic': urlibQuoteEncode(topic, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None, query=None):
        '''Lists matching topics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/topics',
            'method': 'GET',
            'resultType': 'ListTopicsResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'maxResults': maxResults,
                'query': query,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def publish(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, topic=None, data=None, label=None):
        '''Adds a message to the topic. Returns NOT_FOUND if the topic does not exist.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/topics/publish',
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
                'topic': topic,
                'message': {
                    'data': data,
                    'label': label,
                },
            },
        }
        return self._request(queryParams)

    def delete(self, topic, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Deletes the topic with the given name. All subscriptions to this topic are also deleted. Returns NOT_FOUND if the topic does not exist. After a topic is deleted, a new topic may be created with the same name.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/topics/{+topic}',
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
                'topic': urlibQuoteEncode(topic, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Subscriptions(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Subscriptions, self).__init__(service, conn, *args, **kwargs)

    def pull(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, returnImmediately=None, subscription=None):
        '''Pulls a single message from the server. If return_immediately is true, and no messages are available in the subscription, this method returns FAILED_PRECONDITION. The system is free to return an UNAVAILABLE error if no messages are available in a reasonable amount of time (to reduce system load).'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/subscriptions/pull',
            'method': 'POST',
            'resultType': 'PullResponse',
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
                'returnImmediately': returnImmediately,
                'subscription': subscription,
            },
        }
        return self._request(queryParams)

    def get(self, subscription, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the configuration details of a subscription.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/subscriptions/{+subscription}',
            'method': 'GET',
            'resultType': 'Subscription',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'subscription': urlibQuoteEncode(subscription, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None, query=None):
        '''Lists matching subscriptions.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/subscriptions',
            'method': 'GET',
            'resultType': 'ListSubscriptionsResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'maxResults': maxResults,
                'query': query,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def create(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ackDeadlineSeconds=None, topic=None, pushEndpoint=None, name=None):
        '''Creates a subscription on a given topic for a given subscriber. If the subscription already exists, returns ALREADY_EXISTS. If the corresponding topic doesn't exist, returns NOT_FOUND.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/subscriptions',
            'method': 'POST',
            'resultType': 'Subscription',
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
                'ackDeadlineSeconds': ackDeadlineSeconds,
                'topic': topic,
                'pushConfig': {
                    'pushEndpoint': pushEndpoint,
                },
                'name': name,
            },
        }
        return self._request(queryParams)

    def acknowledge(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ackId=None, subscription=None):
        '''Acknowledges a particular received message: the Pub/Sub system can remove the given message from the subscription. Acknowledging a message whose Ack deadline has expired may succeed, but the message could have been already redelivered. Acknowledging a message more than once will not result in an error. This is only used for messages received via pull.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/subscriptions/acknowledge',
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
                'ackId': ackId,
                'subscription': subscription,
            },
        }
        return self._request(queryParams)

    def modifyAckDeadline(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ackDeadlineSeconds=None, ackId=None, subscription=None):
        '''Modifies the Ack deadline for a message received from a pull request.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/subscriptions/modifyAckDeadline',
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
                'ackDeadlineSeconds': ackDeadlineSeconds,
                'ackId': ackId,
                'subscription': subscription,
            },
        }
        return self._request(queryParams)

    def modifyPushConfig(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pushEndpoint=None, subscription=None):
        '''Modifies the PushConfig for a specified subscription. This method can be used to suspend the flow of messages to an end point by clearing the PushConfig field in the request. Messages will be accumulated for delivery even if no push configuration is defined or while the configuration is modified.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/subscriptions/modifyPushConfig',
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
                'pushConfig': {
                    'pushEndpoint': pushEndpoint,
                },
                'subscription': subscription,
            },
        }
        return self._request(queryParams)

    def delete(self, subscription, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Deletes an existing subscription. All pending messages in the subscription are immediately dropped. Calls to Pull after deletion will return NOT_FOUND.'''
        queryParams = {
            'url': 'https://www.googleapis.com/pubsub/v1beta1/subscriptions/{+subscription}',
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
                'subscription': urlibQuoteEncode(subscription, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Pubsub(Service):
    '''Provides reliable, many-to-many, asynchronous messaging between applications.'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/pubsub']

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Pubsub, self).__init__(conn, *args, **kwargs)
        self.topics = Topics(self, conn, *args, **kwargs)
        self.subscriptions = Subscriptions(self, conn, *args, **kwargs)
