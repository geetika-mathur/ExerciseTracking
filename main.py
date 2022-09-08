import requests
from datetime import datetime
import os

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "your endpoint"

APP_ID = os.environ.get()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
exercise = input("Tell me what exercise you did: ")
user_params = {
    "query": exercise,
    "gender": "gender_here",
    "weight_kg": weight_here,
    "height_cm": height_here,
    "age": age_here
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": ,
}

nutri_response = requests.post(url=nutri_endpoint,
                               json=user_params,
                               headers=header)
nutri_response.raise_for_status()
result = nutri_response.json()
print(result)

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    header_sheet = {"userName": "", "password": ""}
    sheety_response = requests.post(url=sheety_endpoint,
                                    json=sheet_inputs,
                                    headers=header_sheet)
    print(sheety_response.text)
