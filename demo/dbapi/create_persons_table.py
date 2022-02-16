# Test connection

import sqlite3
import dbutil

try:
    con = sqlite3.connect(dbutil.DBNAME)
    cur = con.cursor()
    cur.execute('create table persons (name varchar(20) primary key, email varchar(30) unique, age integer(3))')
    con.close()
except Exception as ex:
    print('Error :', ex)

