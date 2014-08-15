'''
Created on Aug 4, 2014

@author: sjuul
'''
from zope.interface.declarations import implements
from twisted.internet.protocol import Protocol
from twisted.web.http_headers import Headers
from twisted.web.client import RedirectAgent
from twisted.internet.defer import succeed
from twisted.internet.defer import Deferred
from twisted.web.iweb import IBodyProducer
from twisted.internet.defer import fail
from twisted.web.client import Agent
from twisted.internet import reactor
from StringIO import StringIO
from urllib import urlencode
import simplejson as json
from gzip import GzipFile


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


class ResponseReceiver(Protocol):

    def __init__(self, dfd, response, jsonHandleFun=None):
        self._jsonHandleFun = jsonHandleFun
        self.strIoBuff = StringIO()
        self.dfd = dfd
        self.contentType = response
        headers = dict(response.headers.getAllRawHeaders())
        self.contentType = ''
        self.contentEncoding = ''
        if 'Content-Type' in headers:
            contentType = headers['Content-Type'][0]
            if contentType.startswith('application/json'):
                self.contentType = 'json'
                idx = contentType.index('charset=')
                if idx >= 0:
                    self.charset = contentType[idx + 8:]
                else:
                    self.charset = ''
            else:
                self.contentType = contentType
        if 'Content-Encoding' in headers:
            self.contentEncoding = headers['Content-Encoding'][0]

    def dataReceived(self, data):
        self.strIoBuff.write(data)
        
    def _handleJson(self, data, dfd):
        dfd.callback(json.loads(data))

    def connectionLost(self, reason):
        self.strIoBuff.seek(0)
        try:
            if self.contentEncoding == 'gzip':
                try:
                    msg = GzipFile(fileobj=self.strIoBuff).read()
                except:
                    pass
            else:
                msg = self.strIoBuff.getvalue()
            self.strIoBuff.close()
            if self.contentType == 'json':
                if self._jsonHandleFun:
                    self._jsonHandleFun(msg, self.dfd)
                else:
                    self._handleJson(msg, self.dfd)
            else:
                self.dfd.callback(msg)
        except Exception as ex:
            self.dfd.errback(Exception(str(ex) + '\n' + msg))


class AsyncHttp(object):
    
    def __init__(self, jsonHandleFun=None):
        self._jsonHandleFun = jsonHandleFun
    

    def _handleResponse(self, response=None, *args, **kwargs):
        if response.code == 204:
            return succeed(None)
        else:
            dfdResponse = Deferred()
            receiver = ResponseReceiver(dfdResponse, response, jsonHandleFun=self._jsonHandleFun)
            response.deliverBody(receiver)
            return dfdResponse

    def httpRequest(self, url, urlParams=None, bodyParams=None, headers=None, method='POST', formEncode=False):
        dataProducer = None
        if headers is None:
            headers = {}
        headers['Accept-Encoding'] = ['gzip']
        if method in ('POST'):
            if isinstance(bodyParams, dict) and len(bodyParams) > 0:
                self._upsertContentType(headers, 'application/json')
                data = json.dumps(bodyParams).encode('ascii', 'ignore')
                dataProducer = StringProducer(data)
            elif isinstance(bodyParams, basestring):
                dataProducer = StringProducer(bodyParams)
            elif 'Content-Length' not in headers:
                headers['Content-Length'] = [0]
        if not urlParams:
            urlParams = {}
        if len(urlParams) > 0:
            encoded = urlencode(urlParams)
            url += '?' + encoded
            if formEncode:
                self._upsertContentType(headers, 'application/x-www-form-urlencoded')
                headers['Content-Length'] = [len(encoded)]
                dataProducer = StringProducer(encoded)
        url = url.encode('ascii', 'ignore')

        agent = RedirectAgent(Agent(reactor))
        try:
            dfdReq = agent.request(method, url, Headers(headers), dataProducer)
            dfdReq.addCallback(self._handleResponse)
            return dfdReq
        except Exception as ex:
            print ex
            fail(ex)

    def _upsertContentType(self, headers, contentType):
        if 'Content-Type' not in headers:
                headers['Content-Type'] = []
        if contentType not in headers['Content-Type']:
            headers['Content-Type'].append(contentType)
