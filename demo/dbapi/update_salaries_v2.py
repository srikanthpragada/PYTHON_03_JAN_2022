import sqlite3

con = sqlite3.connect(r"c:\classroom\apr19\hr.db")
cur = con.cursor()
f = open('salaries.txt', 'rt')
success = notfound = failure = 0

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) != 2:
        continue          # Ignore line

    try:
        id, salary = parts
        cur.execute("update employees set salary = ? where id = ?", (salary, id))
        if cur.rowcount == 1:
           success += 1
        else:
           notfound += 1
    except Exception as ex:
        failure += 1


con.commit()
f.close()
cur.close()
con.close()

print(f"Success count    : {success}")
print(f"Not found  count : {notfound}")
print(f"Failures count   : {failure}")
