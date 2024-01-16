import requests
import json

# GET api/data
response = requests.get('http://localhost:8000/api/data')
print("GET /api/data")
print("Status code:", response.status_code)
print("Response:", response.text)

# POST api/data
new_data_point = {'feature1': 1.04, 'feature2': 2.25, 'category': 1}
headers = {'Content-Type': 'application/json'}  # specify that we're sending JSON data
response = requests.post('http://localhost:8000/api/data', data=json.dumps(new_data_point), headers=headers)
print("\nPOST /api/data")
print("Status code:", response.status_code)
print("Response:", response.text)