'''
count theh empty line and write into anoter output file 

cnt = 0
with open('mysample.txt', 'r') as f, open('output.txt', 'w') as o:
    for i in f:  # Read file line by line
        if i.strip():  # Ignore empty lines
            o.write(i)
            cnt += 1

print(cnt)
'''
import os 

path ='/Users/sreenivasulumacharla/Documents/Test_files/'

dir_list = os.listdir(path)
print(dir_list)

for i in dir_list:
    print(i)
    with open(path + i,'r') as f:
        print(f.read())
