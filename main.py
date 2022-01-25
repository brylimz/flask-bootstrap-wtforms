from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.data_required()])
    password = PasswordField('Password', [validators.data_required()])
    submit = SubmitField("Log In")



app = Flask(__name__)
app.secret_key = "some secret"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
