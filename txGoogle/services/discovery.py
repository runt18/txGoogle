from txGoogle.utils import leaveOutNulls

class Apis():
    def __init__(self, conn):
        self._conn = conn

    def getRest(self, api, version, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Retrieve the description of a particular version of an api.'''
        queryParams = {
            'url': 'https://www.googleapis.com/discovery/v1/apis/{api}/{version}/rest',
            'method': 'GET',
            'resultType': 'dummy',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'api': api,
                'version': version,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

    def list(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, name=None, preferred=None):
        '''Retrieve the list of APIs supported at this endpoint.'''
        queryParams = {
            'url': 'https://www.googleapis.com/discovery/v1/apis',
            'method': 'GET',
            'resultType': 'dummy',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'name': name,
                'preferred': preferred,
            },
            'httpBodyParams': {
            },
        }
        return self._conn._asyncHttpRequest(leaveOutNulls(queryParams))

class Discovery():
    '''Lets you discover information about other Google APIs, such as what APIs are available, the resource and method details for each API.'''
    _DEFAULT_SCOPES = ['']
    
    def __init__(self, conn=None, scopes=None):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        self.apis = Apis(conn)
