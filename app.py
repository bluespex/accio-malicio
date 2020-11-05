import imaplib
import base64
import os
import email
import hashlib
import pathlib


email_user = "p4firebase@gmail.com"
email_pass = "pppp15192902"

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)

mail.login(email_user, email_pass)

mail.select('Inbox')

ok, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()


for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    # msg = email_message
    # email_subject = msg['subject']
    # email_from = msg['from']
    # print ('From : ' + email_from + '\n')
    # print ('Subject : ' + email_subject + '\n')
    # print(msg.get_payload(decode=True))
# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join(os.getcwd(), fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            print(subject)



#Getting a list of all the files in the present directory
path = pathlib.Path().absolute()

files = os.listdir(path)


#Calculating the hash for each file in the current directory
for filename in files:

    print(filename)

    #sha256 hash
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        print('sha256: '+sha256_hash.hexdigest())

    #sha1 hash
    sha1_hash = hashlib.sha1()
    with open(filename,'rb') as f:
        # Read and update hash string value in blocks of 1K
        for byte_block in iter(lambda: f.read(1024),b""):
            sha1_hash.update(byte_block)
        print('sha1:   '+sha1_hash.hexdigest())

    #md5 hash
    md5_hash = hashlib.md5()
    with open(filename,'rb') as f:
        # Read and update hash string value in blocks of 8K
        for byte_block in iter(lambda: f.read(8192),b""):
            md5_hash.update(byte_block)
        print('md5:    '+md5_hash.hexdigest())


    print('\n')
