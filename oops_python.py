'''
oops concepts example programs
1. Class 
2. Objects 
3. Inheritance
4. Polymorphism
5. Encapsulation 
6. Abstract 

'''
# 1 Class 

class Animai:
    def __init__(self,name):
        self.name =name
    def hellow(self):
        print(f'Hellow {self.name}')    


obj = Animai('Rubby')
obj.hellow()


obj1 = Animai('canddy')
obj1.hellow()

x =1 
y= 2.8

print(x + y )