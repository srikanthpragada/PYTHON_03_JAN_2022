import re
import os

FILE = "names.txt"
TARGET_FILE = "temp.txt"

with open(FILE, "rt") as sf, open(TARGET_FILE, "wt") as tf:
    for line in sf.readlines():
        # replace multiple spaces with one space and also remove leading and trailing spaces
        new_line = re.sub(' +', ' ', line).strip()

        # If not empty line
        if len(new_line) > 0:
            tf.write(new_line + "\n")

# Remove original file and rename temp file as original
os.remove(FILE)
os.rename(TARGET_FILE, FILE)
