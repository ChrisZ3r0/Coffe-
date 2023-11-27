import sqlite3
import sys
from datetime import datetime,timedelta

def get_current_date():
    # Get the current date
    current_date = datetime.now()

    # Format the date as yyyy.mm.dd
    formatted_date = current_date.strftime('%Y.%m.%d')

    return formatted_date

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

def is_card_number_in_use(card_number):
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    # Check if the card number already exists in the users table
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE cardnumber = ?)", (card_number,))
    result = cursor.fetchone()[0]
    print(result)
    cursor.close()
    conn.close()

    if result==0:
        return True
    elif result ==1:
        return False

def load_users_db():
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    cardid  =   []
    cardnumber   =   []
    password  =   []
    money = []
    name = []
    for row in data:
        for i in range(len(row)):
            if i==0:
                cardid.append(row[i])
            elif i==1:
                cardnumber.append(row[i])
            elif i==2:
                password.append(row[i])
            elif i==3:
                money.append(row[i])
            elif i==4:
                name.append(row[i])

    cursor.close()
    conn.close()

    return cardid,cardnumber,password,money,name

def add_to_users(cardid, cardnumber, password, money, name):
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    # Insert new user into the users table
    cursor.execute("INSERT INTO users (id, cardnumber, password, money, Name) VALUES (?, ?, ?, ?, ?)",
                   (cardid, cardnumber, password, money, name))

    # Commit the changes and close the connection
    conn.commit()
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

    return cardid, cardnumber, password

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

def add_to_coffeelog(cardid, coffeetype):
    date = get_current_date()
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    # Insert new item into the coffelog table
    cursor.execute("INSERT INTO coffeelog (date, cardid, type) VALUES (?, ?, ?)",
                   (date, cardid, coffeetype))

    # Commit the changes and close the connection
    conn.commit()
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

def add_item_to_moneypaid(cardid, rate, money):
    date = get_current_date()
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    # Insert new item into the moneypaid table
    cursor.execute("INSERT INTO moneypaid (cardid, date, rate, money) VALUES (?, ?, ?, ?)",
                   (cardid, date, rate, money))

    cursor.execute("UPDATE users SET money = money + ? WHERE id = ?", (money, cardid))


    # Commit the changes and close the connection
    conn.commit()
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

    seven_days_ago = datetime.strptime(get_current_date(), '%Y.%m.%d') - timedelta(days=7)
    formatted_date = seven_days_ago.strftime('%Y.%m.%d')   
    # Execute the SQL query

    cursor.execute("SELECT date, COUNT(*) FROM coffeelog WHERE date >= ?  GROUP BY date", (formatted_date,))
    print('printing')
    chart_data = cursor.fetchall()
    print(chart_data)
    cursor.close()
    conn.close()
    return chart_data

def lastsevendays_withfilter(cardnumber):

    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE cardnumber = ? ", (cardnumber,))
    data = cursor.fetchone()
    userid=data[0]
 
    # Calculate the date 7 days ago from the current date

    seven_days_ago = datetime.strptime(get_current_date(), '%Y.%m.%d') - timedelta(days=7)
    formatted_date = seven_days_ago.strftime('%Y.%m.%d')   
    # Execute the SQL query

    cursor.execute("SELECT date, COUNT(*) FROM coffeelog WHERE date >= ? AND cardid = ? GROUP BY date", (formatted_date, userid))
    chart_data = cursor.fetchall()
    # print(chart_data)
    cursor.close()
    conn.close()

    return chart_data
def this_month_withfilter(cardnumber):

    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE cardnumber = ? ", (cardnumber,))
    data = cursor.fetchone()
    userid=data[0]
 
    # Calculate the date 7 days ago from the current date

    seven_days_ago = datetime.strptime(get_current_date(), '%Y.%m.%d') - timedelta(days=7)
    formatted_date = seven_days_ago.strftime('%Y.%m.%d')   
    # Execute the SQL query

    cursor.execute("SELECT date, COUNT(*) FROM coffeelog WHERE date >= ? AND cardid = ? GROUP BY date", (formatted_date, userid))
    chart_data = cursor.fetchall()
    print(chart_data)
    cursor.close()
    conn.close()

    return chart_data
def this_year_withfilter(cardnumber):

    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE cardnumber = ? ", (cardnumber,))
    data = cursor.fetchone()
    userid=data[0]
 
    # Calculate the date 7 days ago from the current date

    seven_days_ago = datetime.strptime(get_current_date(), '%Y.%m.%d') - timedelta(days=7)
    formatted_date = seven_days_ago.strftime('%Y.%m.%d')   
    # Execute the SQL query

    cursor.execute("SELECT date, COUNT(*) FROM coffeelog WHERE date >= ? AND cardid = ? GROUP BY date", (formatted_date, userid))
    chart_data = cursor.fetchall()
    print(chart_data)
    cursor.close()
    conn.close()

    return chart_data

def getcoffeetype(thetype):    

    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT coffee.id,coffee.coffee_name FROM coffeelog,coffee WHERE coffeelog.type == coffee.id")
    data = cursor.fetchall()

    for row in data:
        if(int(thetype) == row[0]):
            return row[1]

def getcoffeeprice():

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
    
    return price

def getcoffeetypebyname():

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
    
    return coffeeid

def checkcardid(rfidcardnum):
    isonlist = False

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

    for row in data:
        #print (row[0])
        if rfidcardnum == str(row[0]):
            isonlist=True
            break


    return isonlist

def checkcanbuy(buttonnumber, rfidcardnum):

    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT money FROM users WHERE id = ?", (rfidcardnum,))
    money_result = cursor.fetchone()
    money=money_result[0]
    print(money)
    cursor.close()
    conn.close()
    price=getcoffeeprice()
    coffename=getcoffeetypebyname()
    print(price[buttonnumber-1])
    coffeprice=price[buttonnumber-1]
    if  coffeprice <= money:
        #print("setmoney")
        set_user_money(rfidcardnum,coffeprice)
        # print(coffename[buttonnumber-1])
        add_to_coffeelog(rfidcardnum,coffename[buttonnumber-1])
        return True
    else:
        return False


def set_user_money(rfidcardnum,coffeprice):
    
    conn = sqlite3.connect('/home/pi/Coffe-/data/mydatabase.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (rfidcardnum,))    
    data = cursor.fetchone()

    if data:

        user_money = data[3]
        user_money -= coffeprice

        query = "UPDATE users SET money = ? WHERE id = ?"
        cursor.execute(query, (user_money, rfidcardnum))


        conn.commit()
        conn.close()

    else:
        conn.close()

    print('set')


if __name__ == '__main__':
    globals()[sys.argv[1]]