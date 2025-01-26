# for i in range(1,3):
#     print("I loop",i)
#     for j in range(1,i+1):
#         print("J loop ",j)
# print() 

# 1 how to use the that file like in 


# for i in range(5):
#     for j in range(5-i):
#         print("#",end="")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print("#",end="")
#     print()   

from array import *
arr =array('i',[])
n = int(input("Enter the length of array: "))
for i in range(n):
    x = int(input("Enter the arrya value: "))
    arr.append(x)

print(arr)    
cnt =0 
find_num =int(input("Enter the values : "))
for j in arr:
    if j == find_num:
        print(cnt)
        break
    cnt+= 1
     









  
          


