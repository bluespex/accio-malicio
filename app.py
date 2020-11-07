import imaplib
import base64
import os
import email
import hashlib
import pathlib
import requests
import time
from report_generator import generate_report
from generate_scanId import generate_scanid
from hash_analyzer import hash_analyzer

import sys
from regex import regex_matching

print(sys.argv[1] , sys.argv[2])

email_user = sys.argv[1]
email_pass = sys.argv[2]

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)

mail.login(email_user, email_pass)

temp = ''
while True:
    mail.select('Inbox')
    ok, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    arr = data[0].split()

    ele = arr[len(arr) - 1]
    typ, data = mail.fetch(ele, '(RFC822)' )
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    if temp == raw_email_string:
        continue
    temp = raw_email_string
    print('********************************************************************')
    email_message = email.message_from_string(raw_email_string)

    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
    print(subject)
# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet... 
        
        if part.get_content_type() == "text/plain":
            email_body = part.get_payload(decode=True)
            print (email_body)
            regex_matching(email_body)
            
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        

        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join(os.getcwd() , 'attachment')
            filePath = os.path.join(filePath, fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

            # @app.route('/')
            # def home():
            #     return filename
            hash_analyzer(filePath)
            # generate_scanid(fileName , filePath)

            # generate_report('9849e33e978278070075328520663c618f05d02aad5f1fc802c68af354d44ab1-1604758068')
            