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

    escaped_account = cgi.escape(new_account)
    escaped_password = cgi.escape(new_password)
    escaped_ver = cgi.escape(password_ver)
    escaped_email = cgi.escape(new_email)


    if escaped_account == "" or len(escaped_account) < 3 or len(escaped_account) > 20:
        error = 'That\'s not a valid username'
        return redirect('/?error='+ error)

    if escaped_password == "" or len(escaped_password) < 3 or len(escaped_password) > 20:
        error = 'That\'s not a valid password'
        return redirect('/?error='+ error)

    if escaped_password != escaped_ver:
        error = 'Passwords don\'t match'
        return redirect('/?error=' + error)

    if len(escaped_email) > 0:
        if "@" not in escaped_email or "." not in escaped_email or len(escaped_email) < 3 or len(escaped_email) > 20:
            error = 'That\'s not a valid email'
            return redirect('/?error=' + error)
        
    return render_template('welcome.html', result=escaped_account)

@app.route('/')
def index():
    error_arg = request.args.get('error')
    
    return render_template('index.html', error=error_arg)

app.run()