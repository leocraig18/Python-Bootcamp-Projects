import requests
import datetime
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

date = datetime.date.today().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")

GENDER = "male"
WEIGHT_KG = "90"
HEIGHT_CM = "183.5"
AGE = "21"

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("SHEETY_ENDPOINT_WORKOUT")

exercise_input = input("What exercise did you do today?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
result = response.json()


exercise = result['exercises'][0]['name'].title()
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

sheet_parameters = {
    "sheet1": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}
sheet_response = requests.post(url=sheet_endpoint, json=sheet_parameters, auth=(USERNAME, PASSWORD))
print(sheet_response.text)

