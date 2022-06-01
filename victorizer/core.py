import importlib.resources
import random
import webbrowser

WISDOMS_FILENAME = "wisdoms.txt"
PAPER_LINKS_FILENAME = "paper_links.txt"
SONGS_FILENAME = "songs.txt"
SHORTCUT_FILENAME = "shortcuts.txt"
RESOURCES_PACKAGE_NAME = "victorizer.resources"


def select_random_line(input_filename: str) -> str:
    lines = importlib.resources.read_text(
        RESOURCES_PACKAGE_NAME, input_filename
    ).splitlines()
    if not lines:
        raise ValueError(f"Input file {input_filename} is empty.")
    return random.choice(lines)


def open_url(random_string: str) -> str:
    lst = random_string.split('|')
    print(lst[0])
    webbrowser.open(lst[1])


def get_wisdom() -> str:
    return select_random_line(WISDOMS_FILENAME)


def open_paper_link() -> str:
    open_url(
        random_string=select_random_line(PAPER_LINKS_FILENAME)
    )


def play_song() -> str:
    open_url(
        select_random_line(SONGS_FILENAME)
    )


def get_shortcut() -> str:
    return select_random_line(SHORTCUT_FILENAME)
