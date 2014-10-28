'''Label
Created on 3 okt. 2014

@author: sjuul
'''
from txGoogle.googleResponseHandler import GoogleResponseHandler


class GcsResponseHandler(GoogleResponseHandler):

    def _loadResults_Objects(self, loaded):
        if self._result is None:
            self._result = {'items': [], 'prefixes': []}
        if 'items' in loaded:
            self._result['items'].extend(loaded['items'])
        if 'prefixes' in loaded:
            self._result['prefixes'].extend(loaded['prefixes'])

    def _getResultLen_Objects(self):
        return len(self._result['items']) + len(self._result['prefixes'])
