import json
def is_json(json_data):
    try:
        pdata=json.loads(json_data)
        valid=True
    except:
        valid=False
    return valid

def object_id(id):
    try:
        emp=Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        emp=None
    return emp