"""
This script is used to test the BU course catalog API.
"""

import requests

# Define the API endpoint and your x-api-key
url = "https://prod-buprod-fm.snaplogic.io/api/1/rest/feed/run/task/BUProd/Admin-Reporting-And-Analytics/PublicCourseCatalog/getPublicCourseCatalog_triggered"
api_key = "you-api-key-here"  # Replace with your actual x-api-key

# Define headers and parameters
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key
}

# Optional parameters: update as needed
params = {
    "term": "2251",  # Replace with the desired term (e.g., '2251' for Spring 2025)
    "college": "CDS"  # Replace with the desired college (e.g., 'CDS')
}

# Send the GET request
response = requests.get(url, headers=headers, params=params)

# Handle the response
if response.status_code == 200:
    print("Success! Here is the data:")
    print(response.json())
elif response.status_code == 401:
    print("Authorization failed. Check your API key.")
elif response.status_code == 422:
    print("Validation issue with input parameters.")
elif response.status_code == 500:
    print("Server error. The Snaplogic service could not be reached.")
else:
    print(f"Unexpected status code: {response.status_code}")
    print(response.text)


