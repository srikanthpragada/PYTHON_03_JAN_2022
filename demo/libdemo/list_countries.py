import requests

response = requests.get("https://restcountries.com/v3.1/all")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

countries = response.json()

for country in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    name = country['name']['official']
    capital = country.get('capital', [""])[0]  # First capital
    population = country['population']

    print(f"{name:50} {capital:30} {population:12}")
