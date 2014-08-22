'''
Created on 22 aug. 2014

@author: sjuul
'''
from txGoogle.request import Request


class GoogleServiceRequest(Request):

    def __init__(self, *args, **kwargs):
        super(GoogleServiceRequest, self).__init__(*args, **kwargs)
        self.setAcceptGzip()
