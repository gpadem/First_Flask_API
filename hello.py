from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/<name>")
def user(name):
    return f"Hello Gülce!"


if __name__ == "__main__":
    app.run()
