import sqlite3

conn = sqlite3.connect('exercises.db')
print("Opened database successfully")

conn.execute('CREATE TABLE exercises (name TEXT, sets TEXT, weight TEXT)')
print("Table created successfully")
conn.close()
