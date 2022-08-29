import requests
from requests.auth import HTTPBasicAuth

def test_withauthentication():
    # git_token = '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'

    response  = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('SNPrasadK8', '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'))
    print(response.text)
