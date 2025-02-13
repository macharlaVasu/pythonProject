# Read the snowflake table data and generate the csv files 
from snowflake_connection import create_snowflake_connection
import pandas as pd

conn =create_snowflake_connection()

print(conn)

query = "select * from emp;"

df = pd.read_sql_query(query,conn)

conn.close()

print (df.head())

file_path ='/Users/sreenivasulumacharla/Documents/Test_files/snowflake_emp.csv'    


df.to_csv(file_path,index=None)

print(f"File Saved to: {file_path}")