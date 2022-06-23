import requests

#API Url
url = "https://reqres.in/api/users?page=2"

#Delete User
response = requests.delete(url)

#Fetch Status Code
print(response.status_code)

assert response.status_code == 204