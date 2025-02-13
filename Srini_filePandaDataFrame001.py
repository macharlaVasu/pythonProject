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
import os 

# path ='/Users/sreenivasulumacharla/Documents/Git_Python/pythonProject/'
path = '/Users/sreenivasulumacharla/Documents/Test_files/'


files =  glob.glob(path + '/*.csv')

print(files)
# changes to the env 

data_frame = pd.DataFrame()
content = []

for filename in files:
  try :
    df = pd.read_csv(filename,index_col=None,on_bad_lines='skip')
    content.append(df)    
  except Exception as e:
    print(str(e))

data_frame = pd.concat(content)
print(os.getcwd())
print(data_frame)


