import sqlite3

conn = sqlite3.connect('admin_db.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS admin
       (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       NAME TEXT NOT NULL,
       PASSWORD CHAR(20));''')

## 插入数据
def insert_admin_data():
	conn = sqlite3.connect('admin_db.db')
    print("Please input NAME:")
    NAME = input()
    print("Please input PASSWOED:")
    PASSWOED = input()
    conn.execute("INSERT INTO admin (ID,NAME,PASSWORD) \
    	VALUES (null, ?, ? )",list(NAME,PASSWOED))
    print ("Records Insert successfully")
    conn.commit()

print ('--------------------------- start fetch data from company --------------------------');

cursor = conn.execute("SELECT id, name  from admin")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])

print ("Select Operation done successfully.")

conn.close()
