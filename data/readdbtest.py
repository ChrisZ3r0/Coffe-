import sqlite3

# Connect to the existing database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# You can now execute SQL commands on the existing database
# Execute SQL queries and commands here
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()

for row in data:
    print(row)

# Close the cursor and the connection when done
cursor.close()
conn.close()
