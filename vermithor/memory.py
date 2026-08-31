import json
from pathlib import Path


MEMORY_FILE = Path("data/memory.json")


def create_memory_file():

    MEMORY_FILE.parent.mkdir(
        exist_ok=True
    )

    if not MEMORY_FILE.exists():

        memory = {
            "name": "",
            "preferences": {},
            "notes": [],
            "history": []
        }

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                memory,
                file,
                indent=4
            )


def load_memory():

    create_memory_file()

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )


def save_memory(memory):

    create_memory_file()

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )