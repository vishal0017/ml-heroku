import requests  # Import the requests library for sending HTTP requests

# Define the URL of the API endpoint
url = "https://first-app-api-0219240da9d9.herokuapp.com/predict"

# Create the data payload (the input for your ML model)
data = {"experience": 3}

# Set the headers to indicate that the request body is in JSON format
headers = {"Content-Type": "application/json"}

# Send an HTTP POST request to the API endpoint with the given data and headers
response = requests.post(url, json=data, headers=headers)

# Print the JSON response from the API
print(response.json())
