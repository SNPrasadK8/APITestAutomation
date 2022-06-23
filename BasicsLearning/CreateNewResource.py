import requests
import json
import jsonpath
#API Url
url = "https://reqres.in/api/users?page=2"

file = open('C:\\SNP\\PyTestUdemy\\BasicsLearning\\CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with Json Input body
response = requests.post(url, request_json)
print(response.content)

# Validating Response Code
assert response.status_code == 201

#Fetch header From Response
print(response.headers.get('Content-Length'))

#Parse Response to Json Format
response_json = json.loads(response.text)

# Pick ID Using Json Path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])