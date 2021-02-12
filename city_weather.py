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

def city_weather():
    city_name="Fergana"
    api_key='1b4ba2abbe57cb51a299f2a1c620f80b'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    res=requests.get(url)
    data=res.json()
    
