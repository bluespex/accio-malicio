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


email_user = "p4firebase@gmail.com"
email_pass = "pppp15192902"

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

            generate_scanid(fileName , filePath)

            generate_report('afsd')
            

            

