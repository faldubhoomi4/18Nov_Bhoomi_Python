import sqlite3

try:
    db = sqlite3.connect("studentdb.db")
    print("Database created/connected!")
except Exception as e:
    print(e)

create_tbl = (
    "create table studinfo(id integer primary key autoincrement,name text,gender text)"
)

try:
    db.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)