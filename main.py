from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, EmailField


class LoginForm(FlaskForm):
    email = EmailField('Email', [validators.data_required(), validators.Email()])
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
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
