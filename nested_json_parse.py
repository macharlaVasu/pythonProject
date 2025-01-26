import pandas as pd
from pandas import json_normalize

def dynamic_json_parser(data):
    """
    Dynamically flattens nested JSON into a pandas DataFrame.
    Handles lists, dictionaries, and other nested structures.
    """
    def flatten_json(data):
        """
        Flatten JSON recursively and normalize lists/dictionaries dynamically.
        """
        if isinstance(data, list):  # Handle lists
            # Flatten each item in the list and concatenate into a single DataFrame
            return pd.concat([flatten_json(item) for item in data], ignore_index=True)
        elif isinstance(data, dict):  # Handle dictionaries
            # Normalize dictionaries and flatten further nested elements
            normalized = json_normalize(data, sep='_')
            for col in normalized.columns:
                if isinstance(normalized[col][0], (list, dict)):  # Check for nested fields
                    # Recursively flatten these fields
                    nested_df = flatten_json(normalized[col][0])
                    nested_df.columns = [f"{col}_{subcol}" for subcol in nested_df.columns]
                    normalized = normalized.drop(columns=[col]).join(nested_df, how='left')
            return normalized
        else:  # Handle simple fields
            return pd.DataFrame([data])

    # Start flattening the data
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
