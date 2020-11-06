import requests


def generate_scanid(fileName , filePath):

    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': '0020bc9918f925ee89e0ab9e001e4b69cac3cc711554d5207fba422157ece78c'}

    files = {'file': (fileName, open(filePath, 'rb'))}

    response = requests.post(url, files=files, params=params)
    print(response.json())
