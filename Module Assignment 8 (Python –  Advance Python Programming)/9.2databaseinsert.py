import sqlite3

try:
    db = sqlite3.connect("studentdb.db")
    print("Database created/connected!")
except Exception as e:
    print(e)

insert_data = "insert into studinfo(name,gender)values('Bhoomi','Female'),('Mit','Male'),('Yash','Male')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)

cr = db.cursor()
show_data = "select * from studinfo"
try:
    cr.execute(show_data)
    data = cr.fetchall()
   
    for i in data:
        print(i)
except Exception as e:
    print(e)