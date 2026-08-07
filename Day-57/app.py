"""
Task Manager API (CRUD)

"""

from flask import Flask, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)

FILE = "tasks.json"

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/tasks", methods=["GET"])
def get_all():
    tasks = load()
    return jsonify({"total": len(tasks), "tasks": tasks}), 200

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_one(task_id):
    tasks = load()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    title = data.get("title", "").strip()
    if not title:
        return jsonify({"error": "title is required"}), 400

    tasks = load()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {
        "id": new_id,
        "title": title,
        "description": data.get("description", "").strip(),
        "status": "pending"
    }
    tasks.append(task)
    save(tasks)
    return jsonify({"message": "Task added", "task": task}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    task["title"]       = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["status"]      = data.get("status", task["status"])

    save(tasks)
    return jsonify({"message": "Task updated", "task": task}), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    save(tasks)
    return jsonify({"message": f"Task '{task['title']}' deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
