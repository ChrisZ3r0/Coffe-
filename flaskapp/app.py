from flask import Flask, render_template, request, redirect, url_for
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.features import readdata as rd
from src.features.read import read_id_for_server as serverread

app = Flask(__name__)

template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Weblap'))

app.template_folder = template_path



@app.route('/')
def default(): 
    return render_template('userlog.html')

@app.route('/userlog')
def userlog():
    return render_template('userlog.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/user')
def user():
    return render_template('user.html')

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
    
    cardnumber   =   []
    password  =   []

    _,cardnumber,password,_ = rd.load_users_db()

    user_credentials = {key: value for key, value in zip(cardnumber, password)}


    # Retrieve the username and password from the form
    page_username = request.form.get('username')
    page_password = request.form.get('password')

    # Check the credentials against the database (replace with your actual database logic)
    if page_username in user_credentials and user_credentials[page_username] == page_password:
        # Redirect to user.html if the credentials are correct
        return render_template('user.html')
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
        cardnumber = request.form.get('neptun')
        birth_date = request.form.get('date')

        # Now you can use these variables as needed
        print(f"Name: {name}, Neptun: {cardnumber}, Birth Date: {birth_date}")

        # Add your logic to save the data or perform other actions
        # Here we can call the function to add it to the database
    
    return render_template('admin.html')

@app.route('/read_rfid', methods=['POST'])
def read_rfid():
    # Add your RFID reading logic here
    # You can call your Python function or interact with your RFID reader
    new_user_id = serverread()
    # Return a response to the client
    return "RFID reading initiated on the server   ", new_user_id
 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
