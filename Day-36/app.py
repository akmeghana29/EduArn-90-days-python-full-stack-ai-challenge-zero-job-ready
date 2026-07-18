from flask import Flask, render_template, request, redirect, url_for
import json
from pathlib import Path

app = Flask(__name__)

FILE = "notes.json"

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=2)

@app.route("/")
def index():
    notes = load()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()
    if title and content:
        notes = load()
        notes.append({"id": len(notes) + 1, "title": title, "content": content})
        save(notes)
    return redirect(url_for("index"))

@app.route("/delete/<int:note_id>")
def delete(note_id):
    notes = load()
    notes = [n for n in notes if n["id"] != note_id]
    save(notes)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
