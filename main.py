from vermithor.listener import listen
from vermithor.voice import speak
from vermithor.wakeword import is_wake_word
from vermithor.memory import load_memory
from vermithor.commands import process_command


def remove_wake_word(text):

    wake_words = [
        "hey vermithor",
        "hello vermithor",
        "vermithor"
    ]

    text = text.lower().strip()

    for wake_word in wake_words:

        if wake_word in text:

            text = text.replace(
                wake_word,
                "",
                1
            )

            return text.strip()

    return text


def main():

    memory = load_memory()

    speak(
        "Vermithor is online."
    )

    while True:

        print()
        print("Listening...")

        text = listen()

        if not text:

            continue

        print(
            "You said:",
            text
        )


        # -----------------------------
        # WAKE WORD
        # -----------------------------

        if is_wake_word(text):

            command = remove_wake_word(
                text
            )


            # -------------------------
            # WAKE WORD ONLY
            # -------------------------

            if not command:

                speak(
                    "Hello! I'm here. "
                    "How can I help you?"
                )

                continue


            # -------------------------
            # WAKE WORD + COMMAND
            # -------------------------

            response = process_command(
                command
            )

            if response:

                speak(
                    response
                )

            continue


        # -----------------------------
        # NORMAL COMMAND
        # -----------------------------

        response = process_command(
            text
        )

        if response:

            speak(
                response
            )


if __name__ == "__main__":

    main()