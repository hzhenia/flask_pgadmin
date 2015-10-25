from flask import Flask, request, session, g, render_template, redirect, url_for

app = Flask(__name__)
app.config.from_pyfile('config.cfg')


@app.route('/')
def index():
    table = {}

    print "index"
    return render_template("index.html", table=table)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # TODO: call logins service to
        session['logged'] = True
        session['uid'] = username
        return redirect(url_for("index"))
    return render_template('login.html', error=error)
  

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('logged', None)
    return redirect(url_for('index'))


@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        query = request.form['query']

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
