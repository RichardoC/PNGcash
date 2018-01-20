# /usr/bin/env python

from twilio.rest import Client
import json
import getpass
from random import randint
from bcrypt import hashpw, gensalt


class SMSClient(object):
    def __init__(self, sid):
        self.account_sid = sid
        self.token = None
        self.client = None
        self.__createClient()

    def __createClient(self):
        print 'Enter token:'
        self.token = getpass.getpass()
        self.client = Client(self.account_sid, self.token)

    def sendSMS(self, sender, receiver, message):
        self.client.api.account.messages.create(to=receiver,
                                                from_=sender,
                                                body=message)


def main():
    account_sid = 'AC827a7a78896b9789c9c2c1c599d40adb'
    smsc = SMSClient(account_sid)
    me = raw_input('Enter number to send to:\n')
    twil_num = raw_input('Enter sender number:\n')
    body = 'Hello there!'
    smsc.sendSMS(twil_num, me, body)


if __name__ == "__main__":
    main()
