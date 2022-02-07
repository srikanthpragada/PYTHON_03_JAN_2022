import os

entries = os.walk(r"c:\classroom\jan3\demo")
count = 0

for dirname, dirs, files in entries:
    for f in files:
        if f.endswith(".py"):
            count += 1

print("Count =", count)
