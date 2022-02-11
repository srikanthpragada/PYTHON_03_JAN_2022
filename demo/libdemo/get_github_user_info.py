import requests

response = requests.get("https://api.github.com/users/srikanthpragada")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = response.json()

print(details['name'])
print(details['company'])
print(details['public_repos'])

