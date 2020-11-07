import re
from report_generator import generate_hash_report


api_key = '602847a20a2ed4126b2211794a52efb30638c6d759fb5a1d39d2c8c923b974af'

def regex_matching(email_body):

    email_body = str(email_body)
    # Regular Expression to select the 32 character long hexadecimal string (MD5 Hash)
    md5 = re.findall(r'\b[0-9a-fA-F]{32}\b', email_body)
    print(md5)
    for hashes in md5:
        print(hashes)
        if hashes != '':
            generate_hash_report(hashes)


    # Regular Expression to select the 40 character long hexadecimal string (sha-1 Hash)
    sha1 = re.findall(r'\b[0-9a-fA-F]{40}\b', email_body)
    # print(sha1)
    for hashes in sha1:
        print(hashes)
        if hashes != '':
            generate_hash_report(hashes)

    # Regular Expression to select the 64 character long hexadecimal string (sha-256 Hash)
    sha256 = re.findall(r'\b[0-9a-fA-F]{64}\b', email_body)
    # print(sha256)
    for hashes in sha256:
        print(hashes)
        if hashes != '':
            generate_hash_report(hashes)

    # A regular expression to get any URL help within the body of the email
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email_body)
    # print(url)


