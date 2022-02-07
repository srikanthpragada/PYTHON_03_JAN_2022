# Usage : python search_programs.py  word  start_directory

import os
import sys


def has_word(filename, word):
    try:
        with open(filename, "rt") as f:
            return word in f.read()
    except:
        return False

    # there must be atleast 2 parameters - filename and search word


if len(sys.argv) < 2:
    print("Usage : python search_programs.py  <search_word>  [start_directory]")
    exit()

# If start directory not given then take current directory
if len(sys.argv) == 2:
    start_directory = os.getcwd()
else:
    start_directory = sys.argv[2]

search_word = sys.argv[1]
entries = os.walk(start_directory)
count = 0

for dirname, dirs, files in entries:
    for f in files:
        if f.endswith(".py"):
            filename = dirname + "\\" + f
            if has_word(filename, search_word):
                print(filename)
                count += 1

print(f"Word [{search_word}] found in [{count}] files")
