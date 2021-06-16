import requests
import json

url = 'http://127.0.0.1:8000/dataExchange/androidData/'


def parseJson(content):
    stuff = str(content.content,'utf-8')
    contentAsJson = json.loads(stuff)
    return contentAsJson


mysession = requests.session()
response = mysession.get(url)

print(parseJson(response))


payload = { 'spot1' : 'E' ,'spot2' : 'E'  ,'spot3' : 'F'}
postResponse = mysession.post(url, data = payload)

print(parseJson(postResponse))