'''
Created on 22 aug. 2014

@author: sjuul
'''


class Response(object):

    def __init__(self, contentType, msg, charset=None):
        self.contentType = contentType
        self.msg = msg
        self.charset = charset