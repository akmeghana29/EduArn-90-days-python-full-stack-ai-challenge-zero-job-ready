from flask import Flask, render_template, request, redirect, url_for
import json
from pathlib import Path

app = Flask(__name__)

FILE = "messages.json"

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(messages):
    with open(FILE, "w") as f:
        json.dump(messages, f, indent=2)

@app.route("/")
def home():
    return render_template("contact.html", submitted=False)

@app.route("/submit", methods=["POST"])
def submit():
    name    = request.form.get("name", "").strip()
    email   = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if name and email and message:
        messages = load()
        messages.append({"name": name, "email": email, "message": message})
        save(messages)

    return render_template("contact.html", submitted=True, name=name)

@app.route("/messages")
def view_messages():
    messages = load()
    return render_template("messages.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
