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

    def __init__(self, url, httpUrlParams=None, httpBodyParams=None, httpHeaders=None, method=None, formEncode=False, jsonEncode=True, * args, **kwargs):
        if httpUrlParams is None:
            httpUrlParams = {}
        if httpBodyParams is None:
            httpBodyParams = {}
        if httpHeaders is None:
            httpHeaders = {}
        self._url = url.format(**httpUrlParams),
        self._urlParams = httpUrlParams
        self._bodyParams = httpBodyParams
        self._headers = httpHeaders
        self._method = method
        self._formEncode = formEncode
        self._jsonEncode = jsonEncode
        self._dfd = None

    def run(self, agent):
        self._startTs = time.time()
        self._dfd = Deferred()
        dataProducer = None
        if self._headers is None:
            headers = {}
        headers['Accept-Encoding'] = ['gzip']
        if self._method in ('POST'):
            if self._jsonEncode and isinstance(self._bodyParams, dict) and len(self._bodyParams) > 0:
                self._upsertContentType(headers, 'application/json')
                data = json.dumps(self._bodyParams).encode('ascii', 'ignore')
                dataProducer = StringProducer(data)
            elif isinstance(self._bodyParams, basestring):
                dataProducer = StringProducer(self._bodyParams)
        if not self._urlParams:
            urlParams = {}
        if len(urlParams) > 0:
            encoded = urlencode(urlParams)
            self._url += '?' + encoded
            if self._formEncode:
                self._upsertContentType(headers, 'application/x-www-form-urlencoded')
                headers['Content-Length'] = [len(encoded)]
                dataProducer = StringProducer(encoded)
        elif len(self._bodyParams) > 0 and self._formEncode:
            encoded = urlencode(self._bodyParams).encode('ascii', 'ignore')
            if self._formEncode:
                self._upsertContentType(headers, 'application/x-www-form-urlencoded')
                # headers['Content-Length'] = [len(encoded)]
                dataProducer = StringProducer(encoded)
        self._url = self._url.encode('ascii', 'ignore')
        return agent.request(self._method, self._url, Headers(headers), dataProducer)

    def _upsertContentType(self, headers, contentType):
        if 'Content-Type' not in headers:
                headers['Content-Type'] = []
        if contentType not in headers['Content-Type']:
            headers['Content-Type'].append(contentType)

    def setToken(self, token):
        self.setHeaderField('Authorization', ['Bearer {}'.format(token)])

    def setHeaderField(self, fieldName, fieldValue):
        self._headers[fieldName] = fieldValue
