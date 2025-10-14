from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask, jsonify, render_template
from joke.tech_jokes import generate_joke
from os import getenv


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

def about():
    return render_template("about.html")

def contact():
    return render_template("contact.html")


@app.route("/api/tech-joke", methods=["GET"])
def joke():
    return jsonify({"joke": generate_joke()})


if __name__ == "__main__":
    load_dotenv()
    is_debug_mode = getenv("is_debug_mode", "False") == "True"
    app.run(debug=is_debug_mode)
