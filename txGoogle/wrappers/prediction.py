import os
from txGoogle.utils import preparePathForFile
from txGoogle.services.prediction_ import Prediction
import json
import numpy as np
import pylab as pl
import datetime


class PredictionWrapper(Prediction):

    def __init__(self, conn=None, scopes=None, projectId=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(PredictionWrapper, self).__init__(conn, *args, **kwargs)
        self.projectId = projectId
        
    def testXOR(self):
        dataXORTest = [{'csvInstance': [0,0], 'output': 0},
                       {'csvInstance': [0,1], 'output': 1},
                       {'csvInstance': [1,0], 'output': 1},
                       {'csvInstance': [1,1], 'output': 0},
                       ]*2
                       
        dfds = []
        #dfds.append(self.trainedmodels.delete(project=projectId, id='xorClassifier'))
        #dfds.append(self.trainedmodels.insert(project=projectId, id='xorClassifier', modelType='CLASSIFICATION', trainingInstances=dataXORTest))
        #dfds.append(self.trainedmodels.get(project=projectId, id='xorClassifier'))
        dfds.append(self.trainedmodels.predict(project=projectId, id='xorClassifier', input={'csvInstance': [0,1]}))
        
        #dfds.append(self.trainedmodels.delete(project=projectId, id='xorRegressor'))
        #dfds.append(self.trainedmodels.insert(project=projectId, id='xorRegressor', modelType='REGRESSION', trainingInstances=dataXORTest))
        #dfds.append(self.trainedmodels.get(project=projectId, id='xorRegressor'))
        dfds.append(self.trainedmodels.predict(project=projectId, id='xorRegressor', input={'csvInstance': [0,1]}))
        return dfds
    
    def testLinear(self):
        dataLinearTest = [{'csvInstance': [0.], 'output': 0.},
                          {'csvInstance': [1.], 'output': 2.},
                          {'csvInstance': [2.], 'output': 4.},
                          {'csvInstance': [3.], 'output': 6.},
                          {'csvInstance': [4.], 'output': 8.},
                          {'csvInstance': [5.], 'output': 10.},
                          {'csvInstance': [6.], 'output': 12.},
                          {'csvInstance': [7.], 'output': 14.},
                          ]
        dfds = []
        #dfds.append(self.trainedmodels.delete(project=projectId, id='linearTest'))
        #dfds.append(self.trainedmodels.insert(project=projectId, id='linearTest', modelType='REGRESSION', trainingInstances=dataLinearTest))
        dfds.append(self.trainedmodels.get(project=projectId, id='linearTest'))
        dfds.append(self.trainedmodels.predict(project=projectId, id='linearTest', input={'csvInstance': [8]}))
        return dfds
    
    def createRegressionModel(self, modelName, dataTrain):
            
        dfds = []
        #dfds.append(self.trainedmodels.delete(project=self.projectId, id=modelName))
        dfds.append(self.trainedmodels.insert(project=self.projectId, id=modelName, modelType='REGRESSION', trainingInstances=dataTrain))
        #dfds.append(self.trainedmodels.analyze(project=projectId, id=modelName))
        #dfds.append(self.trainedmodels.get(project=self.projectId, id=modelName))
        #dfds.append(self.trainedmodels.predict(project=self.projectId, id=modelName, input={'csvInstance': [0]}))
        #dfds.append(self.trainedmodels.predict(project=self.projectId, id=modelName, input={'csvInstance': [5]}))
        return dfds


def testPatTraindata():
    pat = (([0]*4+[10]*4+[0]*4)*5+[0]*24)*4+np.random.randn(84*4)
    tv = zip([a%84 for a in xrange(84*4)], pat)

    dataTrain = []        
    for t, v in tv:
        dataTrain.append({'csvInstance': [t], 'output': v})
    return dataTrain


if __name__ == '__main__':
    from txGoogle.sharedConnection import SharedConnection
    from txGoogle.asyncUtils import printCb
    from twisted.internet import reactor

    projectId = 'detect-analyze-notify-01a'
    
    conn = SharedConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/GcdCredentials.json')
    pred = PredictionWrapper(conn=conn, projectId='detect-analyze-notify-01a')
    conn.connect()
    
    #dfd = pred.hostedmodels.predict(project='414649711441', hostedModelName='sample.languageid', input={'csvInstance': ['je suis suis un baguette']})
    #dfd = pred.trainedmodels.predict(project=projectId, id='languageClassifier', input={'csvInstance': ['je suis suis un baguette']})
    
    #dfds = pred.testLinear()
    dataTrain = open('/home/koos/Bureaublad/regrTrainData.json')
    dfds = pred.createRegressionModel('regrModel', dataTrain)
    
    for dfd in dfds:
        def onData(data):
            try:
                print json.dumps(data, indent=2)
            except:
                print data
        
        dfd.addCallback(onData)
        dfd.addErrback(printCb)
    
    reactor.run()
