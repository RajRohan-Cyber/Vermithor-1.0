from datetime import datetime


def get_current_time():

    current_time = datetime.now()

    return current_time.strftime(
        "%I:%M %p"
    )


def get_current_date():

    current_date = datetime.now()

    return current_date.strftime(
        "%d %B %Y"
    )