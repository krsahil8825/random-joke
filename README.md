# Random-Joke

A tiny, open-source Flask application that serves random tech and family-friendly jokes via web pages and simple JSON APIs. Built for learning, demos, and quick integrations.

## Highlights

- Lightweight Flask app with two joke categories: tech and family.
- Returns JSON at API endpoints for easy consumption by other apps or services.
- Small, dependency-minimal codebase — great for beginners.

## Contents

Repository structure (important files):

- `app.py` — Flask application and API routes.
- `joke/tech_jokes.py` — tech joke generator.
- `joke/family_jokes.py` — family-friendly joke generator.
- `requirements.txt` — pinned dependencies.
- `.env.example` — example environment variables.

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

## API Endpoints

- GET `/api/tech-joke` — returns a JSON object with a tech joke.
- GET `/api/family-joke` — returns a JSON object with a family-friendly joke.

Example responses:

```json
{ "joke": "Why did the programmer quit his job? Because he didn't get arrays." }
```

Quick examples to call the API

curl (unix / macOS / WSL):

```bash
curl http://127.0.0.1:5000/api/tech-joke
```

PowerShell (Windows):

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/family-joke
```

## Development notes

- The joke generator modules expose a `generate_joke()` function that returns a string. You can add more jokes or categories by following the same pattern.
- Keep the API stable: responses are JSON objects with a single `joke` field.

Suggested small improvements:

- Add unit tests for the joke generators.
- Add a simple web UI listing endpoints and showing a random joke.

## Contributing

Contributions are welcome. Please open issues or pull requests with small, focused changes. A minimal contribution flow:

1. Fork the repository
2. Create a branch: `git checkout -b feat/add-jokes`
3. Implement and test your change
4. Open a pull request describing the change

Please keep changes small and include tests where relevant.

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Author

Kumar Sahil

---

Enjoy the jokes! If you want help adding features, tests, or CI, open an issue and I can help.
