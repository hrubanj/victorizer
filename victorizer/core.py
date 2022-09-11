"""
core.py
The main module of the library that includes all its
core functionality.
"""


import importlib.resources
import random
import webbrowser

WISDOMS_FILENAME = "wisdoms.txt"
PAPER_LINKS_FILENAME = "paper_links.txt"
SONGS_FILENAME = "songs.txt"
SHORTCUT_FILENAME = "shortcuts.txt"
COFFEE_FILENAME = "coffee.txt"
FOOD_FILENAME = "food.txt"
RESOURCES_PACKAGE_NAME = "victorizer.resources"
DESCRIPTION_URL_SEPARATOR = "|"


def select_random_line(input_filename: str) -> str:
    """
    Select random line from a supplied file.

    Args:
         input_filename: name of the file from which the line is selected
    """
    lines = importlib.resources.read_text(
        RESOURCES_PACKAGE_NAME, input_filename
    ).splitlines()
    if not lines:
        raise ValueError(f"Input file {input_filename} is empty.")
    return random.choice(lines)


def open_url(input_string: str) -> str:
    """
    Open url supplied as a part of pipe-separated string in
    the default browser.

    Args:
         input_string: pipe-separated string with (description | URL)
    """
    description, url = input_string.split(DESCRIPTION_URL_SEPARATOR)
    print(description)
    webbrowser.open(url)
    return description


def get_wisdom() -> str:
    """
    Return randomly selected wisdom from a collected selection.
    """
    return select_random_line(WISDOMS_FILENAME)


def get_song() -> str:
    """
    Return randomly selected song from a collected selection.
    """
    return select_random_line(SONGS_FILENAME)


def get_paper_link() -> str:
    """
    Return randomly selected paper link from a collected selection.
    """
    return select_random_line(PAPER_LINKS_FILENAME)


def get_shortcut() -> str:
    """
    Return randomly selected shortcut from a collected selection.
    """
    return select_random_line(SHORTCUT_FILENAME)


def get_coffee() -> str:
    """
    Return randomly selected coffee shop a collected selection.
    """
    return select_random_line(COFFEE_FILENAME)


def open_paper_link() -> str:
    """
    Open randomly selected paper link from a collected selection in
    the default browser.
    """
    return open_url(select_random_line(PAPER_LINKS_FILENAME))


def play_song() -> str:
    """
    Play randomly selected song from a collected selection in
    the default browser on YouTube.
    """
    return open_url(select_random_line(SONGS_FILENAME))


def find_coffee() -> str:
    """
    Open browser with Google Maps pointing to a location of
    randomly selected coffee shop from a selection of coffee
    shops.
    """
    return open_url(select_random_line(COFFEE_FILENAME))


def get_food() -> str:
    """
    Return randomly selected restaurant shop a collected selection.
    """
    return select_random_line(FOOD_FILENAME)


def find_food() -> str:
    """
    Open browser with Google Maps pointing to a location of
    randomly selected restaurant from a selection of coffee
    shops.
    """
    return open_url(select_random_line(FOOD_FILENAME))
