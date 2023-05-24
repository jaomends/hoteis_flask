from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return 'Página principal!!!!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return redirect('/')
        else:
            error = 'Credenciais inválidas. Tente novamente.'
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/user/<username>')
def profile(username):
    return 'User %s' % username


if __name__ == '__main__':
    app.run(debug=True)


# app.run(host='0.0.0.0') para abrir p/ outros computadores.
