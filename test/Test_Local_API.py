import requests
# API_URL = "http://127.0.0.1:8000/CLImood"
# params = {"message": "I passed my exam with 10"}
# response = requests.post(API_URL, params=params)
# print(response.json())

API_URL1 = "http://127.0.0.1:8000/health"
response1 = requests.get(API_URL1)
print(response1.json())
