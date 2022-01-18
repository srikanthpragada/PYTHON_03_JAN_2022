students = {}
data = "1:90,2:60,2:89,1:79,3:50,3:60,3:90,2:87"
entries = data.split(",")

for e in entries:
    rollno, marks = e.split(":")
    marks = int(marks)
    if rollno in students:
        students[rollno].append(marks)  # Add new value to list
    else:
        students[rollno] = [marks]    # Create a new entry with list

# print(students)

for rno, markslist in sorted(students.items()):
    total = sum(markslist)
    avg = total // len(markslist)
    print(f"{rno:5} {total:3} {avg:5.2f}")
