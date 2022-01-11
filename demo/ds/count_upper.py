# Count no. of uppercase letters

s = "This is FINE"
count = 0
for c in s:
    if c.isupper():
        count += 1

print("Count", count)