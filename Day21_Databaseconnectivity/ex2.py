import sqlite3

conn=sqlite3.Connection('univ.db')

cursor=conn.cursor()

data=cursor.execute('select * from Student')

for i in data:
    print(i[1])

cursor.close()
conn.close()