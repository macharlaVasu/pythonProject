import base64

# Original string
data = "Hello, World!"

# Convert string to bytes
data_bytes = data.encode('utf-8')

# Encode to Base64
base64_encoded = base64.b64encode(data_bytes)

# Convert bytes back to string for display
base64_encoded_str = base64_encoded.decode('utf-8')

print("Encoded:", base64_encoded_str)
print(data_bytes)




# Base64 encoded string
base64_encoded_str = "SGVsbG8sIFdvcmxkIQ=="

# Convert string to bytes
base64_encoded_bytes = base64_encoded_str.encode('utf-8')

# Decode from Base64
data_bytes = base64.b64decode(base64_encoded_bytes)

# Convert bytes back to string
data = data_bytes.decode('utf-8')

print("Decoded:", data)