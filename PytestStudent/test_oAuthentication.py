import requests
import json
import jsonpath
import ssl
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from time import sleep
import time
def test_oauth_api():

    ssl._create_default_https_context = ssl._create_unverified_context

    token_url = "https://cat-fact.herokuapp.com/facts"
    data = {'grant_type':'password', 'username':'snprasadk8', 'password':'Sathya@1github'}
    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')
    auth={'Autherization':'Bearer'+token_value[0]}

    Api_url = 'https://cat-fact.herokuapp.com/facts/110'
    response = requests.get(Api_url, headers=auth)
    print(response.text)
    
