import pytest
import requests
import json
import jsonpath

# def test_add_student_data():
#     API_URL = "https://thetestingworldapi.com/api/studentsDetails"
#     f = open('C:/SNP/PyTestUdemy/PytestStudent/RequestJson.json', 'r')
#     json_request = json.loads(f.read())
#     response = requests.post(API_URL, json_request)
#     print(response.text)

# def test_update_student_data():
#     API_URL = "https://thetestingworldapi.com/api/studentsDetails/2676768"
#     f = open('C:/SNP/PyTestUdemy/PytestStudent/RequestJson.json', 'r')
#     json_request = json.loads(f.read())
#     response = requests.put(API_URL, json_request)
#     print(response.text)

# def test_get_student_data():
#     API_URL = "https://thetestingworldapi.com/api/studentsDetails/2676768"
#     response = requests.get(API_URL)
#     # json_response = json.loads(response.text)
#     json_response = response.json()
#     id = jsonpath.jsonpath(json_response, 'data.id')
#     assert id[0] ==2676768
#     print(response.text)



# def test_delete_student_data():
#     API_URL = "https://thetestingworldapi.com/api/studentsDetails/2676768"
#     response = requests.delete(API_URL)
#     print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/2676768"
    response = requests.get(API_URL)
    json_response = response.json()
    print(json_response)
