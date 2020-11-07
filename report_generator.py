import requests
import os
import json


def generate_report(Id):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    params = {'apikey': '0020bc9918f925ee89e0ab9e001e4b69cac3cc711554d5207fba422157ece78c', 'resource':Id}

    response = requests.get(url, params=params)

    # print(response.json())
    
    with open(os.path.join(os.getcwd() , 'db.json'), 'w') as outfile:
        json.dump(response.json(), outfile)

def generate_hash_report(Id):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    params = {'apikey': '0020bc9918f925ee89e0ab9e001e4b69cac3cc711554d5207fba422157ece78c', 'resource':Id}

    response = requests.get(url, params=params)

    # print(response.json())

    with open(os.path.join(os.getcwd() , 'hashdb.json'), 'r') as outfile:
        data = json.load(outfile)

    data.update(response.json())

    with open(os.path.join(os.getcwd() , 'hashdb.json'), 'w') as outfile:
        json.dump(data, outfile)

