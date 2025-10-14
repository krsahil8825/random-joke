"""
family_jokes.py

A Python module to generate random, family-friendly jokes suitable for all ages.

This module provides a function `generate_joke()` that creates a single, random
joke by combining a subject, an action, and a punchline. The jokes are designed
to be light-hearted, humorous, and appropriate for children, families, or any
general audience. It uses templates to format the joke in a variety of styles,
ensuring that repeated calls produce different outputs.

Modules:
--------
- random: To randomly select subjects, actions, punchlines, and templates.
- time: To seed the random number generator with the current system time.

Functions:
----------
generate_joke() -> str
    Generate a single random family-friendly joke.

Usage:
------
>>> from family_jokes import generate_joke
>>> print(generate_joke())
Why did the cat take a nap? Because it wanted to catch up on dreams!

Structure:
----------
- subjects_actions: Dictionary mapping joke subjects (e.g., 'cat', 'dog', 'child')
  to lists of possible actions.
- punchlines: Dictionary mapping each subject to a list of corresponding punchlines.
- templates: List of string templates to format the joke with subject, action, and punchline.

Example Outputs:
----------------
- "Why did the dog chase its tail? And everyone joined in the fun."
- "Ever seen a child build a huge tower? And it fell down, but giggled anyway."
- "The grandma baked cookies — so the grandchildren laughed loudly."

Notes:
------
- The random number generator is seeded with the current system time to ensure
  varied jokes on each execution.
- The module is designed to be imported into web apps, chatbots, or other Python
  programs for generating family-friendly humor on-demand.
- To extend the joke library, simply add more subjects, actions, and punchlines
  to their respective dictionaries.
"""

import random
import time

# Seed random number generator
random.seed(time.time())


def generate_joke() -> str:
    """
    Generate a random, simple family-friendly joke.

    The function randomly selects a subject from the predefined list, chooses a
    corresponding action, and pairs it with a subject-appropriate punchline. The
    joke is then formatted using one of several template styles to produce a
    humorous, readable output.

    Returns:
        str: A randomly generated, family-friendly joke.

    Example:
    --------
    >>> from family_jokes import generate_joke
    >>> generate_joke()
    'Ever seen a cat take a nap? And then fell asleep immediately.'
    """
    subjects_actions = {
        "cat": [
            "chased the laser pointer",
            "took a nap",
            "knocked over the vase",
            "hid in the box",
        ],
        "dog": [
            "barked at the mailman",
            "chased its tail",
            "tried to sit on the sofa",
            "learned a new trick",
        ],
        "grandma": [
            "baked cookies",
            "told a story",
            "tried yoga",
            "joined a dance class",
        ],
        "child": [
            "built a huge tower",
            "painted the wall",
            "asked a million questions",
            "dressed up as a superhero",
        ],
        "teacher": [
            "gave a pop quiz",
            "told a joke",
            "forgot their marker",
            "danced in class",
        ],
        "bird": [
            "sang loudly",
            "stole breadcrumbs",
            "flew into the window",
            "built a nest",
        ],
    }

    punchlines = {
        "cat": [
            "because it wanted to catch up on dreams!",
            "and then fell asleep immediately.",
            "so the mouse laughed quietly.",
            "and everyone clapped for its courage.",
        ],
        "dog": [
            "but ended up chasing its tail forever.",
            "and everyone joined in the fun.",
            "so it became a local hero.",
            "and wagged happily all day.",
        ],
        "grandma": [
            "and everyone enjoyed a cookie!",
            "so the grandchildren laughed loudly.",
            "and joined her in the fun.",
            "because life is sweeter with sugar and love.",
        ],
        "child": [
            "and it fell down, but giggled anyway.",
            "so the cat ran away quickly.",
            "and parents were amazed.",
            "because superheroes always save the day.",
        ],
        "teacher": [
            "and the students cheered.",
            "but everyone laughed instead of studying.",
            "so pencils rolled everywhere.",
            "and the classroom became a dance floor.",
        ],
        "bird": [
            "and everyone smiled at the tiny musician.",
            "but it forgot where it built the nest.",
            "so feathers flew everywhere.",
            "and it became the neighborhood star.",
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
