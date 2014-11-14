'''
Created on 15 aug. 2014

@author: sjuul
'''

from txGoogle.services.gmail_ import Gmail

from email.mime.text import MIMEText
import base64
from txGoogle.asyncUtils import printCb
from txGoogle.singleton import Singleton


class GmailWrapper(Gmail):

    def sendMail(self, fromAddress, toAddresses, subject, body, cc=None, bcc=None, userId=None):
        if userId is None:
            userId = fromAddress
        if not isinstance(toAddresses, list):
            toAddresses = [toAddresses]
        message = MIMEText(body)
        message['to'] = ','.join(toAddresses)
        message['from'] = fromAddress
        message['subject'] = subject
        if cc is not None:
            message['cc'] = cc
        if bcc is not None:
            message['bcc'] = bcc
        raw = base64.urlsafe_b64encode(message.as_string())
        print raw
        return self.users.messages.send(userId=userId, raw=raw)


class GmailSingleton(GmailWrapper):

    __metaclass__ = Singleton


if __name__ == '__main__':
    from txGoogle.sharedOauthConnection import SharedOauthConnection
    from twisted.internet import reactor
    conn = SharedOauthConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/AsyncAllCredentials.json')
    gmail = GmailWrapper(conn)
    conn.connect()
    for i in range(1):
        dfd = gmail.sendMail('sjuul.janssen@transceptor-technology.com', ['sjuulj@hotmail.com', 'sjanssen@insign.it'], 'test', 'Dit is een test {}'.format(i))  #; sjanssen@insign.it
        dfd.addCallback(printCb)
    reactor.run()
