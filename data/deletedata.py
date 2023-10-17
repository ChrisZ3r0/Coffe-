import sqlite3

# Connect to the existing database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Example: Delete a user with a specific ID
user_id_to_delete = input('ID: ')  # Replace with the actual ID of the user you want to delete
cursor.execute("DELETE FROM users WHERE id = ?", (user_id_to_delete,))

# Commit the changes
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
