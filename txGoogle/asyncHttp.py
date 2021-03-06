'''
Created on Aug 4, 2014

@author: sjuul
'''
from twisted.internet.protocol import Protocol
from twisted.web.client import RedirectAgent
from twisted.internet.defer import succeed, logError
from twisted.internet.defer import Deferred
from twisted.internet.defer import fail
from twisted.web.client import Agent
from twisted.internet import reactor
from twisted.python import log
from StringIO import StringIO
from gzip import GzipFile
from txGoogle.response import Response
from twisted.web import client


client._HTTP11ClientFactory.noisy = False


class ResponseReceiver(Protocol):

    def _getCharset(self, contentType):
        self.charset = ''
        if 'charset=' in contentType:
            idx = contentType.index('charset=')
            if idx >= 0:
                self.charset = contentType[idx + 8:]

    def __init__(self, dfd, responseHeaders):
        self.strIoBuff = StringIO()
        self.contentType = ''
        self.contentEncoding = ''
        self.dfd = dfd
        if 'Content-Type' in responseHeaders:
            contentType = responseHeaders['Content-Type'][0]
            if ' ' in contentType:
                self.contentType = contentType.split(' ')[0]
            else:
                self.contentType = contentType
            if self.contentType.endswith(';'):
                self.contentType = self.contentType[:-1]
            self._getCharset(contentType)
        if 'Content-Encoding' in responseHeaders:
            self.contentEncoding = responseHeaders['Content-Encoding'][0]

    def dataReceived(self, data):
        self.strIoBuff.write(data)

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
            resp = Response(self.contentType, msg, self.charset)
            self.dfd.callback(resp)

        except Exception as ex:
            self.dfd.errback(Exception(str(ex) + '\n' + msg))


class AsyncHttp(object):

    def __init__(self):
        self._agent = RedirectAgent(Agent(reactor))

    def _handleResponse(self, response, requestObj):
        if response.code == 204:
            return succeed(Response(None, None, None))
        else:
            dfdResponse = Deferred()
            headers = dict(response.headers.getAllRawHeaders())
            receiver = ResponseReceiver(dfdResponse, headers)
            response.deliverBody(receiver)
            return dfdResponse

    def asyncHttpRequest(self, request):
        try:
            dfdReq = request.run(self._agent)
            dfdReq.addCallback(self._handleResponse, request)
            dfdReq.addErrback(logError)
            return dfdReq
        except Exception as ex:
            log.err()
            return fail(ex)
