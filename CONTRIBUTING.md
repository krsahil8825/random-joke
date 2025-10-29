# Contributing to Random-Joke

Thank you for your interest in contributing to **Random-Joke**, an open-source Flask app and Python package that generates family-friendly and tech jokes!

We welcome contributions from developers of all experience levels — from beginners to experts.

## Table of Contents

-   [How to Contribute](#how-to-contribute)
-   [Branch Naming Convention](#branch-naming-convention)
-   [Commit Message Format](#commit-message-format)
-   [Code Style](#code-style)
-   [Testing](#testing)
-   [Documentation](#documentation)
-   [Pull Request Guidelines](#pull-request-guidelines)
-   [License](#license)

## How to Contribute

1. **Fork the repository**

2. **Clone your fork locally**

    ```bash
    git clone https://github.com/<your-username>/random-joke.git
    cd random-joke
    ```

3. **Create a new branch**

    ```bash
    git checkout -b feat/add-new-jokes
    ```

4. **Make your changes**

    - Follow the [Code Style](#code-style)
    - Add type hints and docstrings
    - Test your code locally

5. **Commit your changes**

    ```bash
    git commit -m "feat: add new tech jokes with improved structure"
    ```

6. **Push to your fork**

    ```bash
    git push origin feat/add-new-jokes
    ```

7. **Open a Pull Request (PR)**

    - Go to the original repository on GitHub
    - Click “Compare & pull request”
    - Add a **clear title** and **detailed description**
    - Link any related issues if applicable


## Branch Naming Convention

Use descriptive names for your branches, starting with a category prefix:

| Type          | Example                           |
| ------------- | --------------------------------- |
| Feature       | `feat/add-family-jokes`           |
| Fix           | `fix/api-response-format`         |
| Documentation | `docs/update-readme`              |
| Refactor      | `refactor/improve-template-logic` |
| Test          | `test/add-unit-tests`             |


## Commit Message Format

Follow **Conventional Commit** style:

```
<type>: <short description>

[optional body]
```

**Types:**

-   `feat` – New feature
-   `fix` – Bug fix
-   `docs` – Documentation update
-   `style` – Code formatting, no logic change
-   `refactor` – Code restructure without behavior change
-   `test` – Add or modify tests

**Examples:**

```
feat: add new tech joke templates
fix: correct typo in router punchline
docs: update contributing guidelines
```

## Code Style

-   Follow [PEP 8](https://peps.python.org/pep-0008/) style guide.
-   Use **type hints** for all function parameters and return types.
-   Add **docstrings** with examples where appropriate.
-   Keep functions **focused and modular**.
-   Avoid unnecessary dependencies.

Example:

```python
def generate_joke() -> str:
    """Generate a random tech-themed joke."""
    return "The computer rebooted itself — and displayed '404: life not found.'"
```

## Testing

Before submitting a PR:

-   Run your code locally and ensure no syntax errors.
-   If applicable, write unit tests under a `tests/` directory.
-   Validate that joke generation returns valid strings and no runtime errors occur.

## Documentation

-   Update **README.md** if you introduce new features or modules.
-   Document all new functions with descriptive docstrings.
-   Keep comments meaningful and concise.

## Pull Request Guidelines

-   PR titles must be **clear and concise**.
-   PRs should address **one feature or fix at a time**.
-   Reference any related issue numbers (`Fixes #123`).
-   Ensure all code passes local testing.
-   Do **not** include unrelated file changes or personal debug prints.
-   Follow the **branch naming** and **commit format** rules.

If a pull request does not meet these requirements, maintainers may close it with feedback for revision.

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
