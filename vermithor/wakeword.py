WAKE_WORDS = [
    "hey vermithor",
    "hello vermithor",
    "vermithor",
]


def is_wake_word(text):

    text = text.lower().strip()

    for wake_word in WAKE_WORDS:

        if wake_word in text:

            return True

    return False