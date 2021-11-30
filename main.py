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
    'query': input('What did you do today to stay active?'),
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
        'exercise': exercise_name.title(),
        'duration': round(exercise_duration, 1),
        'calories': round(exercise_calories_burned),
    }
}


# To post data to Google Sheet
sheety_response = requests.post(url=sheety_endpoint, json=sheety_params)
sheety_response.raise_for_status()
sheety_data = sheety_response.json()
print(sheety_data)

# # To delete previously posted data from Google Sheet
# sheety_delete = requests.delete(url='https://api.sheety.co/a99db41127fc507b26df34b1a69f67ad/workoutTracking/workouts/3')
# sheety_delete.raise_for_status()
# sheety_delete_data = sheety_delete.json()