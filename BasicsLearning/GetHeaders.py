from urllib import response
import requests

#Adding Headers
# headerdata ={'H1':'Header1', 'H2': 'Header2'}
# response = requests.get('https://httpbin.org/get', headers=headerdata)
# print(response.text)

#Adding Parameters
param  ={'name':'MyName', 'email': 'MyEmail', 'number':'3535'}
response = requests.get('https://httpbin.org/get', params=param)
print(response.text)