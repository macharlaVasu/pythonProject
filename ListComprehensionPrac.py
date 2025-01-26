list = [1,2,3,4,5,6,7,8,9,10]
# res = []
# for i in list:
#     # print(list[i])
#     res.append(i *2)
# res =[i for i in list if i %2 != 0 ]
# print(res)  


# list1 =[[1,2,3],[9,8,7],[5,6,7]]
# res= []
# for i in list1:
#     # print(i)
#     for j in i:
#         # print(j)
#         res.append(j)
# print(res)  

# res =[j for i in list1 for j in i]
# print(res.sort())
# how to move the all zero to last of the list 
# a= [1,0,2,3,5,0,5,0,8,9,0,12]
# temp =[]
# nonzero = []
# for i in range(len(a)):
#     if a[i]==0:
#         temp.append(a[i])
#     else:
#         nonzero.append(a[i])
# print(nonzero + temp)            
"""
Python Programming  practices   
"""

# how to move the zero to last of the list 
# list = [2,5,3,0,8,9,0,6,0,5,8]
# print(list.count(0))
# res = [i for i in list if i !=0 ]
# res.extend([0] * list.count(0))
# print(res)

# mystr = "My phone number is : 8867677471 ,"
# number =[ i for i in mystr if i.isdigit()]
# print(number)

# list which extracts number  

list1 = [1,2,3,4,5,6,7,8,9,10]

list5 = list1[: : -1 ]
print(list5)

