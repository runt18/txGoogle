'''
Created on 15 aug. 2014

@author: sjuul
'''

from txGoogle.services.gmail import Gmail
from txGoogle.asyncBase import AsyncBase
from email.mime.text import MIMEText
import base64


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
        return self.messages.send(userId=userId, raw=raw)


if __name__ == '__main__':
    from twisted.internet import reactor
    conn = AsyncBase('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/AsyncAllCredentials.json')
    gmail = GmailWrapper(conn)
    conn.connect()
    gmail.sendMail('sjuul.janssen@transceptor-technology.com', 'sjanssen@insign.it', 'test', 'Dit is een test')
    reactor.run()