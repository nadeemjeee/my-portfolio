from flask import Flask, render_template, request
import csv
import sqlite3

def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE
        )
    """)

    conn.commit()
    conn.close()


app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO contacts (name, email) VALUES (?, ?)",
            (name, email)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return f"{email} already exists. Duplicate not saved."

    conn.close()

    return render_template("contact.html", name=name, email=email)

@app.route("/contacts")
def contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, email FROM contacts")
    data = cursor.fetchall()

    conn.close()

    return render_template("contacts.html", contacts=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)