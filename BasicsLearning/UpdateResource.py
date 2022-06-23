import requests
import json
import jsonpath
#API Url
url = "https://reqres.in/api/users/2"

file = open('C:\\SNP\\PyTestUdemy\\BasicsLearning\\CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT request with Json Input body
response = requests.put(url, request_json)
print(response.content)

# Validating Response Code
assert response.status_code == 200

#Parse Response to Json Format
response_json = json.loads(response.text)


updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])