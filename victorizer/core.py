import importlib.resources
import random
import webbrowser

WISDOMS_FILENAME = "wisdoms.txt"
PAPER_LINKS_FILENAME = "paper_links.txt"
SONGS_FILENAME = "songs.txt"
SHORTCUT_FILENAME = "shortcuts.txt"
RESOURCES_PACKAGE_NAME = "victorizer.resources"
DESCRIPTION_URL_SEPARATOR = "|"


def select_random_line(input_filename: str) -> str:
    lines = importlib.resources.read_text(
        RESOURCES_PACKAGE_NAME, input_filename
    ).splitlines()
    if not lines:
        raise ValueError(f"Input file {input_filename} is empty.")
    return random.choice(lines)


def open_url(input_string: str) -> None:
    description, url = input_string.split(DESCRIPTION_URL_SEPARATOR)
    print(description)
    webbrowser.open(url)


def get_wisdom() -> str:
    return select_random_line(WISDOMS_FILENAME)


def get_shortcut() -> str:
    return select_random_line(SHORTCUT_FILENAME)


def open_paper_link() -> None:
    open_url(select_random_line(PAPER_LINKS_FILENAME))


def play_song() -> None:
    open_url(select_random_line(SONGS_FILENAME))
