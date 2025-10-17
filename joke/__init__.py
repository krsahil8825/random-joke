"""
joke package
============

A Python package for generating random, family-friendly jokes across different categories.

This package contains modules for various joke categories:
- `family_jokes` — Family-friendly jokes suitable for all ages
- `tech_jokes` — Programming and technology-related jokes

Modules:
--------
- family_jokes: Contains family-friendly joke generation
- tech_jokes: Contains technology/programming joke generation

Functions:
----------
get_family_joke() -> str
    Generate a random family-friendly joke.

get_tech_joke() -> str
    Generate a random technology/programming joke.

get_random_joke(category: str = None) -> str
    Generate a random joke from a specific category or any category.

Usage:
------
>>> from joke import get_family_joke, get_tech_joke, get_random_joke
>>> print(get_family_joke())
>>> print(get_tech_joke())
>>> print(get_random_joke())  # Random category
>>> print(get_random_joke('tech'))  # Specific category

Example:
--------
>>> import joke
>>> print(joke.get_family_joke())
Why did the cat take a nap? Because it wanted to catch up on dreams!

>>> print(joke.get_tech_joke())
The programmer tried to debug — but forgot what they were doing.
"""

import random
from typing import Optional

from .family_jokes import generate_joke as _family_joke
from .tech_jokes import generate_joke as _tech_joke

# Package metadata
__version__ = '1.0.0'
__author__ = 'krsahil8825'
__description__ = 'A Python package for generating random, family-friendly jokes'
__all__ = [
    'get_family_joke',
    'get_tech_joke', 
    'get_random_joke',
    'CATEGORIES',
    '__version__'
]

# Available joke categories
CATEGORIES = ['family', 'tech']


def get_family_joke() -> str:
    """
    Generate a random family-friendly joke.
    
    Returns:
        str: A randomly generated family-friendly joke.
    
    Example:
        >>> joke = get_family_joke()
        >>> print(joke)
        Why did the dog chase its tail? And everyone joined in the fun.
    """
    return _family_joke()


def get_tech_joke() -> str:
    """
    Generate a random technology/programming joke.
    
    Returns:
        str: A randomly generated tech joke.
    
    Example:
        >>> joke = get_tech_joke()
        >>> print(joke)
        The computer rebooted itself — and then displayed '404: life not found.'
    """
    return _tech_joke()


def get_random_joke(category: Optional[str] = None) -> str:
    """
    Generate a random joke from a specific category or any category.
    
    Args:
        category (str, optional): The joke category ('family' or 'tech').
                                 If None, randomly selects a category.
    
    Returns:
        str: A randomly generated joke.
    
    Raises:
        ValueError: If an invalid category is provided.
    
    Example:
        >>> joke = get_random_joke()  # Random category
        >>> print(joke)
        
        >>> joke = get_random_joke('tech')  # Tech jokes only
        >>> print(joke)
        
        >>> joke = get_random_joke('family')  # Family jokes only
        >>> print(joke)
    """
    if category is None:
        category = random.choice(CATEGORIES)
    
    category = category.lower()
    
    if category == 'family':
        return get_family_joke()
    elif category == 'tech':
        return get_tech_joke()
    else:
        raise ValueError(
            f"Invalid category '{category}'. "
            f"Choose from: {', '.join(CATEGORIES)}"
        )
