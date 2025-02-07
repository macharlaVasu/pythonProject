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
import glob 
import pandas as pd 

path ='/Users/sreenivasulumacharla/Documents/Test_files/'

files =  glob.glob(path + '/*.csv.*')

print(files)
# changes to the env 

