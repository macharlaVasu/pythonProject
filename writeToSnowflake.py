from snowflake_connection import create_snowflake_connection
import pandas as pd

file_path = '/Users/sreenivasulumacharla/Documents/Test_files/snowflake_emp.csv'

df =pd.read_csv(file_path)

print(df)

conn = create_snowflake_connection()
cursor = conn.cursor()
table_name ='EMP'

# df.to_sql('EMP',conn,if_exists='replace',index=False)

for index,row in df.iterrows():
    # print(index,row)
    columns =','.join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query,tuple(row))

print(f"Data written to Snowflake table '{table_name}' successfully!")    

