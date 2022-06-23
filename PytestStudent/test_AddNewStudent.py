import pytest
import requests
import json
import jsonpath

def test_add_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/SNP/PyTestUdemy/PytestStudent/RequestJason.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request, verify= False)
    print(response.text)

# def test_get_student_data():
#     API_URL = "http://thetestingworldapi.com/api/studentsDetails/2673801"
#     response = requests.get(API_URL, verify= False)
#     # json_response = json.loads(response.text)
#     json_response = response.json()
#     id = jsonpath.jsonpath(json_response, 'data.id')
#     assert id[0] == 2673801
#     print(response.text)

# def test_update_student_data():
#     API_URL = "http://thetestingworldapi.com/api/studentsDetails/2673801"
#     f = open('C:/SNP/PyTestUdemy/PytestStudent/RequestJason.json', 'r')
#     json_request = json.loads(f.read())
#     response = requests.put(API_URL, json_request, verify= False)
#     print(response.text)

# def test_delete_student_data():
#     API_URL = "http://thetestingworldapi.com/api/studentsDetails/2673801"
#     response = requests.delete(API_URL, verify = False)
#     print(response.text)

# def test_get_student_data():
#     API_URL = "https://thetestingworldapi.com/api/studentsDetails"
#     response = requests.get(API_URL, verify= False)
#     # json_response = response.json()
#     print(response.text)
