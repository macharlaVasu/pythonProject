import pandas as pd
from pandas import json_normalize

def dynamic_json_parser(data):
    """
    This function takes in JSON data (which may have nested structures) 
    and dynamically flattens it into a pandas DataFrame.
    """
    # Start by normalizing the JSON structure
    def flatten_json(data):
        """
        Flatten JSON recursively to ensure all nested fields are converted to columns
        """
        # We will use json_normalize to handle the flattening
        if isinstance(data, list):  # If it's a list, handle each item
            return pd.concat([flatten_json(item) for item in data], ignore_index=True)
        elif isinstance(data, dict):  # If it's a dictionary, normalize it
            return json_normalize(data, sep='_')
        else:
            # If the data is not nested (neither list nor dict), return as is
            return pd.DataFrame([data])

    # Flatten the nested structure
    flattened_df = flatten_json(data)

    return flattened_df

# Example JSON
json_data = [
    {
        "id": 1,
        "name": "John",
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zipcode": "10001"
        },
        "friends": [
            {"name": "Jane", "age": 24},
            {"name": "Jack", "age": 26}
        ]
    },
    {
        "id": 2,
        "name": "Alice",
        "age": 30,
        "address": {
            "street": "456 Oak Rd",
            "city": "Los Angeles",
            "zipcode": "90001"
        },
        "friends": [
            {"name": "Bob", "age": 31},
            {"name": "Charlie", "age": 32}
        ]
    }
]

# Parse and flatten the JSON data
df = dynamic_json_parser(json_data)

# Display the result
print(df)
