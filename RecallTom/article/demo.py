import sqlite3

conn = sqlite3.connect('django.db')

c = conn.cursor()
c.execute(''' 
select name from sqlite_master where type='table' order by name
''')
print (c.fetchall())
conn.commit()
conn.close()