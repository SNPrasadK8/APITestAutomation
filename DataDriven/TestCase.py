import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_multiple():

    App_Url ="http://localhost:3000/studentDetails"
    f = open('C:/SNP/PyTestUdemy/PytestStudent/RequestJason.json')
    json_request = json.loads(f.read())

    obj = Library.Common('C:/SNP/PyTestUdemy/PytestStudent/Book1.xlsx', 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    
    for i in range(2, row+1):
       
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(App_Url, updated_json_request)
        print(response)