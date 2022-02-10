from datetime import datetime

players = {}
f = open("players.txt", "rt")

for line in f.readlines():
    # line contains name,dob in ddmmyyyy
    parts = line.split(',')

    # Ignore line if it doesn't contain two parts
    if len(parts) < 2:
        continue

    try:
        # Convert string to datetime
        dob = datetime.strptime(parts[1].strip(), '%d%m%Y')
    except:
        continue    # Ignore as DOB is not valid

    # Add name and dob to dict
    players[parts[0].strip()] = dob

f.close()

# Sort players by dob
for name, dob in sorted(players.items(), key=lambda t: t[1], reverse = True):
    age_in_years = (datetime.now() - dob).days // 365
    print(f"{name:15} {dob.strftime('%d-%m-%Y')}  {age_in_years:2}")
