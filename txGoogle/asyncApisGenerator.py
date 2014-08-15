import json
# from subprocess import Popen
from txGoogle.asyncBase import AsyncBase
from twisted.internet import reactor
import collections

'''deDuplicationRules = {
    'bigQuery': {
        'jobs': {
            'datasetId': ['destinationTableDataSetId', 'defaultDatasetDataSetId', 'sourceTableDataSetId']
        }
    }
}'''


def capitalizeFirstChar(inp):
    if inp:
        return inp[0].upper() + inp[1:]
    else:
        return inp


def loadApiDict(apiNames):
    names = []
    for apiDescription in json.load(open('apis.json'))[::-1]:
        if apiDescription['name'] not in names:
            names.append(apiDescription['name'])
            if apiDescription['name'] in apiNames:
                yield apiDescription['name'], apiDescription


def extractSchema(schemaName, apiDict):
    nested = {}
    flat = {}
    for paramName, paramProperties in apiDict['schemas'][schemaName]['properties'].iteritems():
        if paramProperties.get('description', '').startswith('[Output-only]'):
            continue
        elif paramProperties.get('description', '').startswith('[Deprecated]'):
            continue
        elif paramProperties.get('description', '').startswith('[Required]'):
            if '$ref' in paramProperties:
                newNested, newFlat = extractSchema(paramProperties['$ref'], apiDict)
                nested[paramName] = newNested
                flat.update(newFlat)
            else:
                nested[paramName] = '---' + paramName + '---'
                flat[paramName] = paramName
        else:
            if '$ref' in paramProperties:
                newNested, newFlat = extractSchema(paramProperties['$ref'], apiDict)
                nested[paramName] = newNested
                flat.update({a: None for a in newFlat})
            else:
                nested[paramName] = '---' + paramName + '---'
                flat[paramName] = None
    return nested, flat


def createMethod(conn, methodName, methodDict, apiDict):
    
    queryParams = {
        'url': apiDict['baseUrl'] + methodDict['path'],
        'method': str(methodDict['httpMethod']),
        'resultType': 'empty',
        'httpBodyParams': {},
        'httpUrlParams': {'prettyPrint': False}, #TODO fix
    }

    if 'response' in methodDict:
        if 'nextPageToken' in apiDict['schemas'][methodDict['response']['$ref']]['properties']:
            queryParams['resultType'] = 'multi'
        else:
            queryParams['resultType'] = methodDict['response']['$ref']
    
    def _buildQueryParams(*args, **kwargs):
        #TODO walk kwargs for nameerror notification???
        assert len(args) == len(methodDict.get('parameterOrder', []))
        for i, paramName in enumerate(methodDict.get('parameterOrder', [])):
            queryParams[paramName] = args[i]
        
        for paramName, paramProperties in methodDict.get('parameters', {}).iteritems():
            if paramProperties['location'] == 'query':
                if 'required' in paramProperties:
                    assert paramName in kwargs
                    #print paramName, paramProperties['location'], methodDict['id']
                    queryParams['httpUrlParams'][paramName] = kwargs[paramName]
            if paramName in kwargs:
                queryParams['httpUrlParams'][paramName] = kwargs[paramName]
            
        if 'request' in methodDict:
            schemaName = methodDict['request']['$ref']
            
            if 'fields' in kwargs:
                if 'nextPageToken' in apiDict['schemas'][schemaName]['properties']:
                    queryParams['httpUrlParams']['fields'] = 'nextPageToken,' + kwargs['fields']
                else:
                    queryParams['httpUrlParams']['fields'] = kwargs['fields']
                    
            for paramName, paramProperties in apiDict['schemas'][schemaName]['properties'].iteritems():
                if paramName in kwargs:
                    queryParams['httpBodyParams'][paramName] = kwargs[paramName]
                elif paramProperties['description'].startswith('[Required]'):
                    assert paramName in kwargs
                    queryParams['httpBodyParams'][paramName] = kwargs[paramName]
            
        print json.dumps(queryParams, indent=2)
        return queryParams

    def _method(*args, **kwargs):
        dfd = conn._asyncHttpRequest(_buildQueryParams(*args, **kwargs))
        return dfd
    return _method


class Resource():
    def __init__(self, api, resourceName, resourceDict, apiDict):
        for methodName, methodDict in resourceDict.get('methods', {}).iteritems():
            setattr(self, methodName, createMethod(api, methodName, methodDict, apiDict))
        
        
class Schema():
    def __init__(self, schemaName, extractSchema):
        pass
    

class Api():
    def __init__(self, apis, apiName, apiDict):
        
        for resourceName, resourceDict in apiDict.get('resources', {}).iteritems():
            assert not hasattr(self, resourceName), 'resourceName {} was already defined.'.format(resourceDict)
            setattr(self, resourceName, Resource(apis, resourceName, resourceDict, apiDict))
            #print '', resourceName
            
        for schemaName, schemaDict in apiDict.get('schemas', {}).iteritems():
            assert not hasattr(self, '_'+schemaName), 'schemaName _{} was already defined.'.format(schemaName)
            setattr(self, '_'+schemaName, Schema(schemaName, schemaDict))
            #print 's', schemaName#, v#['properties']#['kind']['default']
        
              
class AsyncApis(AsyncBase):
    _SCOPE = 'https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/devstorage.full_control'

    def __init__(self, *args, **kwargs):
        super(AsyncApis, self).__init__(*args, **kwargs)

    def _multipleResultsPossible(self, resultType):
        return resultType in ('multi')
        
    def _loadResults_multi(self, loaded):
        for value in loaded.itervalues():
            if isinstance(value, list):
                for item in value:
                    yield item            

    def loadServices(self, apiNames):
        for apiName, apiDict in loadApiDict(apiNames):
            setattr(self, apiName, Api(self, apiName, apiDict))
            
            
