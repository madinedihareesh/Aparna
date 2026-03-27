import sqlite3

conn=sqlite3.Connection('univ.db')

cursor=conn.cursor()

cursor.execute('create table Student(id integer primary key,name text)')

conn.commit()

cursor.close()
conn.close()

