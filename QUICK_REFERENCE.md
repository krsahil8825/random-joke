# Quick Reference Guide

## For Developers

### Project Structure
```
random-joke/
├── app.py                  # Flask application (web server & API routes)
├── joke/                   # Joke package
│   ├── __init__.py        # Package interface with convenience functions
│   ├── family_jokes.py    # Family-friendly joke generator
│   └── tech_jokes.py      # Tech joke generator
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # Project documentation
```

### Quick Start

```bash
# Clone and setup
git clone https://github.com/krsahil8825/random-joke.git
cd random-joke

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# source .venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure (optional)
cp .env.example .env

# Run the application
python app.py
```

### Using the Joke Package

```python
# Method 1: Import specific functions
from joke import get_family_joke, get_tech_joke, get_random_joke

print(get_family_joke())           # Family joke
print(get_tech_joke())             # Tech joke
print(get_random_joke())           # Random category
print(get_random_joke('tech'))     # Specific category

# Method 2: Import the module
import joke

print(joke.get_family_joke())
print(joke.CATEGORIES)             # ['family', 'tech']
print(joke.__version__)            # '1.0.0'

# Method 3: Direct module access (legacy)
from joke import tech_jokes, family_jokes

print(tech_jokes.generate_joke())
print(family_jokes.generate_joke())
```

### API Endpoints

| Endpoint | Method | Description | Example Response |
|----------|--------|-------------|------------------|
| `/api/random-joke` | GET | Random joke from any category | `{"joke": "..."}` |
| `/api/tech-joke` | GET | Tech/programming joke | `{"joke": "..."}` |
| `/api/family-joke` | GET | Family-friendly joke | `{"joke": "..."}` |

### Testing API Locally

```bash
# Using curl
curl http://127.0.0.1:5000/api/random-joke
curl http://127.0.0.1:5000/api/tech-joke
curl http://127.0.0.1:5000/api/family-joke

# Using PowerShell
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/random-joke
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/tech-joke
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/family-joke
```

### Adding a New Joke Category

1. **Create module**: `joke/science_jokes.py`
   ```python
   def generate_joke() -> str:
       """Generate a random science joke."""
       jokes = [
           "Why did the scientist...",
           "What do you call...",
       ]
       return random.choice(jokes)
   ```

2. **Update package**: `joke/__init__.py`
   ```python
   from .science_jokes import generate_joke as _science_joke
   
   CATEGORIES = ['family', 'tech', 'science']
   
   def get_science_joke() -> str:
       return _science_joke()
   ```

3. **Add route**: `app.py`
   ```python
   @app.route("/api/science-joke", methods=["GET"])
   def science_joke():
       return jsonify({"joke": get_science_joke()})
   ```

4. **Update homepage**: Add to `alljokes_name_and_url` list in `home()` function

### Common Tasks

#### View API Documentation
```bash
# Generate and serve documentation
pdoc serve joke/* app
# Visit: http://localhost:8080
```

#### Run in Debug Mode
```bash
# Set in .env file
is_debug_mode=True

# Or set environment variable directly
$env:is_debug_mode="True"; python app.py  # PowerShell
export is_debug_mode=True && python app.py  # Bash
```

#### Deploy to Production
```bash
# Use a production WSGI server
pip install gunicorn  # Linux/macOS
pip install waitress  # Windows

# Run with Gunicorn (Linux/macOS)
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# Run with Waitress (Windows)
waitress-serve --host=0.0.0.0 --port=8000 app:app
```

### Package API Reference

#### Functions

- **`get_family_joke() -> str`**
  - Returns a random family-friendly joke
  - No parameters required

- **`get_tech_joke() -> str`**
  - Returns a random tech/programming joke
  - No parameters required

- **`get_random_joke(category: Optional[str] = None) -> str`**
  - Returns a random joke
  - Parameters:
    - `category` (optional): 'family', 'tech', or None for random
  - Raises: `ValueError` if invalid category

#### Constants

- **`CATEGORIES`**: List of available joke categories `['family', 'tech']`
- **`__version__`**: Package version string `'1.0.0'`
- **`__author__`**: Package author `'krsahil8825'`

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `is_debug_mode` | `False` | Enable Flask debug mode (`True`/`False`) |

### Dependencies

Core dependencies from `requirements.txt`:
- **Flask** (3.1.2) - Web framework
- **flask-cors** (6.0.1) - CORS support
- **python-dotenv** (1.1.1) - Environment variable management

Development dependencies:
- **pdoc** (15.0.4) - Documentation generator

### Troubleshooting

**Port already in use:**
```python
# Change port in app.py
if __name__ == "__main__":
    app.run(debug=is_debug_mode, port=8000)
```

**Module not found error:**
```bash
# Ensure you're in the correct directory
cd random-joke

# Ensure virtual environment is activated
.\.venv\Scripts\Activate.ps1
```

**CORS issues:**
- CORS is enabled by default via `flask-cors`
- Modify `app.py` if you need to restrict origins

### Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [REST API Best Practices](https://restfulapi.net/)

### Support

- **Issues**: [GitHub Issues](https://github.com/krsahil8825/random-joke/issues)
- **Discussions**: Open a GitHub Discussion for questions
- **Contributing**: See [CONTRIBUTING](README.md#contributing) section in README
