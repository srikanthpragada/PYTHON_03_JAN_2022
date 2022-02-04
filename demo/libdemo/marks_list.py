# Display rollno followed by total marks using marks.txt

f = open("marks.txt", "rt")

for line in f.readlines():
    parts = line.split(",")
    rollno = parts[0]
    # total = 0
    # for m in parts[1:]:
    #     total += int(m)
    total = sum(map(int, parts[1:]))
    print(f"{rollno:5} {total:5}")

f.close()
