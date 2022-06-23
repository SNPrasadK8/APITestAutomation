import requests
import json
import jsonpath

def test_Add_new_data():
    App_Url ="http://localhost:3000/studentDetails"
    f = open('C:/SNP/PyTestUdemy/PytestStudent/RequestJason.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(App_Url, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    
    tech_api_url = "http://localhost:3000/technicalskills"
    f = open('C:/SNP/PyTestUdemy/PytestStudent/TechnicalUpdate.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    add_api_url = "http://localhost:3000/address"
    f = open('C:/SNP/PyTestUdemy/PytestStudent/AddressUpdate.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(add_api_url, request_json)
    print(response.text)


# unable to find
    # final_details = "http://localhost:3000/CompleteDetail/1"
    # response = requests.get(final_details)
    # print(response.text)