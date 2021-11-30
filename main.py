import os
from datetime import datetime
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
    'query': 'ran 1 mile',
    'gender': 'male',
    'weight_kg': 77,
    'height_cm': 170,
    'age': 22
}

exercise_response = requests.request('POST', url=exercise_endpoint, data=exercise_params, headers=HEADERS)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()

exercise_name = exercise_data['exercises'][0]['name']
exercise_duration = exercise_data['exercises'][0]['duration_min']
exercise_calories_burned = exercise_data['exercises'][0]['nf_calories']

SHEETY_USERNAME = os.environ.get('SHEETY_USERNAME')
SHEETY_PROJECT_NAME = os.environ.get('SHEETY_PROJECT_NAME')

sheety_endpoint = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}'

now = datetime.now()
now_date = now.strftime('%d/%m/%Y')
now_time = now.strftime('%H:%M:%S')

sheety_params = {
    'workout': {
        'date': now_date,
        'time': now_time,
        'exercise': exercise_name,
        'duration': exercise_duration,
        'calories': exercise_calories_burned,
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_params)
sheety_response.raise_for_status()
sheety_data = sheety_response.json()

print(sheety_data)