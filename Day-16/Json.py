import json 

print("------------------------ 1. COnvert JSON strings to python objects ----------------------")
people_string = '''
{
"people":[
    {
        "name": "Rachana Mahesh",
        "phone": "786-456-7321",
        "email": ["rachana.m@gmail.com","rtest@gmail.com"],
        "has_license": false
    },
    {
        "name": "Madhu Mahesh",
        "phone": "732-456-7321",
        "email": null,
        "has_license": true 
    }
]
}
'''
# # NOTE: True is not a JSON value so it will throw an error actual json boolean values are true & false
# # Json.loads : to load a Json string

# data = json.loads(people_string)
# print(data)
# print(type(data))

# # JSON to Python convertion table
# # JSON   - Python
# # object - dict
# # array - list
# # string - str
# # number (int) - int
# # number (real) - float
# # true - True
# # false - False
# # null - None

# print(type(data['people']))
# for person in data['people']:
#     print(person)

# for person in data['people']:
#     print(person['name'])

## json.dumps : to dump a python object into Json string for eg: lets delete a phonenumber and dump it to json string as below

# for person in data['people']:
#     del person['phone']

## new_string = json.dumps(data)
# new_string = json.dumps(data, indent = 2, sort_keys=True) # to format it which is easy to read via indent attribute & sort_keys is used to sort
# print(new_string)

print("-------------------- 2. To load JSON file to python objects & vice versa----------------- ")
# import os
# cwd = os.getcwd()
# os.chdir("C:/Users/User/FY25/Python/30-Days-Python-Challenge/Day-16")
# # print(os.getcwd())

# with open("States.json") as f:
#     data = json.load(f)

# # print(data['states'])
# for state in data['states']:
#     print(state['name'],state['abbreviation'])

# ## dump : to load data into json file & dumps : to load data into json string
# for state in data['states']:
#     del state['area_codes']

# with open("New_string.json",'w') as f :
#     json.dump(data,f,indent=2)

# os.chdir(cwd)

