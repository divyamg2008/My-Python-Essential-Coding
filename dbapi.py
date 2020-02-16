import sqlite3

db = sqlite3.connect('db-api.db') #getting handle
cur = db.cursor() # getting cursor on handle
cur.execute("DROP TABLE IF EXISTS test")
cur.execute("""CREATE TABLE test
(id INTEGER PRIMARY KEY, string TEXT, number INTEGER)
""")
cur.execute(""" 
INSERT INTO test (id, string, number) VALUES (2124,'three', 3)
""")
cur.execute(""" 
INSERT INTO test (string, number) VALUES ('five', 5)
""")
cur.execute(""" 
INSERT INTO test (string, number) VALUES ('one', 123)
""")
db.commit()
cur.execute("SELECT COUNT(*) FROM TEST")
count = cur.fetchone()[0]
print(count)

for row in cur.execute("SELECT * FROM test"):
    print (row)
cur.execute("DROP TABLE test")
db.close()
