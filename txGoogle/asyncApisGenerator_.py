from collections import defaultdict
import json
# from subprocess import Popen
import os
import jinja2

CURRENT_DIR = os.path.dirname(__file__)
templatesDir = os.path.join(CURRENT_DIR, 'templates')
fsLoader = jinja2.FileSystemLoader(templatesDir)
JINJA_ENVIRONMENT = jinja2.Environment(loader=fsLoader, extensions=['jinja2.ext.autoescape'], lstrip_blocks=True, trim_blocks=True)


paramNamesNewDict = {'gmail.users.messages.attachments.get': {
    },
    'gmail.users.messages.insert': {
    },
    'gmail.users.messages.untrash': {
    },
    'gmail.users.messages.get': {
    },
    'gmail.users.messages.list': {
    },
    'gmail.users.messages.modify': {
    },
    'gmail.users.messages.send': {
    },
    'gmail.users.messages.import': {
    },
    'gmail.users.messages.trash': {
    },
    'gmail.users.messages.delete': {
    },
    'gmail.users.labels.get': {
    },
    'gmail.users.labels.create': {
    },
    'gmail.users.labels.list': {
    },
    'gmail.users.labels.update': {
        'id': 'id',
    },
    'gmail.users.labels.patch': {
        'id': 'id',
    },
    'gmail.users.labels.delete': {
    },
    'gmail.users.threads.untrash': {
    },
    'gmail.users.threads.get': {
    },
    'gmail.users.threads.list': {
    },
    'gmail.users.threads.modify': {
    },
    'gmail.users.threads.trash': {
    },
    'gmail.users.threads.delete': {
    },
    'gmail.users.drafts.get': {
    },
    'gmail.users.drafts.create': {
        'id': 'id',
    },
    'gmail.users.drafts.list': {
    },
    'gmail.users.drafts.update': {
        'id': 'message_id',
        'id': 'id',
    },
    'gmail.users.drafts.send': {
        'id': 'id',
    },
    'gmail.users.drafts.delete': {
    },
    'gmail.users.history.list': {
    },
    'bigquery.tables.insert': {
        'fields': 'schema_fields',
        'projectId': 'tableReference_projectId',
        'datasetId': 'tableReference_datasetId',
    },
    'bigquery.tables.get': {
    },
    'bigquery.tables.list': {
    },
    'bigquery.tables.update': {
        'fields': 'schema_fields',
        'projectId': 'tableReference_projectId',
        'tableId': 'tableReference_tableId',
        'datasetId': 'tableReference_datasetId',
    },
    'bigquery.tables.patch': {
        'fields': 'schema_fields',
        'projectId': 'tableReference_projectId',
        'tableId': 'tableReference_tableId',
        'datasetId': 'tableReference_datasetId',
    },
    'bigquery.tables.delete': {
    },
    'bigquery.datasets.insert': {
        'projectId': 'datasetReference_projectId',
    },
    'bigquery.datasets.get': {
    },
    'bigquery.datasets.list': {
    },
    'bigquery.datasets.update': {
        'projectId': 'datasetReference_projectId',
        'datasetId': 'datasetReference_datasetId',
    },
    'bigquery.datasets.patch': {
        'projectId': 'datasetReference_projectId',
        'datasetId': 'datasetReference_datasetId',
    },
    'bigquery.datasets.delete': {
    },
    'bigquery.jobs.insert': {
        'totalBytesProcessed': 'statistics_query_totalBytesProcessed',
        'projectId': 'jobReference_projectId',
        'projectId': 'configuration_load_destinationTable_projectId',
        'fields': 'configuration_load_schema_fields',
        'createDisposition': 'configuration_link_createDisposition',
        'writeDisposition': 'configuration_link_writeDisposition',
        'projectId': 'configuration_link_destinationTable_projectId',
        'tableId': 'configuration_link_destinationTable_tableId',
        'datasetId': 'configuration_link_destinationTable_datasetId',
        'projectId': 'configuration_query_defaultDataset_projectId',
        'datasetId': 'configuration_query_defaultDataset_datasetId',
        'projectId': 'configuration_query_destinationTable_projectId',
        'tableId': 'configuration_query_destinationTable_tableId',
        'datasetId': 'configuration_query_destinationTable_datasetId',
        'writeDisposition': 'configuration_query_writeDisposition',
        'createDisposition': 'configuration_query_createDisposition',
        'createDisposition': 'configuration_copy_createDisposition',
        'writeDisposition': 'configuration_copy_writeDisposition',
        'projectId': 'configuration_copy_destinationTable_projectId',
        'tableId': 'configuration_copy_destinationTable_tableId',
        'datasetId': 'configuration_copy_destinationTable_datasetId',
        'projectId': 'configuration_copy_sourceTable_projectId',
        'tableId': 'configuration_copy_sourceTable_tableId',
        'datasetId': 'configuration_copy_sourceTable_datasetId',
        'fieldDelimiter': 'configuration_extract_fieldDelimiter',
        'projectId': 'configuration_extract_sourceTable_projectId',
        'tableId': 'configuration_extract_sourceTable_tableId',
        'datasetId': 'configuration_extract_sourceTable_datasetId',
    },
    'bigquery.jobs.get': {
    },
    'bigquery.jobs.list': {
    },
    'bigquery.jobs.getQueryResults': {
    },
    'bigquery.jobs.query': {
        'projectId': 'defaultDataset_projectId',
    },
    'bigquery.tabledata.list': {
    },
    'bigquery.tabledata.insertAll': {
    },
    'bigquery.projects.list': {
    },
}


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
                print "        '{}': '{}',".format(newKey, k)
                #key = newKey
            #if key in rParams or key in oParams:
            #    key += '_'
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
            print "    '{}': ".format(method['id']) + '{'
            bodyParams, rParams, oParams = schemaFun(schema, rParams, oParams)
            print '    },'
        else:
            bodyParams = {}
        
        methodLines = render('template_method.py', apiDict=apiDict, 
                                                   methodName=methodName, 
                                                   methodDict=method, 
                                                   bodyParams=bodyParams, 
                                                   rParams=rParams, 
                                                   oParams=oParams,
                                                   paramNamesNewDict=paramNamesNewDict)
        return methodLines
    
        
    def generateResourceCode(resourceName, resource, scopes=None):
        functionCode = ''
        for resourceName_, resourceDict_ in resource.get('resources', {}).iteritems():
            functionCode += generateResourceCode(resourceName_, resourceDict_)
            
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
        open('services/{}.py'.format(apiName + '_'), 'wb').write(code.replace('\t', '    '))
        #print tests
        #open('AsyncApis.py'.format(apiName), 'a').write(tests)


if __name__ == '__main__':
    # aApis = AsyncApis('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', '../apiFiles/AsyncBigQueryCredentials.json')
    # dfds = [aApis.bigquery.tables.list('over-sight', 'testdataset', fields='tables')]
    # reactor.run()

    generateCode(['discovery', 'gmail', 'bigquery'])
    #Popen('python generated.py').communicate()
    pass