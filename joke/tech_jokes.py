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
The computer rebooted itself — and then displayed '404: life not found.'
"""


random.seed(time.time())


def generate_joke() -> str:
    """
    Generate a random, simple tech joke.

    The joke is context-aware: subjects, actions, and punchlines are paired more meaningfully.

    Returns:
        str: A randomly generated tech joke.
    """

    subjects_actions = {
        "programmer": [
            "tried to debug",
            "tried to commit",
            "tried to push",
            "wrote a function that",
            "tried to merge",
            "forgot a semicolon in",
        ],
        "computer": [
            "rebooted itself",
            "ran out of memory",
            "displayed an error",
            "started overclocking",
        ],
        "AI": [
            "made a decision",
            "generated a meme",
            "tried to understand emotions",
            "wrote poetry",
        ],
        "server": [
            "went down unexpectedly",
            "handled too many requests",
            "refused connections",
            "updated silently",
        ],
        "router": [
            "dropped packets",
            "restarted unexpectedly",
            "changed IP address",
            "lost connection",
        ],
        "keyboard": [
            "refused input",
            "typed on its own",
            "went on strike",
            "sent random characters",
        ],
        "robot": [
            "asked for a coffee break",
            "danced unexpectedly",
            "ignored commands",
            "learned a new skill",
        ],
        "bug": [
            "hid in the code",
            "caused chaos",
            "multiplied quickly",
            "disguised itself as a feature",
        ],
    }

    punchlines = {
        "programmer": [
            "but forgot what they were doing.",
            "and then asked for coffee.",
            "so it returned True anyway.",
            "and the code compiled magically.",
        ],
        "computer": [
            "and then displayed '404: life not found.'",
            "but it only beeped.",
            "so it froze in thought.",
            "and then restarted like nothing happened.",
        ],
        "AI": [
            "and confused everyone.",
            "but ended up writing a poem.",
            "so it claimed victory.",
            "and then asked existential questions.",
        ],
        "server": [
            "and everyone panicked.",
            "but handled it gracefully.",
            "so logs filled up quickly.",
            "and then crashed politely.",
        ],
        "router": [
            "and no packets survived.",
            "but the internet stayed slow.",
            "so it lost its mind.",
            "and everyone blamed Wi-Fi.",
        ],
        "keyboard": [
            "and typed random letters.",
            "but nobody noticed.",
            "so CAPS LOCK was triggered.",
            "and it became a secret agent.",
        ],
        "robot": [
            "and took a selfie.",
            "but forgot how to walk.",
            "so it danced instead.",
            "and reported a bug in humans.",
        ],
        "bug": [
            "and no one could find it.",
            "so it lived happily in production.",
            "and became a legendary feature.",
            "but got squashed eventually.",
        ],
    }

    templates = [
        "Why did the {subj} {act}? {punch}",
        "The {subj} {act} — {punch}",
        "When a {subj} {act}, {punch}",
        "Ever seen a {subj} {act}? {punch}",
        "{subj.capitalize()} {act}, and guess what? {punch}",
    ]

    subj = random.choice(list(subjects_actions.keys()))
    act = random.choice(subjects_actions[subj])
    punch = random.choice(punchlines[subj])

    joke = random.choice(templates).format(subj=subj, act=act, punch=punch)

    return joke


if __name__ == "__main__":
    print(generate_joke())
