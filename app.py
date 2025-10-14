"""
app.py

A simple Flask web application providing both web pages and API endpoints for
generating random tech and family-friendly jokes.

This application serves static HTML pages for home, about, and contact sections,
and exposes two API endpoints that return JSON-formatted jokes. It is configured
to support Cross-Origin Resource Sharing (CORS) and can be run in debug mode
based on an environment variable.

Modules:
--------
- os: To access environment variables.
- dotenv: To load environment variables from a .env file.
- flask: Core Flask module for creating web applications.
- flask_cors: To enable Cross-Origin Resource Sharing.
- joke.tech_jokes: Module containing functions to generate tech-related jokes.
- joke.family_jokes: Module containing functions to generate family-friendly jokes.

Flask Routes:
-------------
- GET "/":
    Serves the main homepage (index.html).

- GET "/about":
    Serves the about page (about.html).

- GET "/contact":
    Serves the contact page (contact.html).

- GET "/api/tech-joke":
    Returns a JSON response with a randomly generated tech joke.
    Example Response:
    {
        "joke": "The computer rebooted itself — and then displayed '404: life not found.'"
    }

- GET "/api/family-joke":
    Returns a JSON response with a randomly generated family-friendly joke.
    Example Response:
    {
        "joke": "Why did the cat chase the laser pointer? Because it wanted to catch up on dreams!"
    }

Environment Variables:
----------------------
- is_debug_mode (str, optional):
    Determines if Flask runs in debug mode. Accepts "True" or "False". Default is "False".

Usage:
------
1. Install dependencies:
    pip install flask flask_cors python-dotenv

2. Set environment variables in a `.env` file:
    is_debug_mode=True

3. Run the application:
    python app.py

4. Access in a browser:
    http://127.0.0.1:5000/       # Home page
    http://127.0.0.1:5000/api/tech-joke   # Tech joke API
    http://127.0.0.1:5000/api/family-joke # Family joke API

Notes:
------
- This application is designed for educational and fun purposes.
- The joke generation modules (`tech_jokes` and `family_jokes`) should follow
  the same interface with a `generate_joke()` function returning a string.
"""

from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask, jsonify, render_template
from joke import tech_jokes, family_jokes
from os import getenv

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    """Serve the home page (index.html)."""
    return render_template("index.html")


def about():
    """Serve the about page (about.html)."""
    return render_template("about.html")


def contact():
    """Serve the contact page (contact.html)."""
    return render_template("contact.html")


@app.route("/api/tech-joke", methods=["GET"])
def joke():
    """Return a JSON response with a random tech joke."""
    return jsonify({"joke": tech_jokes.generate_joke()})


@app.route("/api/family-joke", methods=["GET"])
def family_joke():
    """Return a JSON response with a random family-friendly joke."""
    return jsonify({"joke": family_jokes.generate_joke()})


if __name__ == "__main__":
    load_dotenv()
    is_debug_mode = getenv("is_debug_mode", "False") == "True"
    app.run(debug=is_debug_mode)
