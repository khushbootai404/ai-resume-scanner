print("🔥 THIS IS THE REAL FILE RUNNING 🔥")

from flask import Flask, render_template, request, redirect, url_for, session
import os

from database import init_db, insert_resume, get_resumes, create_user, get_user
from utils.parser import extract_text
from utils.matcher import match_resume

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Initialize DB
init_db()

# Upload config
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# 🏠 MAIN ROUTE
# =========================
@app.route("/", methods=["GET", "POST"])
def index():

    if "user" not in session:
        return redirect(url_for("login"))

    score = None

    if request.method == "POST":
        file = request.files.get("resume")
        job_desc = request.form.get("job_desc")

        if file and job_desc:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            resume_text = extract_text(file_path)
            score = match_resume(resume_text, job_desc)

            # ✅ GO TO RESULT PAGE
            return render_template("result.html", score=score)

    # 👇 ONLY for first load
    return render_template("index.html")

# =========================
# 🔐 LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user(username, password)

        if user:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return "Invalid credentials"

    return render_template("login.html")


# =========================
# 🆕 SIGNUP
# =========================
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            create_user(username, password)
            return redirect(url_for("login"))
        except:
            return "User already exists"

    return render_template("signup.html")

# =========================
# 🚪 LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# =========================
# 🚀 RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)