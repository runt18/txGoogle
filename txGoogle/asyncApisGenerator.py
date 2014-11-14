from collections import defaultdict, OrderedDict
import json
import os
import jinja2
from txGoogle.duplicateParams import duplicateDict
import collections

CURRENT_DIR = os.path.dirname(__file__)
templatesDir = os.path.join(CURRENT_DIR, 'templates')
fsLoader = jinja2.FileSystemLoader(templatesDir)
JINJA_ENVIRONMENT = jinja2.Environment(loader=fsLoader, extensions=['jinja2.ext.autoescape'], lstrip_blocks=True, trim_blocks=True)

_APIDOCS_PATH = 'apiFiles/'


def render(templateName, **kwargs):
    template = JINJA_ENVIRONMENT.get_template(templateName)
    return template.render(**kwargs)


def capitalizeFirstChar(inp):
    if inp:
        return inp[0].upper() + inp[1:]
    else:
        return inp


def getDuplicates(lst):
    return [x for x, y in collections.Counter(lst).items() if y > 1]


def generatePyCode(apiName, apiDict):

    def generateMethodCode(resourceName, methodName, method):

        def getFullMethodName():
            return '{}.{}.{}'.format(apiName, resourceName, methodName)

        if methodName == 'import':
            methodName = 'import_'

        paramsToEncode = [k for k, v in method.get('parameters', {}).iteritems() if 'location' in v and v['location'] == 'path']

        rParams = [k for k, v in method.get('parameters', {}).iteritems() if 'required' in v]
        oParams = apiDict.get('parameters', {}).keys() + [k for k, v in method.get('parameters', {}).iteritems() if not 'required' in v]

        if 'request' in method:
            def schemaFun(schemaDict, rParams=[], oParams=[], parentKeyIsRequired=True, parentKey='', sep='_'):
                bodyParams = {}
                for k, v in schemaDict.get('properties', {}).iteritems():
                    key = k
                    newKey = parentKey + sep + k if parentKey else k

                    paramKey = '{}:{}:{}'.format(apiDict['id'], method['id'], newKey)
                    key = duplicateDict.get(paramKey, key)
                    if (key in rParams or key in oParams) and not paramKey in duplicateDict:
                        pass  #raise Exception('Duplicate key {} found. Try adding\n"{}": <NEW_KEY_ALIAS>,\nto duplicateParams.py'.format(key, paramKey))

                    description = v.get('description', '')
                    isRequired = 'Required' in description
                    if 'Output-only' in description:
                        continue
                    if '$ref' in v:
                        bodyParams[k], rParams, oParams = schemaFun(apiDict['schemas'][v['$ref']], rParams, oParams, isRequired, newKey)
                    else:
                        bodyParams[k] = key
                        if parentKeyIsRequired and isRequired:
                            rParams.append(key)
                        else:
                            oParams.append(key)

                return bodyParams, rParams, oParams

            schema = apiDict['schemas'][method['request']['$ref']]
            bodyParams, rParams, oParams = schemaFun(schema, rParams, oParams)

            rParamsSet = []
            for itm in rParams:
                if not itm in rParamsSet:
                    rParamsSet.append(itm)
            rParams = rParamsSet

            rParams = list(OrderedDict.fromkeys(rParams))
            oParams = list(OrderedDict.fromkeys(oParams))

            for key in list(oParams):
                if key in rParams:
                    oParams.remove(key)
            allParams = oParams + rParams
            duplicates = getDuplicates(allParams)
            if duplicates:
                raise Exception('Duplicate params detected in {}: {}'.format(getFullMethodName(), ','.join(duplicates)))

        else:
            bodyParams = {}

        methodLines = render('method.py', apiDict=apiDict,
                                                   methodName=methodName,
                                                   methodDict=method,
                                                   bodyParams=bodyParams,
                                                   rParams=rParams,
                                                   oParams=oParams,
                                                   paramsToEncode=paramsToEncode)
        return methodLines

    def generateResourceCode(resourceName, resource, scopes=None, existingResources=None):
        if existingResources is None:
            existingResources = set()
        functionCode = ''
        existingResources.add(resourceName)

        for resourceName_, resourceDict_ in resource.get('resources', {}).iteritems():
            if resourceName_ not in existingResources:
                functionCode += generateResourceCode(resourceName_, resourceDict_, existingResources=existingResources)
            else:
                print 'skipping {}'.format(resourceName_)

        methodsDict = defaultdict(dict)
        for methodName, methodDict in resource.get('methods', {}).iteritems():
            methodsDict[methodName] = generateMethodCode(resourceName, methodName, methodDict)

        if scopes:
            resourceLines = render('service.py', resourceName=resourceName,
                                                           resourceDict=resource,
                                                           methodsDict=methodsDict,
                                                           scopes=scopes)
        else:
            resourceLines = render('resource.py', resourceName=resourceName,
                                                           resourceDict=resource,
                                                           methodsDict=methodsDict)
        functionCode += resourceLines
        return functionCode

    functionCode = 'from txGoogle.googleService import Service\nfrom urllib import quote as urlibQuoteEncode\nfrom txGoogle.googleResource import Resource\n'
    if 'auth' in apiDict:
        scopes = apiDict['auth']['oauth2']['scopes'].keys()
    else:
        scopes = ['']
    functionCode += generateResourceCode(apiDict['name'], apiDict, scopes)
    return functionCode, None


def generateCode(apiNames):
    for apiName in apiNames:
        apiFilename = 'apiFiles/{}.json'.format(apiName)
        if not os.path.exists(apiFilename):
            print 'Api description file ({}) does not exist. Try downloading it with discovery service wrapper'.format(apiFilename)
        else:
            apiDict = json.load(open(apiFilename))

            code, tests = generatePyCode(apiName, apiDict)
            open('services/{}.py'.format(apiName + '_'), 'wb').write(code)
    #open('AsyncApis.py'.format(apiName), 'a').write(tests)


if __name__ == '__main__':
    # aApis = AsyncApis('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', '../apiFiles/AsyncBigQueryCredentials.json')
    # dfds = [aApis.bigquery.tables.list('over-sight', 'testdataset', fields='tables')]
    # reactor.run()

    generateCode(['bigquery', 'cloudmonitoring', 'datastore', 'gmail', 'pubsub', 'storage', 'prediction'])
    #Popen('python generated.py').communicate()
    pass
