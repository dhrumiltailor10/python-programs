import json

#json data in similar to python dictionary format
data = '''{
    "name" : "dhrumil",
    "age"  : "24"

}'''

# json data similar to python table/array format (dictionary nested inside a table)
data1 = '''[
    {
        "name" : "dhrumil",
        "rollno" : "10"
    },
    {
        "name" : "dhruv",
        "rollno" : "7" 
    }
]'''

info = json.loads(data)
print('Name : ', info["name"])
print('Age:', info["age"])

info1 = json.loads(data1)
for item in info1:
    print("Name:", item["name"])
    print("rollno:",item["rollno"])