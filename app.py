from database.functions import ORM
from flask import Flask, render_template, request, redirect, url_for
import hashlib

orm = ORM()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/home")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
        app.logger.error(email)
        return redirect(url_for('profile'))
    return render_template('login.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
        username = request.form['name']
        app.logger.error(email)
        app.logger.error(password)
        
        if orm.GetUserByEmail(email) is not None:
            orm.AddUser(email_=email, username_=username, password_=password)

        return redirect(url_for('profile'))
    return render_template('signup.html')


@app.route("/logout")
def logout():
    return '<h1>:Log out</h1>'


@app.route("/profile")
def profile():
    return render_template('profile.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
