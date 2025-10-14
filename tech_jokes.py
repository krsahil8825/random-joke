import random
import time

"""
tech_jokes.py

A simple Python module to generate random, family-friendly tech jokes.

This module provides a function `generate_joke()` that creates a single random
tech-related joke by combining a subject, an action, and a punchline. It is
intended for light-hearted, fun use and is suitable for general audiences.

Functions:
----------
generate_joke() -> str
    Returns a single randomly generated tech joke as a string.

Example:
--------
>>> from tech_jokes import generate_joke
>>> print(generate_joke())
Why did the programmer try to deploy? but it only returned a shrug.
"""


random.seed(time.time())


def generate_joke() -> str:
    """
    Generate a single random, simple tech joke. 

    The joke is constructed from a random subject, action, and punchline.
    
    Returns:
        str: A randomly generated tech joke.
    """

    subjects = [
        "programmer",
        "computer",
        "developer",
        "server",
        "router",
        "switch",
        "database",
        "cache",
        "debugger",
        "compiler",
        "editor",
        "keyboard",
        "mouse",
        "monitor",
        "battery",
        "cloud",
        "AI",
        "robot",
        "algorithm",
        "function",
        "variable",
        "loop",
        "thread",
        "process",
        "pixel",
        "bit",
        "byte",
        "script",
        "package",
        "module",
        "API",
        "endpoint",
        "security guard",
        "firewall",
        "hash",
        "blockchain",
        "emoji",
        "startup",
        "bug",
        "patch",
        "screenshot",
        "stack",
        "network",
        "ping",
        "backup",
        "log",
        "terminal",
        "command",
        "IDE",
        "toy robot",
    ]

    actions = [
        "tried to compile",
        "tried to reboot",
        "tried to ping",
        "tried to update",
        "tried to cache",
        "tried to debug",
        "tried to deploy",
        "tried to encrypt",
        "tried to optimize",
        "tried to render",
        "tried to connect",
        "tried to save",
        "tried to print",
        "tried to install",
        "tried to commit",
        "tried to push",
        "tried to pull",
        "tried to fork",
        "tried to merge",
        "tried to map",
    ]

    punchlines = [
        "but it only returned a shrug.",
        "and then it said '404: patience not found.'",
        "but it forgot to include feelings.",
        "so it flagged itself as 'todo'.",
        "and then it asked for coffee.",
        "but it needed a semicolon.",
        "and the output was 'try again later'.",
        "so it logged a complaint and went home.",
        "but it kept looping on a joke.",
        "and then it asked for a restart hug.",
        "and it claimed 'I am not a bug, I'm a feature'.",
        "but it only produced a tiny dot: '.'",
        "and then it printed 'Hello, world!' again.",
        "but the keyboard took the day off.",
        "so the screen showed a smiley face.",
        "and it answered in emoji.",
        "but the cloud said 'no storage left'.",
        "so it explained everything in comments.",
        "and then it compiled into a nap.",
        "so it returned True and went to lunch.",
    ]

    templates = [
        "Why did the {subj} {act}? {punch}",
        "The {subj} {act} — {punch}",
        "When a {subj} {act}, {punch}",
    ]

    joke = random.choice(templates).format(
        subj=random.choice(subjects),
        act=random.choice(actions),
        punch=random.choice(punchlines),
    )

    return joke


if __name__ == "__main__":
    print(generate_joke())
