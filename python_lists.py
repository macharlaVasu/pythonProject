# count=1
# while count<=100:
#     if count % 2 == 0:
#         i =count
#         print(i,end=" ")
#     count += 1
#Question 2
# num = int(input("Enter the number for multiple table: "))
# count=1
# while count<=10:
#     print(num," * ",count," = ",count*num)
#     count += 1
#Question 3
# list =[1,4,9,16,25,36,49,64,81,100]  
# idx =0
# while idx<len(list):
#     print(list[idx])
#     idx += 1
# Question 4
# num = 5
# fact =1
# i=1 
# while i<=num:
#     fact *=i
#     i +=1
# print(fact) 
# for i in range(5,0,-1):
#     for j in range(1,i+1) :
#         print(j,end="") 
#     print("")     

# Connection connection = DriverManager.getConnection(
#     "jdbc:snowflake://myorganization-myaccount.snowflake.com/?private_key_file=/tmp/rsa_key.p8&private_key_file_pwd=dummyPassword",
#     props);

"""
Pracktice session 
"""
# how to check the wheather given number is palindrom
# def check_Num_palindrom(num):
#     rev =0
#     temp =num
#     while num>0:
#         dig=num %10
#         rev= (rev*10)+dig
#         num= num // 10
#     if (temp == rev):
#         print(temp," is  polindrome")
#     else:
#         print(temp,"Not a  polindrome")            

# check_Num_palindrom(121)

num =5
res =1
# for i in range(1,num+1):
#     res=res * i
#     # print(res)
# print(f" Factorical of {num} is : {res}")   

# i=1
# while (num>=i):
#     res = res * i 
#     print(res,i)
#     i += 1
# print(res)

# def fact(n):
#     return 1 if (n==1 or n==0) else n * fact(n - 1) 
# print(fact(5))

# def isPalindrome(str):

#     # Run loop from 0 to len/2
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True

# main function
# str = "malayalamh"
# for i in range(0, int(len(str)/2)):
#     if str[i] != str[len(str)-i-1]:   
#         print('THis not polidrom ')
#     else:
#         print("is polindrome")
    
    
# str = "sreenivasulu"
# def poli_str(s):
#     print(s,s[::-1])
#     return s == s[::-1]

# ans =poli_str(str)
# if ans:
#     print("Yes")

# else:
#     print("No")    


str = "sreenivauslu"
for i in str:
    print(i,i[::-1])



