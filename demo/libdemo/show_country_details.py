import requests

response = requests.get("https://restcountries.com/v3.1/all")
countries = response.json()

country_dict = {}
for country in countries:
    country_dict[country['cca3']] = country['name']['official']


def get_country_names(codes):
    names = []
    for c in codes:
        names.append(country_dict[c])

    return ",".join(names)


def get_country_info(code):
    for c in countries:
        if c['cca3'] == code:
            return c

    return None  # Code not found


while True:
    code = input("Enter country code [over to stop]: ")
    if code == "over":
        break

    country = get_country_info(code.upper())
    if country is None:
        print("Sorry! County code not found!")
        continue

    print(f"Name              : {country['name']['official']}")
    print(f"Capital           : {country['capital'][0]}")
    print(f"Population        : {country['population']}")
    print(f"Area              : {country['area']}")
    density = (country['population'] // country['area'])
    print(f"Density           : {density:.2f}")
    if 'borders' in country:
        names = get_country_names(country['borders'])
    else:
        names = "No border"
    print(f"Border            : {names}")
    print("=" * 50)
