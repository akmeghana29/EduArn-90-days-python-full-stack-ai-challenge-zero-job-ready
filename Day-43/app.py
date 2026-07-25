"""
Student API (CRUD)
- GET    /students          - get all students
- GET    /students/<id>     - get one student
- POST   /students          - add a student
- PUT    /students/<id>     - update a student
- DELETE /students/<id>     - delete a student

Test with Postman or Thunder Client (VS Code extension)
"""

from flask import Flask, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)

FILE = "students.json"

# ---------- Load and Save ----------

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

# ---------- GET all students ----------

@app.route("/students", methods=["GET"])
def get_all():
    students = load()
    return jsonify({"total": len(students), "students": students}), 200

# ---------- GET one student ----------

@app.route("/students/<int:student_id>", methods=["GET"])
def get_one(student_id):
    students = load()
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200

# ---------- POST - add student ----------

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name", "").strip()
    age  = data.get("age")
    grade = data.get("grade", "").strip()

    if not name or not age or not grade:
        return jsonify({"error": "name, age and grade are required"}), 400

    students = load()
    new_id = max((s["id"] for s in students), default=0) + 1

    new_student = {"id": new_id, "name": name, "age": age, "grade": grade}
    students.append(new_student)
    save(students)

    return jsonify({"message": "Student added", "student": new_student}), 201

# ---------- PUT - update student ----------

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    students = load()
    student = next((s for s in students if s["id"] == student_id), None)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    student["name"]  = data.get("name", student["name"])
    student["age"]   = data.get("age", student["age"])
    student["grade"] = data.get("grade", student["grade"])

    save(students)
    return jsonify({"message": "Student updated", "student": student}), 200

# ---------- DELETE student ----------

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    students = load()
    student = next((s for s in students if s["id"] == student_id), None)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    students.remove(student)
    save(students)
    return jsonify({"message": f"Student {student['name']} deleted"}), 200

# ---------- Run ----------

if __name__ == "__main__":
    app.run(debug=True)
