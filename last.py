import requests
import json
from pprint import pprint
import os

token=os.environ["TOKEN"]

def getUpdates():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url)
    updates=res.json()["result"]
    return updates

def last():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url)
    updates=res.json()["result"]
    return updates[-1]



