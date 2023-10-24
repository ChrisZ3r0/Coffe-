import sqlite3
import sys
import datetime

def load_coffee_db():
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM coffee")
    data = cursor.fetchall()

    coffeeid  =   []
    coffee_nam  =   []
    price   =   []
    available   =   []
    button_num  =   []

    for row in data:
        for i in range(len(row)):
            if i==0:
                cardid.append(row[i])
            elif i==1:
                coffee_nam.append(row[i])
            elif i==2:
                price.append(row[i])
            elif i==3:
                available.append(row[i])
            elif i==4:
                button_num.append(row[i])

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
        for i in range(len(row)):
            if i==0:
                cardid.append(row[i])
            elif i==1:
                cardnumber.append(row[i])
            elif i==2:
                password.append(row[i])

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
        for i in range(len(row)):
            if i==0:
                cardid.append(row[i])
            elif i==1:
                cardnumber.append(row[i])
            elif i==2:
                password.append(row[i])
                
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
        for i in range(len(row)):
            if i==0:
                buyid.append(row[i])
            elif i==1:
                date.append(row[i])
            elif i==2:
                cardid.append(row[i])
            elif i==3:
                coffetype.append(row[i])

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
        for i in range(len(row)):
            if i==0:
                cardid.append(row[i])
            elif i==1:
                date.append(row[i])
            elif i==2:
                rate.append(row[i])
            elif i==3:
                money.append(row[i])

    cursor.close()
    conn.close()

def getbuttons():
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM coffee WHERE button_num > 0 ORDER BY button_num ASC")
    data = cursor.fetchall()

    coffeeid  =   []
    coffee_nam  =   []
    price   =   []
    available   =   []
    button_num  =   []

    

    for row in data:
        for i in range(len(row)):
            if i==0:
                coffeeid.append(row[i])
            elif i==1:
                coffee_nam.append(row[i])
            elif i==2:
                price.append(row[i])
            elif i==3:
                available.append(row[i])
            elif i==4:
                button_num.append(row[i])

    cursor.close()
    conn.close()
    
    return coffeeid,coffee_nam,price,available,button_num

def lastsevendays():

    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    # Calculate the date 7 days ago from the current date

    seven_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    formatted_date = seven_days_ago.strftime('%Y.%m.%d')   
    # Execute the SQL query

    cursor.execute("SELECT * FROM coffeelog WHERE date >= ?", (formatted_date,))
    data = cursor.fetchall()
    for row in data:
        print(row)

def getcoffeetype():    

if __name__ == '__main__':
    globals()[sys.argv[1]]()