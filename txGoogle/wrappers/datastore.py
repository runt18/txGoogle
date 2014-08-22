'''
Created on 21 aug. 2014

@author: sjuul
'''
from txGoogle.services.datastore_ import Datastore


class DatastoreWrapper(Datastore):
    pass

if __name__ == '__main__':
    conn = DatastoreWrapper('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/GcdCredentials.json')
    gcd = DatastoreWrapper(conn)
    conn.connect()
    gcd.datasets.runQuery()
