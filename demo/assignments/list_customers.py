import re

customers = {}
f = open("customers.txt", "rt")

for line in f.readlines():
    # Search for name
    name_match = re.search('[A-Za-z ]+', line)
    if name_match is None:  # Name not found
        continue

    name = name_match.group().strip()
    if len(name) == 0:  # Empty name, so ignore
        continue

    # Search for mobile
    mobile_match = re.search('[0-9]+', line)
    if mobile_match is None:  # Mobile not found
        continue

    # Add name and mobile to dict
    customers[name] = mobile_match.group()

f.close()

for name, mobile in sorted(customers.items()):
    print(f"{name:15} {mobile}")
