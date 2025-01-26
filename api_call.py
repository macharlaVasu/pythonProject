import requests
import pandas as pd
import json

# api_url= 'https://jsonplaceholder.typicode.com/todos/2'
api_url= 'https://jsonplaceholder.typicode.com/posts/2'

# response = requests.get(api_url + '/10')
response = requests.get(api_url )
if response.status_code == 200:
    # json_data = response.json()  # Parse JSON response
    print("API data fetched successfully. ",response.text)


else:
    print(f"Failed to fetch data from API. Status code: {response.status_code}")
    exit()