import requests
from twilio.rest import Client
import os
qpi_key = 'API_KEY'

account_sid = 'ACC_SID'
auth_token = 'AUTH_TOKEN'


parameters = {'lat':43.222015, 'lon':76.851250, 'appid':'cc69b8a8fccc77a022c4d90468b6f944','exclude':'current,minutely,daily'}
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hourly_weather in range(0,13):
    condition = weather_data['hourly'][hourly_weather]['weather'][0]['id']
    if condition < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+15612207867',
        to='+85295355691'
    )
    print(message.status)