def generatePyCode(apiName, apiDict):
    
    def generateMethodCode(resourceName, methodName, methodDict):
        if methodName == 'import':
            methodName = 'import_'
        
        queryParams = {
            'url': apiDict['baseUrl'] + methodDict['path'],
            'method': str(methodDict['httpMethod']),
            'resultType': 'empty',
            'httpBodyParams': {},
            'httpUrlParams': {},
        }
        
        apiParams = apiDict['parameters'].keys()
        for paramName in apiParams:
            queryParams['httpUrlParams'][paramName] = '---' + paramName + '---'
        
        pathParams = []
        for paramName in methodDict.get('parameterOrder', []):
            pathParams.append(paramName)
            queryParams[paramName] = '---' + paramName + '---'
        
        urlParams = []
        optionalUrlParams = []
        for paramName, paramProperties in methodDict.get('parameters', {}).iteritems():
            if paramProperties['location'] == 'query':
                if 'required' in paramProperties:
                    urlParams.append(paramName)
                else:
                    optionalUrlParams.append(paramName)
                queryParams['httpUrlParams'][paramName] = '---' + paramName + '---'
                    
        bodyParamsFlat = {}
        if 'request' in methodDict:
            schemaName = methodDict['request']['$ref']
        
            bodyParams, bodyParamsFlat = extractSchema(schemaName, apiDict)
            queryParams['httpBodyParams'] = bodyParams
        
        if 'response' in methodDict:
            if 'nextPageToken' in apiDict['schemas'][methodDict['response']['$ref']]['properties']:
                queryParams['resultType'] = 'multi'
            else:
                queryParams['resultType'] = methodDict['response']['$ref']
                                        
        duplicates = [x for x, y in collections.Counter(urlParams).items() if y > 1]
        if len(duplicates) > 0:
            raise Exception('Add some deduplication rules for {}'.format(duplicates))
        
        requiredParams = pathParams + [paramName for paramName in urlParams if not paramName in pathParams] + [paramName for paramName, param in bodyParamsFlat.iteritems() if param and not paramName in pathParams and not paramName in urlParams]
        optionalParams = [paramName for paramName in optionalUrlParams + bodyParamsFlat.keys() if not paramName in requiredParams]
        params = [paramName for paramName in requiredParams] + [paramName+'=None' for paramName in apiParams] + [paramName+'=None' for paramName in optionalParams if not paramName in apiParams]
        
        functionCode = '\n\n\tdef {}({}):'.format(methodName, ', '.join(['self'] + params))
        functionCode += '\n\t\t"{}"'.format(methodDict['description'])
        functionCode += '\n\t\tqueryParams = ' + '\n\t\t'.join(json.dumps(queryParams, indent=4).replace('"---', '').replace('---"', '').split('\n'))
        functionCode += '\n\t\treturn self._conn._asyncHttpRequest(leaveOutNulls(queryParams))'
        
        functionCodeCallCode = '\n#aApi.{}.{}.{}({}),'.format(capitalizeFirstChar(apiDict['name']), resourceName, methodName, ', '.join(requiredParams))
        return functionCode, functionCodeCallCode

    
    def exploreApis(resourceName, resource):
        functionCode = ''
        functionCodeCallCode = ''
    
        capResourceName = capitalizeFirstChar(resourceName)
        functionCode += '\n\n\nclass {}(object):'.format(capResourceName)
        functionCode += '\n\tdef __init__(self, connection, *args, **kwargs):'
        functionCode += '\n\t\tself._conn = connection'

        
        for resourceName, resource_ in resource.get('resources', {}).iteritems():
            functionCode += '\n\t\tself.{0} = {1}(connection)'.format(resourceName, capitalizeFirstChar(resourceName))
            
        for methodName, method in resource.get('methods', {}).iteritems():
            functionCode_, functionCodeCallCode_ = generateMethodCode(resourceName, methodName, method)
            functionCode += functionCode_
            functionCodeCallCode += functionCodeCallCode_
        
        for resourceName, resource_ in resource.get('resources', {}).iteritems():
            functionCode_, functionCodeCallCode_ = exploreApis(resourceName, resource_)
            functionCode += functionCode_
            functionCodeCallCode += functionCodeCallCode_
            
        return functionCode, functionCodeCallCode
    
    functionCode = 'from txGoogle.asyncUtils import leaveOutNulls'
    functionCodeCallCode = ''
    functionCode_, functionCodeCallCode_ = exploreApis(apiName, apiDict)
    functionCode += functionCode_
    functionCodeCallCode += functionCodeCallCode_

    return functionCode, functionCodeCallCode 


def generateCode(apiNames):
    for apiName, apiDict in loadApiDict(apiNames):
        code, tests = generatePyCode(apiName, apiDict)
        open('services/{}.py'.format(apiName + '_'), 'wb').write(code)
        print tests
        #open('AsyncApis.py'.format(apiName), 'a').write(tests)


if __name__ == '__main__':
    # aApis = AsyncApis('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', '../apiFiles/AsyncBigQueryCredentials.json')
    # dfds = [aApis.bigquery.tables.list('over-sight', 'testdataset', fields='tables')]
    # reactor.run()

    generateCode(['gmail'])
    #Popen('python generated.py').communicate()
    pass
