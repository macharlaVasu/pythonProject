import json

'''
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# json parse 

y = json.loads(x)
print(y["city"])

#convert into json 
y = json.dumps(x)
print(y)

'''


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x,indent=1)

print(y)
