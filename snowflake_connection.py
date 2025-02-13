
# snowflake_connection.py
import snowflake.connector

def create_snowflake_connection():
    """
    Create and return a Snowflake connection.
    """
    config = {
        "user": "SRINI",          # Your Snowflake username
        "password": "Sreenivasulu@123",      # Your Snowflake password
        "account": "fspzgvp-io77649",        # Your Snowflake account identifier (e.g., xy12345)
        "warehouse": "COMPUTE_WH",    # Your Snowflake warehouse
        "database": "DEMO",      # Your Snowflake database
        "schema": "TEST"           # Your Snowflake schema
    }

    try:
        # Establish a connection
        conn = snowflake.connector.connect(**config)
        print("Connected to Snowflake successfully!")
        return conn
    except Exception as e:
        print("An error occurred while connecting to Snowflake:", str(e))
        return None
    

create_snowflake_connection()    