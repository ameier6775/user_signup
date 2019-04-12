from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/add_user', methods=['POST'])
def add_user():
    new_account = request.form['new-account']
    new_password = request.form['new-password']
    password_ver = request.form['password-verified']
    new_email = request.form['email-created']

    user_error = ""
    password_error = ""
    pass_val_error = ""
    email_error = ""

    errors = []
    names = []

    if new_account == "" or len(new_account) < 3 or len(new_account) > 20:
        user_error = 'That\'s not a valid username'
        errors.append(user_error)
        names.append(new_account)

    if new_password == "" or len(new_password) < 3 or len(new_password) > 20:
        password_error = 'That\'s not a valid password'
        errors.append(password_error)


    if new_password != password_ver:
        pass_val_error = 'Passwords don\'t match'
        errors.append(pass_val_error)


    if len(new_email) > 0:
        if "@" not in new_email or "." not in new_email or len(new_email) < 3 or len(new_email) > 20:
            email_error = 'That\'s not a valid email'
            errors.append(email_error)
            names.append(new_email)

    if len(errors) > 0:
        return render_template('index.html', user_error=user_error, password_error=password_error, pass_val_error=pass_val_error, email_error=email_error, new_account=new_account, new_email=new_email)
    else:
        return render_template('welcome.html', result=new_account)

@app.route('/')
def index():
    error_arg = request.args.get('error')
    
    return render_template('index.html', error=error_arg)

app.run()