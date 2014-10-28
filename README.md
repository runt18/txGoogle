txGoogle
========

Twisted implementations of Google JSON API's

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
