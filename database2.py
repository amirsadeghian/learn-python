import sqlite3

#Database connection
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#Database table creation
sql = "DROP TABLE IF EXISTS Counts"
cur.execute(sql)
sql = "CREATE TABLE Counts (org TEXT, count INTEGER)"
cur.execute(sql)


#Open the file
try:
    fh = open("mbox.txt")
except:
    print('Error')
    quit()

map = {}
for line in fh:
    if line.startswith('From: '):
        parts = line.split()
        email = parts[1]
        org = email.split('@')[1]
        if org in map:
            map[org] += 1
        else:
            map[org] = 1
for item in map:
    sql = "INSERT INTO Counts (org,count)VALUES(?,?)"
    cur.execute(sql,(item,map[item]))

conn.commit()

#close the database connection
conn.close()