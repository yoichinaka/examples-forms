from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
from predict import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')

# Simple form handling using raw HTML forms
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        first_name = request.form['firstname']
        last_name = request.form['lastname']

        # Validate form data
        if len(first_name) == 0 or len(last_name) == 0:
            # Form data failed validation; try again
            error = "Please supply both first and last name"
        else:
            # Form data is valid; move along
            #return redirect(url_for('thank_you'))
            #return render_template('input.html')
            return redirect(url_for('input'))
    # Render the sign-up page
    return render_template('sign-up.html', message=error)

@app.route('/input', methods=['GET', 'POST'])
def input():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        home = request.form['home']
        away = request.form['away']
        print(home, away)
        # Validate form data
        if len(home) == 0 or len(away) == 0:
            # Form data failed validation; try again
            error = "Please supply both home and away name"
        else:

            #  !!!!!! make prediction
            result = predict (home, away)
            #result = home

            return render_template('input.html', text=result)
            #return redirect(url_for('result', text = home))
    # Render the sign-up page
    return render_template('input.html', message=error)

@app.route('/result')
def result():
    text ='GGG'
    return render_template('result.html', text = text)

# More powerful approach using WTForms
class RegistrationForm(Form):
    first_name = TextField('First Name')
    last_name = TextField('Last Name')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return redirect(url_for('thank_you'))

    return render_template('register.html', form=form, message=error)

# Run the application
#app.run(debug=True)
