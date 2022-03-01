import json

# JSON TO PYOBJ
test = """ {
    "name": "Son",
    "age" : 25,
    "id" : 1
    }"""

j_test = json.loads(test)
print(j_test)

# PYOBJ TO  JSON 
test ={
    "name": "Son",
    "age" : 25,
    "id" : 1
    }

j_test = json.dumps(test,indent=4)

print(j_test)


pt_dict = {
    "page" : "marianonilne",
    "followers" : 1000,
    "partners" : None
}
#open("name files","w ?? write "r" ?? read")
with open("pages_info.json","w") as json_flie:
    data = json.dump(pt_dict,json_flie,indent=4)