import json
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

def get_resource(id=None):
    emp_data={
        'id':id,
    }
    rp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(emp_data))
    print("Status Code:",rp.status_code)
    print("*"*100)
    print(rp.json())
    print("*"*100)

def post_resource():
    emp_data={
        'ename':'Bunny',
        'eaddr':'Mumbai',
        'esal' :1000,
        'eno'  :1002
    }
    rp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(emp_data))
    print("Status Code:",rp.status_code)
    print("*"*100)
    print(rp.json())
    print("*"*100)

def put_resource():
    emp_data={
        'id':2,
        'ename':'Ganesh',
        'eaddr':'Hyderabad',
        'esal':4000
    }
    rp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(emp_data))
    print("Status Code:",rp.status_code)
    print("*"*100)
    print(rp.json())
    print("*"*100)

def delete_resource():
    emp_data={
        'id':1,
    }
    rp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(emp_data))
    print("Status Code:",rp.status_code)
    print("*"*100)
    print(rp.json())
    print("*"*100)


put_resource()