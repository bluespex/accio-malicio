#Getting a list of all the files in the present directory
path = pathlib.Path().absolute()

files = os.listdir(path)


#Calculating the hash for each file in the current directory
for filename in files:

    # print(filename)

    if filename != "PIYUSH_CV (1).pdf":
        continue

    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': '0020bc9918f925ee89e0ab9e001e4b69cac3cc711554d5207fba422157ece78c'}

    files = {'file': (filename, open(filename, 'rb'))}

    response = requests.post(url, files=files, params=params)

    print(response.json())
    ID = response.json()['scan_id']

    prev_time = time.perf_counter()
    cur_time = prev_time
    while cur_time - prev_time <= 20.0:
        cur_time = time.perf_counter()

    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    params = {'apikey': '0020bc9918f925ee89e0ab9e001e4b69cac3cc711554d5207fba422157ece78c', 'resource':"4d6f31698ea75b74e6464aa6bc409d00b8831fe140e029ac571b7cc394755d2c-1604664826"}

    response = requests.get(url, params=params)

    print(response.json())



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
