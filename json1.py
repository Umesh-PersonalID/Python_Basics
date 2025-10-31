import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


#covert dictionary to JSON
person_json = json.dumps(person)
print(person_json)




#convert JSON to dictionary
person_dict = json.loads(person_json)
print(person_dict)