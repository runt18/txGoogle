txGoogle
========

Twisted implementations of Google JSON API's

The main reasons for building this library:
- we wanted to use twisted (if you don't this library might not be for you)
- pythons httplib is not thread safe and googles library is built on top of httplib
- we wanted to have autocompletion in eclipse 
- googles api for python generates code but it wasn't inspectable by reading files.


## The following services already have wrappers:

- Gmail
- Google Cloud Datastore (GCD)
- Google Cloud Storage (GCS)
- Google Big Query (BQ)
- Discovery Service (we use this to download the service definitions for our generated code)
- Prediction API


## How this project is set up:

This is how we build the wrappers that you can use. 

- you can download service descriptions with: [discovery.py](https://github.com/transceptor-technology/txGoogle/blob/master/txGoogle/wrappers/discovery.py)
- you can generate the service file. This is stored in [txGoogle/services](https://github.com/transceptor-technology/txGoogle/tree/master/txGoogle/services) with: [asyncApisGenerator.py](https://github.com/transceptor-technology/txGoogle/blob/master/txGoogle/asyncApisGenerator.py)
- then it's time to build a wrapper for the service. Google provides nice api calls but most likely you want it to be just a bit more than that. Wrappers are stored in [txGoogle/wrappers](https://github.com/transceptor-technology/txGoogle/tree/master/txGoogle/wrappers)



## setting up a connection:

```python
import sys
from twisted.python import log
from twisted.internet import reactor
from txGoogle.sharedConnection import SharedConnection
from txGoogle.wrappers.storage import StorageWrapper
from txGoogle.wrappers.bigQuery import BigQueryWrapper

log.startLogging(sys.stdout) # We try not to use print statements.

# First create a shared connection
# clientId, clientSecret, fileNameToStoreTokens
conn = SharedConnection('XXXXX.apps.googleusercontent.com', 'XXXXXX', 'myCredentials.json')

# instanciate the wrappers we want to use.
# they will register their scopes on the shared connection
gcs = StorageWrapper(conn) 
bq = BigQueryWrapper(conn) 

# connect 
dfd = conn.connect() 

reactor.run()
```
This will open up a browser asking for the authorisation scopes that are required


## BQ:

This is the usecase where it all started: http://stackoverflow.com/questions/23810923/google-cloud-big-queries-cost-big-memory
Furthermore I was using deferToThread to use the google api's. I wanted to use the json api and go full async

Nice features:
 - Records will be returned in list of lists is stead of the bulky json format Google uses. And they are converted to the corresponding python values
 - csv support is possible but not yet fully develloped (this should allow for quicker requests)
 - implemented rename table (does copy and delete under the hood)
 - handles pagination out of the box. So even if you have thousands of tables and you do tables.list you will get called back when all the results are in.
 - lower memory footprint than the original library because we avoid json.loading the rows. In stead we use line-splitting since the format doesn't change.


```python
from txGoogle.sharedConnection import SharedConnection
from txGoogle.asyncUtils import printCb
from twisted.internet import reactor
conn = SharedConnection('XXXXX.apps.googleusercontent.com', 'XXXXXX', 'myCredentials.json')
abq = BigQueryWrapper(conn)
conn.connect()

dfd = abq.jobs.query(projectId=projectId, datasetId='samples', query='SELECT * FROM [publicdata:samples.shakespeare]')
dfd.addCallback(printCb)
```

result

```json
[
  [
    "brave", 
    6, 
    "titusandronicus", 
    1593
  ], 
  [
    "fealty", 
    1, 
    "titusandronicus", 
    1593
  ], 
  [
    "dimm'd", 
    1, 
    "titusandronicus", 
    1593
  ],
  ...
]
```

## GCD:

Nice features we've built:

- Serialisation and de-serialisation from and to objects in python

Example to delete entities by key:

```python
from txGoogle.wrappers.datastore import DatastoreWrapper
from txGoogle.sharedConnection import SharedConnection
from twisted.internet import reactor
from txGoogle.wrappers.gcd import setGlobalGcdServiceAndProjectId

conn = SharedConnection('XXXXX.apps.googleusercontent.com', 'XXXXXX', 'myCredentials.json')
gcd = DatastoreWrapper(conn)
conn.connect()
setGlobalGcdServiceAndProjectId(gcd, 'projectId') #this is used in batch operations. 

def onEntitiesToRemove(entities):
  for entity in entities:
      self.gcd.batchOperations.delete(entity.key) # gcd allows for max 500 entities per "commit" so we batch them up
        
dfd = gcd.datasets.query(datasetId='over-sight', kinds=['Sample'], properties=['__key__'], limit=5000)
dfd.addCallback(onEntitiesToRemove)

reactor.run()
  
```


## GCS:

I've used the follwing script to bulk-delete thousands of files. Please be carefull when using @inlineCallbacks. If an exception raises, you might not know it. 


```python
from twisted.internet.defer import inlineCallbacks
from txGoogle.asyncUtils import waitTime
from txGoogle.asyncUtils import ignoreFirstArg
from twisted.internet import reactor
#setup connection where  dfd = conn.connect()


def extractFileNames(res):
    files = res['items']
    print len(files)
    return [fileItem['name'] for fileItem in files]


@inlineCallbacks
def cleanup(bucket, folder):
    res = yield gcs.objects.list(bucket=bucket, prefix=folder, maxResults=10000)
    files = extractFileNames(res)
    while files:
        for fileName in files:
            print fileName
            gcs.objects.delete(fileName, bucket=bucket)
        wait = yield gcs._conn.waitForEmptyQueue()
        res = yield gcs.objects.list(bucket=bucket, prefix=folder, maxResults=10000)
        files = extractFileNames(res)
        print 'DoneBatch'

log.startLogging(sys.stdout)
dfd.addCallback(ignoreFirstArg, cleanup, 'BUCKET_NAME', 'FOLDER_NAME')
reactor.run()
```
