import json

test = """ {
    "name": "Son",
    "age" : 25,
    "id" : 1
    }"""

j_test = json.loads(test)
print(j_test)


test ={
    "name": "Son",
    "age" : 25,
    "id" : 1
    }

j_test = json.dumps(test,indent=4)

print(j_test)
