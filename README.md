txGoogle
========

Twisted implementations of Google JSON API's

The main reasons for building this library:
- we wanted to use twisted (if you don't this library might not be for you)
- pythons httplib is not thread safe and googles library is built on top of httplib
- we wanted to have autocompletion in eclipse 
- googles api for python generates code but it wasn't inspectable by reading files.
- usign boto is not straight forward.


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
 - Records will be returned in list of lists in stead of the bulky json format Google uses. And they are converted to the corresponding python values
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
- Uses the same method to make urlSafe string representation as App Engine. This allows for interop with AE
- Entities can be constructed by:
 - Giving the serialised json representation that the JSON api uses
 - Giving a python dict and a key. This allows for a smaller transport format than the JSON api uses. Please note some data will get lost:
  - which properties are indexed
  - types are deducted from their json representation
- Keys can be constructed by:
 - Giving the serialised json representation that the JSON api uses
 - Giving key pairs just like in NDB `Key('Parent', 'Dad', 'Person', 'Bob')`
 - Giving the urlsafe string `Key('urlsafeStringHere')`
- A small ORM is included which allows for App Engine like models. This feature is quite new so expect changes to happen here
- Aggregating entities to be updated in one single batch is possible. Example: `gcd.batchOperations.upsert(entity, 60)` will make sure the entity is saved within 60 seconds. If other entities are saved as well they will be saved in `commit`s of 500 entities. This way you don't have to worry about making commits that are to large for GCD

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
        
dfd = gcd.datasets.query(datasetId='DATA_SET_ID', kinds=['Sample'], properties=['__key__'], limit=5000)
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

## Gmail

The gmail wrapper contains the following method so that you don't have to build it:

```python
def sendMail(self, fromAddress, toAddress, subject, body, cc=None, bcc=None, userId=None):
  if userId is None:
   userId = fromAddress
  message = MIMEText(body)
  message['to'] = ', '.join(toAddress)
  message['from'] = fromAddress
  message['subject'] = subject
  if cc is not None:
   message['cc'] = cc
  if bcc is not None:
   message['bcc'] = bcc
  raw = base64.urlsafe_b64encode(message.as_string())
  print raw
  return self.users.messages.send(userId=userId, raw=raw)
```

Sending mail should be as simple as:

```python
dfd = gmail.sendMail('from@somewhere.com', ['to1@somewhere.com', 'to2@somewhere.com'], 'test', 'This is a test')
```
