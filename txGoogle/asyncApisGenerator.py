from collections import defaultdict
import json
import os
import jinja2
from txGoogle.duplicateParams import duplicateDict

CURRENT_DIR = os.path.dirname(__file__)
templatesDir = os.path.join(CURRENT_DIR, 'templates')
fsLoader = jinja2.FileSystemLoader(templatesDir)
JINJA_ENVIRONMENT = jinja2.Environment(loader=fsLoader, extensions=['jinja2.ext.autoescape'], lstrip_blocks=True, trim_blocks=True)

_APIDOCS_PATH = '../apiFiles/'


def render(templateName, **kwargs):
    template = JINJA_ENVIRONMENT.get_template(templateName)
    return template.render(**kwargs)


def capitalizeFirstChar(inp):
    if inp:
        return inp[0].upper() + inp[1:]
    else:
        return inp


def loadApiDict(apiNames):
    for apiName in apiNames:
        filename = os.path.join(_APIDOCS_PATH, apiName) + '.json'
        if os.path.exists(filename):
            apiDescription = json.load(open(filename))
            yield apiName, apiDescription
        else:
            print filename


def generatePyCode(apiName, apiDict):

    def generateMethodCode(methodName, method):
        if methodName == 'import':
            methodName = 'import_'

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
                    if key in rParams or key in oParams:
                        print method['id'], newKey

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
        else:
            bodyParams = {}

        methodLines = render('template_method.py', apiDict=apiDict,
                                                   methodName=methodName,
                                                   methodDict=method,
                                                   bodyParams=bodyParams,
                                                   rParams=rParams,
                                                   oParams=oParams)
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
            methodsDict[methodName] = generateMethodCode(methodName, methodDict)

        if scopes:
            resourceLines = render('template_api.py', resourceName=resourceName,
                                                           resourceDict=resource,
                                                           methodsDict=methodsDict,
                                                           scopes=scopes)
        else:
            resourceLines = render('template_resource.py', resourceName=resourceName,
                                                           resourceDict=resource,
                                                           methodsDict=methodsDict)
        functionCode += resourceLines
        return functionCode

    functionCode = 'from txGoogle.utils import leaveOutNulls\n'
    if 'auth' in apiDict:
        scopes = apiDict['auth']['oauth2']['scopes'].keys()
    else:
        scopes = ['']
    functionCode += generateResourceCode(apiDict['name'], apiDict, scopes)
    return functionCode, None


def generateCode(apiNames):
    for apiName, apiDict in loadApiDict(apiNames):
        code, tests = generatePyCode(apiName, apiDict)
        fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'services/{}.py'.format(apiName + '_'))
        fl = open(fileName, 'wb')
        fl.write(code.replace('\t', '    '))
        fl.close()
        print 'generated {}'.format(fileName)


if __name__ == '__main__':
    # aApis = AsyncApis('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', '../apiFiles/AsyncBigQueryCredentials.json')
    # dfds = [aApis.bigquery.tables.list('over-sight', 'testdataset', fields='tables')]
    # reactor.run()

    generateCode(['bigquery', 'cloudmonitoring', 'datastore', 'gmail', 'pubsub', 'storage'])
    #Popen('python generated.py').communicate()
    pass
