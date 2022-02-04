f = open("names.txt", "rt")

for line in sorted(f.readlines()):
    # print(line, end ='')
    print(line.strip())

f.close()
