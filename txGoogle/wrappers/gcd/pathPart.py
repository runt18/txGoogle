'''
Created on Oct 21, 2014

@author: sjuul
'''


class PathPart(object):

    def __init__(self, kind, name=None, id=None):
        self.kind = kind
        self.name = name
        if id:
            id = long(id)
        self.id = id

    def serialize(self):
        if self.name is None:
            return {'kind': self.kind, 'id': str(self.id)}
        else:
            return {'kind': self.kind, 'name': self.name}

    def nameId(self):
        if self.name:
            return self.name
        else:
            return self.id

    def __repr__(self):
        try:
            if self.name is None:
                return "('{}', {})".format(self.kind, self.id)
            else:
                return "('{}', '{}')".format(self.kind, self.name)
        except:
            return 'KEY?'

    def __eq__(self, other):
        return self.kind == other.kind and self.id == other.id and self.name == other.name
