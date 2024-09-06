from flask import Flask, render_template


app = Flask(__name__)
students = [{"id": 1, "name": "ahmad"}, {"id": 2, "name": "ali"},
            {"id": 3, "name": "omar"}]

@app.route("/")


def home():
    return render_template("index.html", students=students)

@app.route("/search/<int:id>")


def search(id):
    is_found = False
    target_student = None
    for student in students:
        if student['id'] == id:
            is_found = True
            target_student = student

    return render_template("search.html", is_found=is_found, target_student=target_student)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
