'''
Created on 15 aug. 2014

@author: sjuul
'''

from txGoogle.services.gmail_ import Gmail

from email.mime.text import MIMEText
import base64
from txGoogle.asyncUtils import printCb
from txGoogle.sharedConnection import SharedConnection


class GmailWrapper(Gmail):

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


if __name__ == '__main__':
    from twisted.internet import reactor
    conn = SharedConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/AsyncAllCredentials.json')
    gmail = GmailWrapper(conn)
    conn.connect()
    for i in range(1):
        dfd = gmail.sendMail('sjuul.janssen@transceptor-technology.com', ['sjuulj@hotmail.com'], 'test', 'Dit is een test {}'.format(i))  #; sjanssen@insign.it
        dfd.addCallback(printCb)
    reactor.run()
