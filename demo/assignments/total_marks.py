students = {}
data = "1:90,2:60,2:89,1:79,3:50,3:60,3:90,2:87"
entries = data.split(",")
# print(entries)
for e in entries:
    rollno, marks = e.split(":")
    marks = int(marks)
    if rollno in students:
        students[rollno] = students[rollno] + marks
    else:
        students[rollno] = marks

for rno, total in sorted(students.items()):
    print(f"{rno:5} {total:3}")
