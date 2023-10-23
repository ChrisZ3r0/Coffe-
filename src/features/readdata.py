import sqlite3
import sys

def load_coffee_db():
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM coffee")
    data = cursor.fetchall()

    cardid  =   []
    coffee_nam  =   []
    price   =   []
    available   =   []
    button_num  =   []



    for row in data:
        print(row)

    cursor.close()
    conn.close()

def load_users_db():
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    cardid  =   []
    cardnumber   =   []
    password  =   []

    for row in data:
        print(row)

    cursor.close()
    conn.close()

def load_admin_db():
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM admin")
    data = cursor.fetchall()

    cardid  =   []
    cardnumber   =   []
    password  =   []

    for row in data:
        print(row)

    cursor.close()
    conn.close()

def load_coffeelog_db():
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM coffeelog")
    data = cursor.fetchall()

    buyid  =   []
    date  =   []
    cardid   =   []
    coffetype  =   []

    for row in data:
        print(row)

    cursor.close()
    conn.close()

def load_moneypaid_db():
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM moneypaid")
    data = cursor.fetchall()

    cardid  =   []
    date  =   []
    rate   =   []
    money  =   []

    for row in data:
        print(row)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    globals()[sys.argv[1]]()