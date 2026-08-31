import speech_recognition as sr


MICROPHONE_INDEX = 1


recognizer = sr.Recognizer()

recognizer.dynamic_energy_threshold = True

recognizer.pause_threshold = 1.0

recognizer.phrase_threshold = 0.3

recognizer.non_speaking_duration = 0.5


def listen():

    try:

        microphone = sr.Microphone(
            device_index=MICROPHONE_INDEX
        )

        with microphone as source:

            print(
                "Speak now..."
            )

            audio = recognizer.listen(
                source,
                timeout=None,
                phrase_time_limit=10
            )

        try:

            text = recognizer.recognize_google(
                audio,
                language="en-US"
            )

            return text.lower().strip()

        except sr.UnknownValueError:

            print(
                "I didn't understand that."
            )

            return ""

        except sr.RequestError as error:

            print(
                "Speech recognition error:",
                error
            )

            return ""

    except Exception as error:

        print(
            "Microphone error:",
            error
        )

        return ""