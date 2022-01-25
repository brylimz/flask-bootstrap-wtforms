from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, EmailField


EMAIL = "admin@email.com"
PASSWORD = "12345678"


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.data_required()])
    password = PasswordField('Password', [validators.data_required()])
    submit = SubmitField("Log In")


app = Flask(__name__)
app.secret_key = "some secret"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "123" and login_form.password.data == "123":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
