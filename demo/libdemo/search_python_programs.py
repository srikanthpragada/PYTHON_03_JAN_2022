import os


def has_word(filename, word):
    with open(filename, "rt") as f:
        return word in f.read()


entries = os.walk(r"c:\classroom\jan3")
word = "map"
count = 0

for dirname, dirs, files in entries:
    for f in files:
        if f.endswith(".py"):
            filename = dirname + "\\" + f
            if has_word(filename, word):
                print(filename)
                count += 1

print(f"Word [{word}] found in [{count}] files")
