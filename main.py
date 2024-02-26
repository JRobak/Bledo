from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/main', methods=['post'])
def main():
    username = request.form['username']

    if not username:
        # return 'Nazwa nie może być pusta!' # jak zwrócić do strony logowania, chyba że sprawdzenie dać w html?
        username = 'noname'

    return redirect(url_for('account', username=username))


@app.route('/account/<username>')
def account(username):
    title = 'Ustawienia konta'
    return render_template('account.html', title=title, username=username)


@app.route('/login')
def login():
    title = 'Zaloguj się'
    return render_template('login.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)