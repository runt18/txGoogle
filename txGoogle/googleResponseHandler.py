'''
Created on 9 sep. 2014

@author: sjuul
'''
from urllib import unquote
import simplejson as json
from txGoogle.responseHandler import ResponseHandler


class GoogleResponseHandler(ResponseHandler):

    def __init__(self, *args, **kwargs):
        super(GoogleResponseHandler, self).__init__(*args, **kwargs)
        self._result = None

    def handleLoaded(self, loaded, requestObj):
        if 'error' in loaded:
            if 'errors' in loaded['error']:
                errorMessages = [item['message'] for item in loaded['error']['errors']]
                self._dfd.errback(Exception('\n'.join(errorMessages)))
            else:
                self._dfd.errback(Exception(json.dumps(loaded['error'])))
        else:
            self._onResponse(loaded, requestObj)

    def _onResponse(self, loaded, requestObj):
        self._loadResults(loaded, requestObj)
        if 'nextPageToken' in loaded:
            requestObj.setUrlParam('pageToken', unquote(loaded['nextPageToken']))
            self._connection.request(requestObj, self)
        else:
            self._dfd.callback(self._result)

    def _loadResults(self, loaded, requestObj):
        loadFunName = '_loadResults_' + self._resultType
        if hasattr(self, loadFunName):
            loadFun = getattr(self, loadFunName)
            loadFun(loaded)
        else:
            self._result = loaded

    def _loadResults_multi(self, loaded):
        if self._result is None:
            self._result = []
        if loaded != 'Not Found':
            for v in loaded.itervalues():
                if isinstance(v, list):
                    self._result.extend(v)
