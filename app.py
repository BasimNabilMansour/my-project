from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Git", "completed": True},
    {"id": 2, "title": "Learn CI/CD", "completed": False},
    {"id": 3, "title": "Build a project", "completed": False}
]


@app.route("/")
def home():
    return "Task Manager API is running!"


@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True)