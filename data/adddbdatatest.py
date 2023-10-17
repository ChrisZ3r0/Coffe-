import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

custom_id = 528924223
name = 'John Doe'
mail = 'john@doe.com'
# Add other data...

# Replace 'custom_id', 'name', '...' with actual column names
# Replace '?, ?, ...' with actual values
cursor.execute("INSERT INTO users (id, username, email) VALUES (?, ?, ?)", (custom_id, name, mail))
conn.commit()

cursor.close()
conn.close()
