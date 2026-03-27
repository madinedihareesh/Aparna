import sqlite3

conn=sqlite3.Connection('univ.db')

cursor=conn.cursor()

cursor.execute('insert into Student values(1,\'james\'),(2,\'jason\'),(3,\'sam\')')

conn.commit()

cursor.close()
conn.close()