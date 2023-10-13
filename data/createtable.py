import sqlite3

# Connect to the existing or a new database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a new table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        cardnumber TEXT NOT NULL
    )
''')

# Commit the changes
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
