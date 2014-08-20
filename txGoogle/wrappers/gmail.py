'''
Created on 15 aug. 2014

@author: sjuul
'''

from txGoogle.services.gmail_ import Gmail
from txGoogle.asyncBase import AsyncBase
from email.mime.text import MIMEText
import base64
from txGoogle.asyncUtils import printCb


class GmailWrapper(Gmail):

    def sendMail(self, fromAddress, toAddress, subject, body, cc=None, bcc=None, userId=None):
        if userId is None:
            userId = fromAddress
        message = MIMEText(body)
        message['to'] = toAddress
        message['from'] = fromAddress
        message['subject'] = subject
        if cc is not None:
            message['cc'] = cc
        if bcc is not None:
            message['bcc'] = bcc
        raw = base64.urlsafe_b64encode(message.as_string())
        return self.users.messages.send(userId=userId, raw=raw)


if __name__ == '__main__':
    from twisted.internet import reactor
    conn = AsyncBase('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/AsyncAllCredentials.json')
    gmail = GmailWrapper(conn)
    conn.connect()
    for i in range(1):
        dfd = gmail.sendMail('sjuul.janssen@transceptor-technology.com', 'sjanssen@insign.it', 'test', 'Dit is een test {}'.format(i))
        dfd.addCallback(printCb)
    reactor.run()
