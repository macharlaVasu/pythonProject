'''
This is Python Complete pracktice with concept with example 
'''

'''
1. print example

print(1 +2 )

print("Srini's laptop")
print('Srini\'s "laptop"')
print('c:/docs/navin')

a= 10 
b= 10 

print(id(a),'-',id(b))

i =1 
while True:
    if i%3 == 0:
        break
    print(i)
    
    i += 1 
'''
'''
List examples with list methods 

even_list = []
odd_list =[]
for i in range(1,11):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)  

print("Evev List : ",even_list)
print()
print("Odd List  : ",odd_list)


i =1
while i<=5:
    print("Sreenivasulu" ,end=" ")
    j=1 
    while j<=1:
        print("Macharla",end=" ")
        j += 1
    print()
    i += 1 


n1=0
n2=1 
num = int(input("Enter the fabanacci series range: "))
for i in range(2,num):
    n3 = n1 +n2
    n1 =n2
    n2= n3
    print(n3,end=" ")
print()
from numpy import *
list =array([1,2,3,4,7])
print(list * 2)




def get_activie_user(list):
    cnt =0
    for i in list:
        if len(i)>5:
            cnt +=1
    print(cnt) 

lenght_list =int(input("Enter the list lenght: "))
user_name =[]

for i in range(lenght_list):
    x =str(input("Enter the user name :"))
    user_name.append(x)

get_activie_user(user_name)




def factorial_num(num):
    fact =1
    for i in range(1,num+1):
        fact = fact * i

    return  fact    




fact_no = int(input("Enter the factorial number: "))

print(factorial_num(fact_no))



def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)


print(fact(5))



f = lambda a: a*a
print(f(5))


import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def greet():
    print("Hellow")
    greet()

# greet()    

'''

import datetime

x =datetime.datetime.now()

print(x.strftime("%a"))