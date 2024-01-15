import requests

# Test the add_data endpoint
# print("Sending POST request to /add")
# response = requests.post('http://localhost:8000/add/',
#                          data={'feature1': '1.23', 'feature2': '4.56',
#                                'category': '2'})
# print(response.status_code)

# Test the delete_data endpoint
print("Sending POST request to /delete/3")
response = requests.post('http://localhost:8000/delete/1/')
print(response.status_code)
