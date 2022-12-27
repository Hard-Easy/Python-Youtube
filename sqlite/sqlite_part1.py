#SQLite Code Adhayayana

import sqlite3

connection = sqlite3.connect('dummy_database.db')

cursor = connection.cursor()
cursor.execute("drop table if exists dummy")
table_statement = """create table dummy(
    name text not null,
    age int
);
"""

cursor.execute(table_statement)

cursor.execute("insert into dummy values(?,?)",("Ross",25))
cursor.execute("insert into dummy values(?,?)",("Ishu",28))
cursor.execute("insert into dummy values(?,?)",("Robin",30))

cursor.execute("select * from dummy")

for row in cursor:
    print(row)

cursor.close()
connection.commit()
connection.close()