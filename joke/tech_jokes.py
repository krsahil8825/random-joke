"""
tech_jokes.py

A Python module to generate random, family-friendly technology-themed jokes.

This module provides a function `generate_joke()` which creates a single, random
tech-related joke by combining a subject, an action, and a punchline. The jokes
are designed to be light-hearted, humorous, and suitable for general audiences,
including children and adults. The module uses templates to produce a variety
of joke formats.

Modules:
--------
- random: For random selection of subjects, actions, punchlines, and templates.
- time: To seed the random number generator with the current time.

Functions:
----------
generate_joke() -> str
    Generate a single, random, family-friendly tech joke. The joke is
    context-aware: actions and punchlines are matched with the subject to make
    the joke more coherent.

Usage:
------
>>> from tech_jokes import generate_joke
>>> print(generate_joke())
The computer rebooted itself — and then displayed '404: life not found.'

Structure:
----------
- subjects_actions: Dict mapping tech-related subjects (e.g., 'programmer', 'computer')
  to a list of possible actions.
- punchlines: Dict mapping subjects to lists of corresponding punchlines.
- templates: List of string templates to format the joke with subject, action, and punchline.

Example Output:
---------------
- "Why did the programmer try to debug? But forgot what they were doing."
- "The AI generated a meme — and confused everyone."
- "Ever seen a robot dance unexpectedly? So it danced instead."

Notes:
------
- The random seed is set using the current system time to ensure varied jokes on
  each execution.
- This module can be imported into other Python applications, such as web APIs,
  chatbots, or desktop apps, to provide on-demand tech jokes.
- To extend the joke library, simply add more subjects, actions, and punchlines
  to the respective dictionaries.
"""

import random
import time

random.seed(time.time())


def generate_joke() -> str:
    """
    Generate a random, simple tech joke.

    This function selects a random tech-related subject, then chooses a corresponding
    action and punchline to form a coherent and humorous joke. The final joke is
    formatted using one of several template styles to increase variety.

    Returns:
        str: A randomly generated tech joke.

    Example:
    --------
    >>> from tech_jokes import generate_joke
    >>> generate_joke()
    'The computer ran out of memory — and then restarted like nothing happened.'
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
        "The {subj} {act} - {punch}",
        "When a {subj} {act}, {punch}",
        "Ever seen a {subj} {act}? {punch}",
        "{subj} {act}, and guess what? {punch}",
    ]

    subj = random.choice(list(subjects_actions.keys()))
    act = random.choice(subjects_actions[subj])
    punch = random.choice(punchlines[subj])

    joke = random.choice(templates).format(subj=subj, act=act, punch=punch)

    return joke.capitalize()


if __name__ == "__main__":
    print(generate_joke())
