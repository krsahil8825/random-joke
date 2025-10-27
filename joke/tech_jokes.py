"""
tech_jokes.py

A Python module to generate random, family-friendly technology-themed jokes.

Features:
- generate_joke(): Produces a single tech joke using matched subjects, actions, and punchlines.
- Jokes are light-hearted, coherent, and accessible for all ages.
"""

import random
import time

random.seed(time.time())

def generate_joke() -> str:
    """
    Generate a random, family-friendly tech joke.

    Selects a tech subject, action, and punchline that fit together.
    The result is a single, naturally-worded joke.

    Returns:
        str: Randomly generated technology-themed joke.
    """
    subjects_actions = {
        "programmer": [
            "debugged their code",
            "committed changes",
            "pushed updates",
            "wrote a function",
            "merged branches",
            "forgot a semicolon",
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
            "changed its IP address",
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
            "But then realized it was a feature, not a bug.",
            "Turns out, coffee was the real solution.",
            "The code compiled magically, somehow.",
            "And then Googled the error for hours.",
        ],
        "computer": [
            "And then displayed '404: life not found.'",
            "It only beeped in existential dread.",
            "So it froze in deep thought.",
            "Then restarted like nothing happened.",
        ],
        "AI": [
            "It confused everyone except itself.",
            "Ended up writing a poem about its feelings.",
            "Claimed victory over humanity.",
            "Asked existential questions nobody could answer.",
        ],
        "server": [
            "Everyone panicked for five minutes.",
            "But it handled the mess gracefully.",
            "The logs filled up quickly.",
            "Then crashed politely, sending apologies.",
        ],
        "router": [
            "No packet survived.",
            "Still, the internet crawled along.",
            "It lost its mind and wandered off.",
            "Wi-Fi was blamed by everyone.",
        ],
        "keyboard": [
            "Typed random letters for fun.",
            "Nobody noticed the rebellion.",
            "Caps Lock got triggered infinitely.",
            "It became a secret agent in the matrix.",
        ],
        "robot": [
            "It took a selfie and posted it online.",
            "Forgot how to walk during an update.",
            "Started dancing instead of following orders.",
            "Reported a bug in humans.",
        ],
        "bug": [
            "No one could ever find it.",
            "It lived happily ever after in production.",
            "Became a legendary feature.",
            "Got squashed... eventually.",
        ],
    }

    # Templates ensure natural, grammatically correct phrasing
    templates = [
        "Why did the {subj} {act}? {punch}",
        "The {subj} {act}, and then {punch}",
        "What happens when a {subj} {act}? {punch}",
        "Ever seen a {subj} {act}? {punch}",
        "{subj.capitalize()} {act}. {punch}",
    ]

    subj = random.choice(list(subjects_actions.keys()))
    act = random.choice(subjects_actions[subj])
    punch = random.choice(punchlines[subj])

    joke = random.choice(templates).format(subj=subj, act=act, punch=punch)
    return joke[0].upper() + joke[1:]

if __name__ == "__main__":
    print(generate_joke())
