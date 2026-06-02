import sqlite3
 
sqlCreateTable="""
create table if not exists student
(
    id integer primary key autoincrement,
    name text ,
    email text
)
"""
conn=sqlite3.connect('studentManagementSystem.db')
 
cur=conn.cursor()
 
cur.execute(sqlCreateTable)
conn.commit()
conn.close()
 
 
print(" the db is created!")