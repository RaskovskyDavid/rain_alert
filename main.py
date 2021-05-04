from api_key import api_key
from twilio_secure_data import twilio_sid, twilio_token
import requests
from twilio.rest import Client
# this is the path and the parameters that i going to send
path = "https://api.openweathermap.org/data/2.5/onecall"
param = {
    "lat": 19.404430,
    "lon": -99.168870,
    "exclude": "current,minutely,daily",
    "appid": api_key
}
# get the data from the api
response = requests.get(url=path, params=param)
# check if there some problem with the get method
response.raise_for_status()
# reading the data from de response
weather_data = response.json()
# searching if there is any hour where its raining from this they
umbrella_need = any(True for hour_clime in weather_data["hourly"][7:14:1] if hour_clime["weather"][0]["id"] < 700)
print(umbrella_need)
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(twilio_sid, twilio_token)

message = client.messages \
                .create(
                     body="Its going to rain today. Remember to bring an ",
                     from_='+15023058860',
                     to='+525620366355'
                 )

print(message.status)
