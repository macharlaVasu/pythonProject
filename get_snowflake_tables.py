# Read the snowflake table data and generate the csv files update the code
# Test the code 
from snowflake_connection import create_snowflake_connection
import pandas as pd

def writeSFTableToCSVFile(conn ,filePath,query):
    conn =create_snowflake_connection()
    df = pd.read_sql_query(query,conn)
    conn.close()
    df.to_csv(filePath,index=None)
    print(f"File Saved to: {file_path}")


conn =create_snowflake_connection()
query = "select * from emp;"
file_path ='/Users/sreenivasulumacharla/Documents/Test_files/snowflake_emp.csv'    

writeSFTableToCSVFile(conn,file_path,query)






