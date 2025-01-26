tup = (1,2,3,5,1,3)
# dic = {"Name": "Sreenivasulu","Age": 25,"Location":"Bangalore","Mobile":{"MobileNo" : 886767,"HomePhone":7471}}

# print(cnt)
# for i ,j in dic:
#     print(j,end=" ")
# print(dic.get("Name"))


# cnt= 0
# for key,value in dic.items():
#     # print(key,value)
#     if isinstance(value,dict):
#         for i in value:
#             # print(i)
#             cnt += 1
#     else:
#         cnt   += 1
# print(cnt)                


# dic  ={
#     "person1": {"name": "John", "age": 25},
#     "person2": {"name": "Alice", "age": 30},
#     "person3": {"name": "Bob", "age": 22}
#     }

# import json 
# def parse_json(data):
#     if isinstance(data ,dict):
#         for key,values in data.items():
#             print(f"{key} : {values}")
#             if isinstance(values,dict):
#                 parse_json(values)
#             elif isinstance(values,list):
#                 for item in values:
#                     parse_json(item)
#     elif isinstance(data,list):
#         for item in data:
#             parse_json(item)

# nested_json='{"person1": {"name": "John", "age": 25,"phone":[1234,4321]},"person2": {"name": "Alice", "age": 30,"phone":[1234,4321]},"person3": {"name": "Bob", "age": 22,"phone":[1234,4321]}}'
# data1 =json.load(nested_json)
# print(data1)
# #parse_json(data)


'''
22 January 2025 Python Practice


# Abstract  method example 
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("This is Abstract method")
        print("This is implementation method")

ani =Dog()
ani.sound()   
'''

'''  
23 January 2025
'''

# how to delete the duplicate values in list 
'''
list1 = [1,3,2,4,6,2,7,9,10,4]

list2 =list(set(list1))
print(list2)
'''

# how to swap the two number 
'''
a =10 
b=20 

temp=a 
a=b
b=temp
print(a,b,'---After swap ',a,b)

x =12 
y =45
print('before swap ',x,y)
x,y =y,x

print('After swap ',x,y)



# generator yield example 
def generato_fun():
    for i in range(1,5):
        yield i 

gen=generato_fun()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

'''

# Lamda function example 
# add = lambda num : num +4 
# print(add(10))

list1 = [2,5,6,7,9,2,5,10,46,37,87]
odd_nums = [num for num in list1 if num %2 !=0 ]
print('Odd nums :',odd_nums)

print()
#using lamda filter 

even_num = list(filter(lambda num : (num%2 == 0 ),list1))
print('Even numbers: ',even_num)

#using lamda map 

square_list = list(map(lambda num : num **2,even_num))

print()
print('square list: ',square_list)


