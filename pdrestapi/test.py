import json
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='srl/'

#partner application function to get single resource
def get_resource(id=None):
    emp_data={
        'id':id,
    }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(emp_data))
    print(resp.status_code)
    print(resp.json())

def post_resource():
    emp_data={
        'ename':'Bunny',
        'eaddr':'Mumbai',
        'esal' :1000,
        'eno'  :1002
    }
    json_data=json.dumps(emp_data)
    resp=requests.post(BASE_URL+ENDPOINT,data=json_data)
    print(resp.status_code)
    print(resp.json())

def put_resource():
    emp_data={
        'id':1,
        'ename':'Ganesh',
        'esal' :12000,
        
    }
    json_data=json.dumps(emp_data)
    resp=requests.put(BASE_URL+ENDPOINT,data=json_data)
    print(resp.status_code)
    print(resp.json())

def delete_resource(id):
    emp_data={
        'id':id,
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(emp_data))
    print(resp.status_code)
    print(resp.json())


get_resource()