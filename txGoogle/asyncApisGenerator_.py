from collections import defaultdict
import json
# from subprocess import Popen
import os
import jinja2

CURRENT_DIR = os.path.dirname(__file__)
templatesDir = os.path.join(CURRENT_DIR, 'templates')
fsLoader = jinja2.FileSystemLoader(templatesDir)
JINJA_ENVIRONMENT = jinja2.Environment(loader=fsLoader, extensions=['jinja2.ext.autoescape'], lstrip_blocks=True, trim_blocks=True)


def render(templateName, **kwargs):
    template = JINJA_ENVIRONMENT.get_template(templateName)
    return template.render(**kwargs)


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


def generatePyCode(apiName, apiDict):
    
    def schemaFun(schemaDict, rParams=[], oParams=[], parentKeyIsRequired=True, parentKey='', sep='_'):
        bodyParams = {}
        for k, v in schemaDict.get('properties', {}).iteritems():
            ############DUPLICATE NAME HANDLING#############
            key = k
            newKey = parentKey + sep + k if parentKey else k
            if key in rParams or key in oParams: 
                key = newKey
            if key in rParams or key in oParams:
                key += '_'
            ################################################
            
            isRequired = 'Required' in v.get('description', '')
            if '$ref' in v:
                bodyParams[k], rParams, oParams = schemaFun(apiDict['schemas'][v['$ref']], rParams, oParams, isRequired, newKey)
            else:
                bodyParams[k] = key
                if parentKeyIsRequired and isRequired:
                    rParams.append(key)
                else:    
                    oParams.append(key)
        return bodyParams, rParams, oParams

    def generateMethodCode(methodName, method):
        if methodName == 'import':
            methodName = 'import_'

        rParams = [k for k, v in method.get('parameters', {}).iteritems() if 'required' in v]
        oParams = apiDict.get('parameters', {}).keys() + [k for k, v in method.get('parameters', {}).iteritems() if not 'required' in v]
        
        
        if 'request' in method:
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
    
        
    def generateResourceCode(resourceName, resource, scopes=None):
        functionCode = ''
        for k, v in resource.get('resources', {}).iteritems():
            functionCode += generateResourceCode(k, v)
            
        methodsDict = defaultdict(dict)
        for k, v in resource.get('methods', {}).iteritems():
            methodsDict[k] = generateMethodCode(k, v)
        
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
    scopes = apiDict['auth']['oauth2']['scopes'].keys()
    functionCode += generateResourceCode(apiDict['name'], apiDict, scopes)
    return functionCode, None
    

def generateCode(apiNames):
    for apiName, apiDict in loadApiDict(apiNames):
        print apiName
        code, tests = generatePyCode(apiName, apiDict)
        open('services/{}.py'.format(apiName + '_'), 'wb').write(code.replace('\t', '    '))
        #print tests
        #open('AsyncApis.py'.format(apiName), 'a').write(tests)


if __name__ == '__main__':
    # aApis = AsyncApis('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', '../apiFiles/AsyncBigQueryCredentials.json')
    # dfds = [aApis.bigquery.tables.list('over-sight', 'testdataset', fields='tables')]
    # reactor.run()

    generateCode(['gmail'])
    #Popen('python generated.py').communicate()
    pass