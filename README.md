# WorkoutTracker
Track your daily exercise routine, calories and other details automatically.

I used [Nutritionix API](https://developer.nutritionix.com/) for exercise information and [Sheety API](https://sheety.co/) to insert rows into the Google Sheets spreadsheet.

## Prerequisites:
- Create an account in [Nutritionix API](https://developer.nutritionix.com/) & [Sheety API](https://sheety.co/) and generate your API keys.
- Create environment variables containing your private API keys and tokens within your local environment by typing in terminal:
  
  ```bash
   export SHEETY_USER=sheety_user
   export SHEETY_PASS=sheety_pass
   export NUTRI_APIKEY=nutri_apikey
   export NUTRI_APPID=nutri_appid
  ```
  
- Python 3.9 & up

### To run in terminal:
- Open Powershell in the local repository folder
- Type:

  ```bash
   python main.py
  ```

### Expected Output
Input: `ran 5k and cycled for 20 minutes`

```bash
{
  "workout": {
    "date": "30/10/2023",
    "time": "15:25:03",
    "exercise": "Running",
    "duration": 31.08,
    "calories": 355.35,
    "id": 3
  }
}
{
  "workout": {
    "date": "30/10/2023",
    "time": "15:25:03",
    "exercise": "Road Cycling",
    "duration": 20,
    "calories": 233.33,
    "id": 4
  }
}
```


