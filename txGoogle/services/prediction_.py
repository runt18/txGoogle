from txGoogle.service import Service
from urllib import quote as urlibQuoteEncode


class Trainedmodels(Service):
    def __init__(self, conn, *args, **kwargs):
        super(Trainedmodels, self).__init__(conn, *args, **kwargs)

    def insert(self, project, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, storageDataLocation=None, modelType=None, storagePMMLModelLocation=None, sourceModel=None, storagePMMLLocation=None, trainingInstances=None, id=None, utility=None):
        '''Train a Prediction API model.'''
        queryParams = {
            'url': 'https://www.googleapis.com/prediction/v1.6/projects/{project}/trainedmodels',
            'method': 'POST',
            'resultType': 'Insert2',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': urlibQuoteEncode(project, safe=''),
            },
            'httpBodyParams': {
                'storageDataLocation': storageDataLocation,
                'modelType': modelType,
                'storagePMMLModelLocation': storagePMMLModelLocation,
                'sourceModel': sourceModel,
                'storagePMMLLocation': storagePMMLLocation,
                'trainingInstances': trainingInstances,
                'id': id,
                'utility': utility,
            },
        }
        return self._request(queryParams)

    def get(self, project, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Check training status of your model.'''
        queryParams = {
            'url': 'https://www.googleapis.com/prediction/v1.6/projects/{project}/trainedmodels/{id}',
            'method': 'GET',
            'resultType': 'Insert2',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': urlibQuoteEncode(project, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def predict(self, project, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, input=None):
        '''Submit model id and request a prediction.'''
        queryParams = {
            'url': 'https://www.googleapis.com/prediction/v1.6/projects/{project}/trainedmodels/{id}/predict',
            'method': 'POST',
            'resultType': 'Output',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': urlibQuoteEncode(project, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
                'input': input,
            },
        }
        return self._request(queryParams)

    def list(self, project, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        '''List available models.'''
        queryParams = {
            'url': 'https://www.googleapis.com/prediction/v1.6/projects/{project}/trainedmodels/list',
            'method': 'GET',
            'resultType': 'List',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': urlibQuoteEncode(project, safe=''),
                'pageToken': pageToken,
                'maxResults': maxResults,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, project, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, output=None, csvInstance=None):
        '''Add new data to a trained model.'''
        queryParams = {
            'url': 'https://www.googleapis.com/prediction/v1.6/projects/{project}/trainedmodels/{id}',
            'method': 'PUT',
            'resultType': 'Insert2',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': urlibQuoteEncode(project, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
                'output': output,
                'csvInstance': csvInstance,
            },
        }
        return self._request(queryParams)

    def analyze(self, project, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Get analysis of the model and the data the model was trained on.'''
        queryParams = {
            'url': 'https://www.googleapis.com/prediction/v1.6/projects/{project}/trainedmodels/{id}/analyze',
            'method': 'GET',
            'resultType': 'Analyze',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': urlibQuoteEncode(project, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def delete(self, project, id, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Delete a trained model.'''
        queryParams = {
            'url': 'https://www.googleapis.com/prediction/v1.6/projects/{project}/trainedmodels/{id}',
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
                'project': urlibQuoteEncode(project, safe=''),
                'id': urlibQuoteEncode(id, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Hostedmodels(Service):
    def __init__(self, conn, *args, **kwargs):
        super(Hostedmodels, self).__init__(conn, *args, **kwargs)

    def predict(self, project, hostedModelName, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, input=None):
        '''Submit input and request an output against a hosted model.'''
        queryParams = {
            'url': 'https://www.googleapis.com/prediction/v1.6/projects/{project}/hostedmodels/{hostedModelName}/predict',
            'method': 'POST',
            'resultType': 'Output',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'project': urlibQuoteEncode(project, safe=''),
                'hostedModelName': urlibQuoteEncode(hostedModelName, safe=''),
            },
            'httpBodyParams': {
                'input': input,
            },
        }
        return self._request(queryParams)


class Prediction(Service):
    '''Lets you access a cloud hosted machine learning service that makes it easy to build smart apps'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/devstorage.read_only', u'https://www.googleapis.com/auth/devstorage.read_write', u'https://www.googleapis.com/auth/devstorage.full_control', u'https://www.googleapis.com/auth/prediction']

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Prediction, self).__init__(conn, *args, **kwargs)
        self.trainedmodels = Trainedmodels(conn, *args, **kwargs)
        self.hostedmodels = Hostedmodels(conn, *args, **kwargs)
