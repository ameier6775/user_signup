from flask import Flask, request
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def get_title():
    question = input()
    answer =



@app.route('/add_user', methods=['POST'])
def add_user():
    new_account = request.form['new-account']

    escaped_account = cig.escape(new_account)

    if escaped_account == "":
        error = 'Please enter a valid email'
        return redirect('/?error='+ error)

    if escaped_account.len() < 3 or escaped_account.len() > 20:
        error_result = 'Please enter a valid email'
        return redirect('/?error=' + error)

    result = 'The user,' + escaped_account + ' has been added.'

    return result

@app.route('/save_password', method=['POST'])
def add_pass():
    new_password = request.form['new-password']

    escaped_password = cgi.escape(new_password)

    if escaped_password == "":
        error = 'Please enter a pasword'
        return redirect('/?error='+ error)

    if escaped_password.len() < 3 or escaped_password.len() > 20:
        error_result = 'Please enter a password'
        return redirect('/?error=' + error)

@app.route('/')
def index():
    error_arg = request.args.get('error')
    
    return render_primary('index.html', users=add_user())
