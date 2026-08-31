import webbrowser
import subprocess
from datetime import datetime

from vermithor.system import open_calculator, open_notepad


def process_command(command):

    command = command.lower().strip()

    # -----------------------------
    # GREETINGS
    # -----------------------------

    if command in [
        "hello",
        "hi",
        "hey"
    ]:

        return "Hello! How can I help you?"


    # -----------------------------
    # TIME
    # -----------------------------

    if "time" in command:

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        return (
            f"The current time is "
            f"{current_time}."
        )


    # -----------------------------
    # DATE
    # -----------------------------

    if "date" in command:

        current_date = datetime.now().strftime(
            "%d %B %Y"
        )

        return (
            f"Today is "
            f"{current_date}."
        )


    # -----------------------------
    # OPEN CALCULATOR
    # -----------------------------

    if (
        "open calculator" in command
        or
        "open calc" in command
        or
        command == "calculator"
    ):

        open_calculator()

        return "Opening calculator."


    # -----------------------------
    # OPEN NOTEPAD
    # -----------------------------

    if (
        "open notepad" in command
        or
        command == "notepad"
    ):

        open_notepad()

        return "Opening Notepad."

        
    # -----------------------------
    # OPEN YOUTUBE
    # -----------------------------

    if "open youtube" in command:

        webbrowser.open(
            "https://www.youtube.com"
        )

        return "Opening YouTube."


    # -----------------------------
    # OPEN INSTAGRAM
    # -----------------------------

    if "open instagram" in command:

        webbrowser.open(
            "https://www.instagram.com"
        )

        return "Opening Instagram."


    # -----------------------------
    # OPEN GOOGLE
    # -----------------------------

    if "open google" in command:

        webbrowser.open(
            "https://www.google.com"
        )

        return "Opening Google."


    # -----------------------------
    # OPEN GITHUB
    # -----------------------------

    if "open github" in command:

        webbrowser.open(
            "https://github.com"
        )

        return "Opening GitHub."


    # -----------------------------
    # SEARCH THE WEB
    # -----------------------------

    if command.startswith(
        "search for "
    ):

        search_query = command.replace(
            "search for ",
            "",
            1
        )

        if search_query:

            url = (
                "https://www.google.com/search?q="
                + search_query.replace(
                    " ",
                    "+"
                )
            )

            webbrowser.open(
                url
            )

            return (
                f"Searching for "
                f"{search_query}."
            )


    # -----------------------------
    # UNKNOWN COMMAND
    # -----------------------------

    return (
        "I heard you, but I don't "
        "know how to do that yet."
    )