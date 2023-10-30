import requests
from datetime import datetime
import os

NUTRI_APPID = os.environ["NUTRI_APPID"]
NUTRI_APIKEY = os.environ["NUTRI_APIKEY"]

SHEETY_USER = os.environ["SHEETY_USER"]
SHEETY_PASS = os.environ["SHEETY_PASS"]

# Sending exercise input to Nutritionix API which uses NLP to get relevant info such as calories burnt and duration
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRI_APPID,
    "x-app-key": NUTRI_APIKEY
}

exercise_query = str(input("Which exercises did you do today? "))

parameters = {
    "query": exercise_query
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

# Getting current date and time
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

# Adding rows to personal Google Sheets spreadsheet for each exercise
sheety_url = os.environ["SHEETY_ENDPOINT"]

for exercise in result["exercises"]:
    parameters_sheety = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=sheety_url, json=parameters_sheety, auth=(SHEETY_USER, SHEETY_PASS))
    response.raise_for_status()
    print(response.text)
