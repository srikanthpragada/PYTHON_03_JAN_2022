data = ["abc", "AB", "xy", "PQ", "def"]

for s in sorted(data, key=str.upper):
    print(s)
