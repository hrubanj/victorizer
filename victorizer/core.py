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


def extract_url(random_string: str, split_string: str) -> str:
    lst = random_string.split(split_string)
    url = lst[1]
    name = lst[0]
    return name, url


def get_wisdom() -> str:
    return select_random_line(WISDOMS_FILENAME)


def get_paper_link() -> str:
    paper_name, paper_url = extract_url(
        random_string=select_random_line(PAPER_LINKS_FILENAME),
        split_string=' - '
    )
    print(paper_name)
    webbrowser.open(paper_url)


def get_song() -> str:
    song_name, song_url = extract_url(select_random_line(SONGS_FILENAME), split_string=', ')
    print(song_name)
    webbrowser.open(song_url)


def get_shortcut() -> str:
    return select_random_line(SHORTCUT_FILENAME)
