

from flask import Flask, request, redirect, url_for, render_template_string
import sqlite3

app = Flask(__name__)

# Database setup

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            email TEXT
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


# Home page - View students
@app.route("/")
def index():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()

    html = """
    <h1>Student Management System</h1>
    <a href='/add'>Add Student</a>
    <br><br>
    <table border='1' cellpadding='10'>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>Course</th>
            <th>Email</th>
            <th>Actions</th>
        </tr>
        {% for s in students %}
        <tr>
            <td>{{s[0]}}</td>
            <td>{{s[1]}}</td>
            <td>{{s[2]}}</td>
            <td>{{s[3]}}</td>
            <td>{{s[4]}}</td>
            <td>
                <a href='/update/{{s[0]}}'>Edit</a>
                <a href='/delete/{{s[0]}}'>Delete</a>
            </td>
        </tr>
        {% endfor %}
    </table>
    """

    return render_template_string(html, students=students)


# Add student
@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        email = request.form["email"]

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
            (name, age, course, email),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    html = """
    <h2>Add Student</h2>
    <form method='post'>
        Name: <input type='text' name='name'><br><br>
        Age: <input type='number' name='age'><br><br>
        Course: <input type='text' name='course'><br><br>
        Email: <input type='email' name='email'><br><br>
        <input type='submit' value='Add Student'>
    </form>
    <br>
    <a href='/'>Back</a>
    """

    return render_template_string(html)


# Delete student
@app.route("/delete/<int:id>")
def delete_student(id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# Update student
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_student(id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        email = request.form["email"]

        cursor.execute(
            """
            UPDATE students
            SET name=?, age=?, course=?, email=?
            WHERE id=?
            """,
            (name, age, course, email, id),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cursor.fetchone()
    conn.close()

    html = """
    <h2>Update Student</h2>
    <form method='post'>
        Name: <input type='text' name='name' value='{{student[1]}}'><br><br>
        Age: <input type='number' name='age' value='{{student[2]}}'><br><br>
        Course: <input type='text' name='course' value='{{student[3]}}'><br><br>
        Email: <input type='email' name='email' value='{{student[4]}}'><br><br>
        <input type='submit' value='Update Student'>
    </form>
    <br>
    <a href='/'>Back</a>
    """

    return render_template_string(html, student=student)


if __name__ == "__main__":
    app.run(debug=True)



