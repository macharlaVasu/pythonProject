"""
Method :1 of the Fibonacci series 
# """
# num=2 
# n1=0
# n2=1
# print("Fibonacci Series ",n1,n2,end=" ")
# for i in range(2,num):
#     n3 =n1+n2
#     n1=n2
#     n2=n3
#     print(n3,end =" ")
    
# print()

"""
Method 2 
""" 
def Fibanacii_series(i):
    if i<=1:
        return i
         
    else:
        return (Fibanacii_series(i-1) + Fibanacii_series(i-2))
    
numf = 10
for i in range(numf):
    print(Fibanacii_series(i),end=" ")
print()    


# Pyramid Patterns in Python with Numbers
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")

def print_pyramid(num):
    if num >0 :
        print_pyramid(num - 1)
        print('*' * num)
        #print('*' * num)

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")

n1=5
for i in range(n1,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("")             
#rows =int(input("Enter the values for : "))
# print_pyramid(5)                  
def pymd_s(num):
    for i in range(num,0,-1):
        #print(i)
        for j in range(num-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print("") 
        
def pymd_r(num):
    for i in range(1,num+1):
        #print(i)
        for j in range(num-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print("")                   
            
pymd_r(5)
pymd_s(5) 


from datetime import datetime
import time
import pytz
# Get current date
#current_date = datetime.now(pytz.timezone('Asia/Kolkata'))
current_date = datetime.now()
print(current_date)
# Format the date
formatted_date = current_date.strftime('%A %d %B %Y')
print(formatted_date)
tz= time.timezone
print(tz)