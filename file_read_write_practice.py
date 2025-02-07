
# import os 

# if os.path.exists('mydata.txt'):
#     print("File is aviable in loacation")
# else:
#     print("File not avaibl: ",os.getcwd())    

# how to remove the multiple space in file 
# import re 

# with open("mysample.txt","r")  as file:
#     content = file.read()

# cleaned_content =   re.sub(r'\s+',' ' ,content)

# print(content)

# how to remove the empty lines 

# with open("mysample.txt","r+") as file:
#      for lines in file:
#           if not lines.isspace():
#                file.write(lines)
               
with open ("emp_pract001.csv",'r') as f:
    for i in f:
        print(i)
