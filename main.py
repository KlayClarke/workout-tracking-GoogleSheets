import os
import requests

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_params = {
    'query': input('Tell us what you did to stay active today!\n'),
    'gender': 'male',
    'weight_kg': 77,
    'height_cm': 170,
    'age': 22
}

response = requests.request('POST', url=exercise_endpoint, data=exercise_params, headers=HEADERS)
response.raise_for_status()

data = response.json()

print(data)
