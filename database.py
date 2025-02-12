import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('select * from Users')
results = cur.fetchall()
for result in results:
    print(result[0])


name = 'Susan'
email = 'susan@google.com'
insertSQL = "INSERT INTO Users(name,email)values(?,?)"

cur.execute(insertSQL,(name,email))

cur.execute('select * from Users')

conn.commit()

results = cur.fetchall()
for result in results:
    print(result[0]+' - '+result[1])