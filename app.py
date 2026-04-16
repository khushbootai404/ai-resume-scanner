from database import init_db, insert_resume, get_resumes
from flask import Flask, render_template, request, redirect, url_for, session
import flask
import os
from utils.parser import extract_text
from utils.matcher import match_resume

app = flask.Flask(__name__)
app.secret_key = "supersecretkey"

init_db()

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect(url_for("login"))

    saved_data = get_resumes()

    results = []
    for r in saved_data:
        results.append({
            "name": r[0],
            "score": r[1]
        })

    return flask.render_template("index.html", results=results)

app.secret_key = "supersecretkey"
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # simple hardcoded login (we upgrade later)
        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return "Invalid Credentials"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()
