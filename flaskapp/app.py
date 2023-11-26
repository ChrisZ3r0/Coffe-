from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.features import readdata as rd
from src.features.read import read_id_for_server as serverread

app = Flask(__name__, static_folder='../Weblap/static')
app.secret_key = 'key'
template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Weblap'))

app.template_folder = template_path



@app.route('/')
def default(): 
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/userlog')
def userlog():
    return render_template('userlog.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/user')
def user():
    # Retrieve user information from the session
    user_data = session.get('user_data')

    if user_data:
        # Pass user-specific data to the template
        return render_template('user.html', user_data=user_data)
    else:
        # Redirect to the login page if user information is not found in the session
        return redirect(url_for('userlog'))


@app.route('/logscreen')
def logscreen():
    return render_template('logscreen.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/adminlog')
def adminlog():
    return render_template('adminlog.html')


@app.route('/login/user', methods=['POST'])
def userlogin():
    _, cardnumber, password, money, name = rd.load_users_db()

    user_credentials = {key: (p, m, n) for key, p, m, n in zip(cardnumber, password, money, name)}

    # Retrieve the username and password from the form
    page_username = request.form.get('username')
    page_password = request.form.get('password')

    # Check the credentials against the database
    if page_username in user_credentials and user_credentials[page_username][0] == page_password:
        # Store user information in the session
        session['user_id'] = page_username
        session['user_data'] = {
            'name': user_credentials[page_username][2],
            'money': user_credentials[page_username][1],
            'cardnumber': page_username
        }

        # Redirect to user.html if the credentials are correct
        return redirect(url_for('user'))
    else:
        # Redirect to a login error page or handle authentication failure
        return 'Wrong username or password, please try'


@app.route('/login/admin', methods=['POST'])
def adminlogin():

    cardnumber   =   []
    password  =   []

    _,cardnumber,password = rd.load_admin_db()
    admin_credentials = {key: value for key, value in zip(cardnumber, password)}

    # Retrieve the username and password from the form
    page_username = request.form.get('username')
    page_password = request.form.get('password')

    # Check the credentials against the database (replace with your actual database logic)
    if page_username in admin_credentials and admin_credentials[page_username] == page_password:
        # Redirect to user.html if the credentials are correct
        return render_template('admin.html')
    else:
        # Redirect to a login error page or handle authentication failure
        return 'Wrong username or password, please try'

@app.route('/adminadduser', methods=['GET', 'POST'])
def adminadduser():
    if request.method == 'POST':
        # Form was submitted, process the data
        name = request.form.get('nev')
        cardnumber = request.form.get('card')
        birth_date = request.form.get('date')
        money = request.form.get('money')

        # Extract RFID value from the form submission
        rfidnumber = request.form.get('rfidForMoney')

        # Check if the card number is already in use
        if rd.is_card_number_in_use(rfidnumber):

        # Now you can use these variables as needed
            print(f"Name: {name}, Card: {cardnumber}, Birth Date: {birth_date}, RFIDnumber: {rfidnumber}, Money: {money}")
        
        # Continue with the registration process
            rd.add_to_users(rfidnumber, cardnumber, birth_date, money, name)

        # Add your logic to save the data or perform other actions
        # Here we can call the function to add it to the database
        else:
            return 'User is existing in the database'

    return render_template('admin.html')

@app.route('/read_rfid', methods=['POST'])
def read_rfid():
    # Add your RFID reading logic here
    # You can call your Python function or interact with your RFID reader
    new_user_id = serverread()
    # Return a response to the client
    return jsonify({"rfid": new_user_id}) 

@app.route('/addmoney', methods=['POST'])
def addmoney():
    if request.method == 'POST':
        rfid_number = request.form.get('rfidForMoney')
        money_amount = request.form.get('moneyAmount')
        rate = request.form.get('rate')
        # Add your logic to update user's money based on rfid_number and money_amount
        # For example, you might have a function like set_user_money(rfid_number, money_amount)

                
        if rd.is_card_number_in_use(rfid_number):
            print( f"Added {money_amount} money to user with RFID: {rfid_number} with rate: {rate}")
            rd.add_item_to_moneypaid(rfid_number,rate,money_amount)
        else:
            return 'User is existing in the database'
    return render_template('admin.html')

    # Handle other HTTP methods or redirect as needed


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        # Clear user information from the session
        session.pop('user_id', None)
        session.pop('user_data', None)
        
        # Redirect to the login page
        return redirect(url_for('default'))
    else:
        # Handle GET request (optional)
        return 'Invalid request method for logout'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
