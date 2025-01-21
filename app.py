from flask import Flask, render_template, request, redirect, session
from db import Database
import api
import torch
from api import ner

app = Flask(__name__)
dbo = Database()

# Set a secret key for session handling
app.secret_key = 'your_secret_key'  # Change this to a more secure value in production

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=["POST"])
def perform_registration():
    name = request.form.get("user_ka_name")
    email = request.form.get("user_ka_email")
    password = request.form.get("user_ka_password")
    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html', message="Email already exists")

@app.route('/perform_login', methods=["POST"])
def perform_login():
    email = request.form.get("user_ka_email")
    password = request.form.get("user_ka_password")

    response = dbo.search(email, password)
    if response:
        session['logged_in'] = 1  # Mark the user as logged in
        return redirect('/profile')
    else:
        return render_template('login.html', message="Incorrect email/password")

@app.route('/profile')
def profile():
    if 'logged_in' in session and session['logged_in'] == 1:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner_page():
    if 'logged_in' in session and session['logged_in'] == 1:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner', methods=["POST"])
def perform_ner():
    if 'logged_in' not in session or session['logged_in'] != 1:
        return redirect('/')  # Redirect to login page if not logged in

    text = request.form.get("ner_text")
    response = ner(text)  # Call the ner function from api.py
    print(response)  # You can check the response in the console for debugging
    return render_template('ner.html', response=response)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
