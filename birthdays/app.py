import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month =  int(request.form.get("month"))
        day = int(request.form.get("day"))
        # TODO: Add the user's entry into the database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        print("successful insertion into database")
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        rows = db.execute("SELECT * from birthdays;")
        return render_template("index.html", rows=rows)

@app.route("/delist", methods=["POST"])
def delist():

    # Forget birthday
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")

@app.route("/update", methods=["GET","POST"])
def update():

    if request.method == "GET":
        id =  request.args.get("id")
        print(f'Get request id: {id}')
        return render_template("update.html", id=id)

    # Modify birthday
    if request.method =="POST":

        formid = int(request.form.get("id"))
        fullname = request.form.get("name")
        bdaymonth = int(request.form.get("month"))
        bdayday = int(request.form.get("day"))
        db.execute("""UPDATE birthdays SET name=?, month=?, day=? WHERE id =?""", fullname, bdaymonth, bdayday, formid)
        return redirect("/")