'''
Created on 21 aug. 2014

@author: sjuul
'''
from zope.interface.declarations import implements
from twisted.web.http_headers import Headers
from twisted.web.iweb import IBodyProducer
from twisted.internet.defer import succeed
from twisted.internet.defer import Deferred
from urllib import urlencode
import simplejson as json
import time
from txGoogle.utils import simpleDeepCopy
from twisted.python import log
import logging
from string import Formatter


class StringProducer(object):
    implements(IBodyProducer)

    def __init__(self, body):
        self.body = body
        self.length = len(body)

    def startProducing(self, consumer):
        consumer.write(self.body)
        return succeed(None)

    def pauseProducing(self):
        pass

    def stopProducing(self):
        pass


class Request(object):
    '''
    - httpBodyParams: parameters for the body of the http request in the form of a dict
    - httpUrlParams: parameters for the url of the http request in the form of a dict
    - httpHeaders: http headers in the form of a dict. AsyncOAuthConnectionHandler knows for example that when 'application/json' in headers['Content-Type'] it should json-dump the hhtpParams into the request body.
    - results: a variable to be used to build up the result. Most likely useful when doing pagination
    - url: this is the url where the request is sent to. This can contain parameters eg: https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId} these parameters are expected to be available in the queryParams dict and are filled in just before the request is executed
    - "url parameters": as described above
    - method: http method; POST / GET / UPDATE ...
    '''

    def __init__(self, url, httpUrlParams=None, httpBodyParams=None, httpHeaders=None, method=None, formEncode=False, jsonEncode=True, *args, **kwargs):
        if httpUrlParams is None:
            httpUrlParams = {}
        if httpBodyParams is None:
            httpBodyParams = {}
        if httpHeaders is None:
            httpHeaders = {}
        self._url = url.format(**httpUrlParams)
        self._urlParams = httpUrlParams
        for tup in Formatter().parse(url):
            if len(tup) > 0 and tup[1] is not None:
                del self._urlParams[tup[1]]
        self._bodyParams = httpBodyParams
        self._headers = httpHeaders
        self._method = method
        self._formEncode = formEncode
        self._jsonEncode = jsonEncode
        self._dfd = None

    def run(self, agent):
        self._startTs = time.time()
        self._dfd = Deferred()
        #make sure we don't edit the original request properties
        headers = simpleDeepCopy(self._headers)
        bodyParams = simpleDeepCopy(self._bodyParams)
        urlParams = simpleDeepCopy(self._urlParams)
        return self._run(agent, headers, self._method, bodyParams, urlParams, self._url)

    def setAcceptGzip(self):
        self.setHeaderField('Accept-Encoding', ['gzip'])

    def _run(self, agent, headers, method, bodyParams, urlParams, url):
        dataProducer = None
        if method in ('POST'):
            if self._jsonEncode and isinstance(bodyParams, dict) and len(bodyParams) > 0:
                self._upsertContentType(headers, 'application/json')
                data = json.dumps(bodyParams).encode('ascii', 'ignore')
                dataProducer = StringProducer(data)
            elif isinstance(bodyParams, basestring):
                dataProducer = StringProducer(bodyParams)
        if not urlParams:
            urlParams = {}
        if len(urlParams) > 0:
            encoded = urlencode(urlParams)
            url += '?' + encoded
            if self._formEncode:
                self._upsertContentType(headers, 'application/x-www-form-urlencoded')
                headers['Content-Length'] = [len(encoded)]
                dataProducer = StringProducer(encoded)
        elif len(bodyParams) > 0 and self._formEncode:
            encoded = urlencode(bodyParams).encode('ascii', 'ignore')
            if self._formEncode:
                self._upsertContentType(headers, 'application/x-www-form-urlencoded')
                # headers['Content-Length'] = [len(encoded)]
                dataProducer = StringProducer(encoded)
        url = url.encode('ascii', 'ignore')
        log.msg('fetching {}'.format(url), logLevel=logging.DEBUG)
        return agent.request(method, url, Headers(headers), dataProducer)

    def _upsertContentType(self, headers, contentType):
        if 'Content-Type' not in headers:
                headers['Content-Type'] = []
        if contentType not in headers['Content-Type']:
            headers['Content-Type'].append(contentType)

    def setToken(self, token):
        self.setHeaderField('Authorization', ['Bearer {}'.format(token)])

    def setHeaderField(self, fieldName, fieldValue):
        self._headers[fieldName] = fieldValue

    def setUrlParam(self, key, value):
        self._urlParams[key] = value

    def setUrlParams(self, urlParams):
        self._urlParams = urlParams

    def setBodyParm(self, key, value):
        self._bodyParams[key] = value

    def getUrlParam(self, key):
        return self._urlParams.get(key)
