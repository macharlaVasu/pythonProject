# reverse the list mothod 1
a = [1,3,4,6,5,7]

h =len(a)
n =a[::-1]
print (n)

# reverse the list mothod 2
res = []
print(a)
for i in a:
    res.insert(0,i)
    print(i)
print(res)


