import requests

response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Singapore")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = response.json()

print(details['datetime'])


