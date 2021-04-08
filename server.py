from datetime import datetime
from flask import Flask, jsonify, render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


@app.route("/movies")
def movies_page():
    return render_template("movies.html")


@app.route("/multiply", methods=["GET", "POST"])
def multiply_page():
    if request.method == "GET":
        return render_template("multiply.html")

    else:
        form_First = request.form["First number"]
        form_Second = request.form["Second number"]
        multiplication = int(form_First) * int(form_Second)
        return str(multiplication)


@app.route("/projects")
def projects_page():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)
