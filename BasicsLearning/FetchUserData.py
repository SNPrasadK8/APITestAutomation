import requests
import json
import  jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"
 
#Send Get Request
response = requests.get(url)
 
#Validate Status code 
assert response.status_code == 200

#Fetch Response Content and Header
# print(response.content)
print(response.headers)

#Fetch Specific Header  ----GET Request----
print(response.headers.get('Date'))
print(response.headers.get('Server'))

#Fetch coockies
print(response.cookies)

#Fetch Encoding
print(response.encoding)

#Fetch Elapsed  - time taken for request and response 
print(response.elapsed)

# Parse response to Json format
json_response = json.loads(response.text)
# print(json_response)

#Fetch Values using jsonpath
pages = jsonpath.jsonpath(json_response, 'total_pages')
assert pages[0] == 2

# first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
# print(first_name[0])

#Fetch all the first names
for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0])
