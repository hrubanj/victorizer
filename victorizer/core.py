import importlib.resources
import random


WISDOMS_FILENAME = "wisdoms.txt"
PAPER_LINKS_FILENAME = "paper_links.txt"
RESOURCES_PACKAGE_NAME = "victorizer.resources"


def select_random_line(input_filename: str) -> str:
    lines = importlib.resources.read_text(
        RESOURCES_PACKAGE_NAME, input_filename
    ).splitlines()
    if not lines:
        raise ValueError(f"Input file {input_filename} is empty.")
    return random.choice(lines)


def get_wisdom() -> str:
    return select_random_line(WISDOMS_FILENAME)


def get_paper_link() -> str:
    return select_random_line(PAPER_LINKS_FILENAME)
