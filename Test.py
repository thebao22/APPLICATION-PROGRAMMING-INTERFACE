import requests

API_URL = "http://127.0.0.1:8000/CLImood"
params = {"message": "I just broke up with my girl friend"}
response = requests.post(API_URL, params=params)
ROOT_URL = "http://127.0.0.1:8000/"
response2 = requests.get(ROOT_URL)
HEALTH_URL = "http://127.0.0.1:8000/health"
response3 = requests.get(HEALTH_URL)
print(response.json())
print(response2.json())
print(response3.json())