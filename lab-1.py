from flask import Flask, render_template


app = Flask(__name__)
students = [{"id": 1, "name": "ahmad"}, {"id": 2, "name": "ali"},
            {"id": 3, "name": "omar"}]

@app.route("/")


def home():
    return render_template("index.html", students=students)

@app.route("/search/<int:id>")


def search(id):
    def search(id):
    return render_template('search.html', students=students, id=id)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
