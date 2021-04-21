from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = "gkffh"


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to logot</a></b>"

    return "user are not logged in <br><a href = '/login'>" + "click here to log in</br></a>"


@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return'''
        <form action = "" method = "post">
            <p><input type = 'text' name = username></p>
            <p><input type = 'submit' value = Login></p>
        </form>
    '''


@app.route('/logout', methods = ['GET','POST'])
def logout():
    # 세션 내에 username 이 존재하면 제거한다.
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)