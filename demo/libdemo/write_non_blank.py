SOURCE = "names.txt"
TARGET = "newnames.txt"

sf = open(SOURCE, "rt")
tf = open(TARGET, "wt")

for line in sf.readlines():
    if len(line.strip()) > 0:
        tf.write(line)

sf.close()
tf.close()
