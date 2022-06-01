import importlib.resources
import random
import webbrowser

WISDOMS_FILENAME = "wisdoms.txt"
PAPER_LINKS_FILENAME = "paper_links.txt"
SONGS_FILENAME = "songs.txt"
SHORTCUT_FILENAME = "shortcuts.txt"
COFFEE_FILENAME = "coffee.txt"
RESOURCES_PACKAGE_NAME = "victorizer.resources"
DESCRIPTION_URL_SEPARATOR = "|"


def select_random_line(input_filename: str) -> str:
    lines = importlib.resources.read_text(
        RESOURCES_PACKAGE_NAME, input_filename
    ).splitlines()
    if not lines:
        raise ValueError(f"Input file {input_filename} is empty.")
    return random.choice(lines)


def open_url(input_string: str) -> str:
    description, url = input_string.split(DESCRIPTION_URL_SEPARATOR)
    print(description)
    webbrowser.open(url)
    return description


def get_wisdom() -> str:
    return select_random_line(WISDOMS_FILENAME)


def get_song() -> str:
    return select_random_line(SONGS_FILENAME)


def get_paper_link() -> str:
    return select_random_line(PAPER_LINKS_FILENAME)


def get_shortcut() -> str:
    return select_random_line(SHORTCUT_FILENAME)


def get_coffee() -> str:
    return select_random_line(COFFEE_FILENAME)

  
def open_paper_link() -> str:
    return open_url(select_random_line(PAPER_LINKS_FILENAME))


def play_song() -> str:
    return open_url(select_random_line(SONGS_FILENAME))
