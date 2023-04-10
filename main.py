from twilio.rest import Client

account_sid = "AC9e7fc9299902cc5811e4aab121e49daf"
auth_token = "23f0de75c7f22d0b9e695de9ffacf6e0"
client = Client(account_sid, auth_token)


api_key = "c82b02faae87466cd6385d2322ac4fd7"
MY_LAT = 53
MY_LON = 7
endpoint = "https://api.openweathermap.org/data/3.0/onecall"

#4.071510

import requests

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": api_key
}
response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

list_next_twelve = [weather_data["hourly"][item]["weather"][0]["id"] for item in list]

if any(item < 700 for item in list_next_twelve):
    will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an umbrella.",
        from_='+13465122591',
        to='+237653919277'
    )
    print(message.status)
