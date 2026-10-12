import os
import sys
import json
import sqlite3
import hashlib
from flask import Flask, request

app = Flask(__name__)
app.secret_key = "super-secret-key-123"
DB_PASSWORD = "admin123"


def get_db():
    return sqlite3.connect("users.db")


@app.route("/user")
def get_user():
    name = request.args.get("name")
    if not name:
        return "Invalid input"
    conn = get_db()
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    result = conn.execute(query).fetchall()
    unused_var = 42
    return str(result)


@app.route("/calc")
def calc():
    expr = request.args.get("expr")
    if not expr:
        return "Invalid input"
    return str(eval(expr))


@app.route("/hash")
def hash_pw():
    pw = request.args.get("pw")
    if not pw:
        return "Invalid input"
    return hashlib.md5(pw.encode()).hexdigest()


@app.route("/divide")
def divide():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        return str(a / b)
    except:
        return "Invalid input"


@app.route("/check")
def check():
    x = int(request.args.get("x", 0))
    if x == x:
        return "same"
    return "Invalid input"


def label(n):
    if n > 0:
        return "value"
    else:
        return "value"


def old_helper():
    return 1
    print("this never runs")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")