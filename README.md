# Random-Joke

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

A tiny, open-source Flask application that serves random tech and family-friendly jokes via web pages and simple JSON APIs. Built for learning, demos, and quick integrations.

## Table of Contents

- [Highlights](#highlights)
- [Contents](#contents)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Running the App](#running-the-app)
- [API Endpoints](#api-endpoints)
- [Using the Joke Package](#using-the-joke-package)
- [Web Interface](#web-interface)
- [Extending the Application](#extending-the-application)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Highlights

- 🎭 Lightweight Flask app with multiple joke categories: tech, family, and random
- 🔌 Clean JSON REST API endpoints for easy integration
- 📦 Well-structured Python package with proper module organization
- 🎯 Type-hinted code with comprehensive documentation
- 🚀 Small, dependency-minimal codebase — great for beginners
- 🌐 Responsive web UI with multiple pages (home, about, contact)

## Contents

Repository structure (important files):

- `app.py` — Flask application and API routes
- `joke/__init__.py` — Enhanced joke package with convenience functions
- `joke/tech_jokes.py` — Tech joke generator module
- `joke/family_jokes.py` — Family-friendly joke generator module
- `templates/` — HTML templates for web pages
- `static/` — CSS, JavaScript, and images
- `requirements.txt` — Pinned dependencies
- `.env.example` — Example environment variables

## Requirements

- Python 3.8+
- Windows, macOS, or Linux

Install dependencies (suggested inside a virtual environment):

PowerShell (Windows):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

The app reads configuration from environment variables. Copy `.env.example` to `.env` and adjust if needed. The only supported variable is:

- `is_debug_mode` — set to `True` to enable Flask debug mode (default `False`).

Example `.env`:

```
is_debug_mode=True
```

## Running the app

Start the server from the repository root:

PowerShell (Windows):

```powershell
# ensure virtualenv is activated
python app.py
```

macOS / Linux:

```bash
python3 app.py
```

By default the app serves on http://127.0.0.1:5000

or 

> Use a production server like Waitress:

```bash
waitress-serve --listen=0.0.0.0:8000 app:app
```


## API Endpoints

The application exposes three REST API endpoints that return JSON-formatted jokes:

### 1. Random Joke (Any Category)
- **Endpoint:** `GET /api/random-joke`
- **Description:** Returns a random joke from any available category
- **Response:**
  ```json
  {
    "joke": "Why did the programmer quit his job? Because he didn't get arrays."
  }
  ```

### 2. Tech Jokes
- **Endpoint:** `GET /api/tech-joke`
- **Description:** Returns a technology/programming-themed joke
- **Response:**
  ```json
  {
    "joke": "The computer rebooted itself — and then displayed '404: life not found.'"
  }
  ```

### 3. Family Jokes
- **Endpoint:** `GET /api/family-joke`
- **Description:** Returns a family-friendly joke suitable for all ages
- **Response:**
  ```json
  {
    "joke": "Why did the cat chase the laser pointer? Because it wanted to catch up on dreams!"
  }
  ```

### Quick API Examples

**Using curl (Unix/macOS/WSL):**
```bash
# Get a random joke from any category
curl http://127.0.0.1:5000/api/random-joke

# Get a tech joke
curl http://127.0.0.1:5000/api/tech-joke

# Get a family joke
curl http://127.0.0.1:5000/api/family-joke
```

**Using PowerShell (Windows):**
```powershell
# Get a random joke from any category
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/random-joke

# Get a tech joke
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/tech-joke

# Get a family joke
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/family-joke
```

**Using Python:**
```python
import requests

# Get a random joke
response = requests.get('http://127.0.0.1:5000/api/random-joke')
print(response.json()['joke'])

# Get a specific category
tech_joke = requests.get('http://127.0.0.1:5000/api/tech-joke').json()
print(tech_joke['joke'])
```

## Using the Joke Package

The `joke` package has been enhanced with a clean, intuitive API for generating jokes programmatically.

### Package Features

- **Type-hinted functions** for better IDE support
- **Comprehensive docstrings** with examples
- **Error handling** for invalid categories
- **Public API** defined via `__all__`
- **Package metadata** (`__version__`, `__author__`, etc.)

### Import and Usage

```python
# Import the convenience functions
from joke import get_family_joke, get_tech_joke, get_random_joke

# Get a family-friendly joke
family_joke = get_family_joke()
print(family_joke)
# Output: "Why did the dog chase its tail? And everyone joined in the fun."

# Get a tech joke
tech_joke = get_tech_joke()
print(tech_joke)
# Output: "The programmer tried to debug — but forgot what they were doing."

# Get a random joke from any category
random_joke = get_random_joke()
print(random_joke)

# Get a random joke from a specific category
tech_joke = get_random_joke('tech')
family_joke = get_random_joke('family')

# Access available categories
from joke import CATEGORIES
print(CATEGORIES)  # ['family', 'tech']

# Check package version
from joke import __version__
print(__version__)  # 1.0.0
```

### Available Functions

| Function | Description | Returns |
|----------|-------------|---------|
| `get_family_joke()` | Generate a family-friendly joke | `str` |
| `get_tech_joke()` | Generate a tech/programming joke | `str` |
| `get_random_joke(category=None)` | Generate a joke (optionally specify category) | `str` |

### Error Handling

```python
from joke import get_random_joke

try:
    joke = get_random_joke('invalid')
except ValueError as e:
    print(e)
    # Output: "Invalid category 'invalid'. Choose from: family, tech"
```

## Development notes

- The joke generator modules expose a `generate_joke()` function that returns a string. You can add more jokes or categories by following the same pattern.
- The `joke/__init__.py` provides a unified interface with convenience functions for easy access to all joke categories.
- Keep the API stable: responses are JSON objects with a single `joke` field.
- All public functions include type hints and comprehensive docstrings.

## Web Interface

The application includes a responsive web interface with the following pages:

- **Home (`/`)** — Landing page displaying all available joke categories and API endpoints
- **About (`/about`)** — Information about the project
- **Contact (`/contact`)** — Contact information

Access the web interface by visiting `http://127.0.0.1:5000/` in your browser after starting the server.

## Extending the Application

### Adding a New Joke Category

1. **Create a new module** in the `joke/` directory (e.g., `joke/science_jokes.py`):
   ```python
   def generate_joke() -> str:
       """Generate a random science joke."""
       # Your joke generation logic here
       return "Your science joke here"
   ```

2. **Update `joke/__init__.py`**:
   ```python
   from .science_jokes import generate_joke as _science_joke
   
   CATEGORIES = ['family', 'tech', 'science']
   
   def get_science_joke() -> str:
       """Generate a random science joke."""
       return _science_joke()
   
   # Update get_random_joke() to include the new category
   ```

3. **Add a Flask route** in `app.py`:
   ```python
   @app.route("/api/science-joke", methods=["GET"])
   def science_joke():
       """Return a JSON response with a random science joke."""
       return jsonify({"joke": get_science_joke()})
   ```

### Suggested Improvements

- ✅ Enhanced `joke` package with convenience functions
- ✅ Comprehensive documentation and type hints
- ✅ Web UI with multiple pages
- 📝 Add unit tests for the joke generators
- 📝 Add integration tests for API endpoints
- 📝 Implement joke rating/feedback system
- 📝 Add more joke categories (science, music, sports, etc.)
- 📝 Implement joke search functionality
- 📝 Add CI/CD pipeline with GitHub Actions

## Contributing

Contributions are welcome! Please open issues or pull requests with small, focused changes. 

### Contribution Guidelines

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feat/add-jokes
   # or
   git checkout -b fix/bug-description
   ```
3. **Make your changes:**
   - Follow the existing code style and patterns
   - Add type hints to new functions
   - Include comprehensive docstrings
   - Update documentation if needed
4. **Test your changes** thoroughly
5. **Commit with clear messages:**
   ```bash
   git commit -m "feat: add science jokes category"
   ```
6. **Push and open a pull request:**
   ```bash
   git push origin feat/add-jokes
   ```

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Write descriptive docstrings with examples
- Keep functions focused and single-purpose
- Use meaningful variable and function names

### Testing

Before submitting a PR, ensure:
- All existing functionality still works
- New features are properly tested
- No breaking changes unless discussed
- API responses maintain consistent format

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Author

Kumar Sahil

---

Enjoy the jokes! If you want help adding features, tests, or CI, open an issue and I can help.
