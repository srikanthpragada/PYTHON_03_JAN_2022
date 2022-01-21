entries = ["98,56,77", "75,67,80", "45,56,79,7o"]

for entry in entries:
    marks = filter(str.isdigit, entry.split(","))
    total = sum(map(int, marks))
    print(total)
