from flask import Flask, request, redirect, url_for, session, render_template_string
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# Create database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
conn.close()

register_page = """
<h2>Register</h2>
<form method="post">
Username: <input type="text" name="username"><br><br>
Password: <input type="password" name="password"><br><br>
<input type="submit" value="Register">
</form>
<a href="/login">Go to Login</a>
"""

login_page = """
<h2>Login</h2>
<form method="post">
Username: <input type="text" name="username"><br><br>
Password: <input type="password" name="password"><br><br>
<input type="submit" value="Login">
</form>
<a href="/register">Go to Register</a>
"""

home_page = """
<h2>Welcome {{user}}</h2>
<a href="/logout">Logout</a>
"""

@app.route('/')
def home():
    if 'user' in session:
        return render_template_string(home_page, user=session['user'])
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except:
            return "User already exists"

    return render_template_string(register_page)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"

    return render_template_string(login_page)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)