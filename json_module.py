import json
#string(json to py)
json_obj='{"name":"Ankit", "isStudent": true, "back":null}'
py_obj=json.loads(json_obj)
print(py_obj)
#string(py to json)
json_obj1=json.dumps(py_obj)
print(json_obj1)