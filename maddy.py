import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import scipy.io.wavfile as wav
import webbrowser
import subprocess
import datetime
import os
import tempfile


# ==========================================
# MADDY CONFIGURATION
# ==========================================

SAMPLE_RATE = 16000
RECORD_SECONDS = 5

recognizer = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


# ==========================================
# MADDY SPEAK
# ==========================================

def speak(text):

    print(f"Maddy: {text}")

    engine.say(text)
    engine.runAndWait()


# ==========================================
# RECORD VOICE
# ==========================================

def record_audio():

    print("\n🎤 Listening...")

    try:

        audio = sd.rec(
            int(RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        return audio

    except Exception as e:

        print("Microphone error:", e)

        return None


# ==========================================
# CONVERT VOICE TO TEXT
# ==========================================

def listen():

    audio_data = record_audio()

    if audio_data is None:
        return ""

    try:

        # Create temporary WAV file
        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_file:

            temp_filename = temp_file.name

        wav.write(
            temp_filename,
            SAMPLE_RATE,
            audio_data
        )

        # Read audio using SpeechRecognition
        with sr.AudioFile(temp_filename) as source:

            audio = recognizer.record(source)

        print("🔎 Recognizing...")

        command = recognizer.recognize_google(audio)

        print(f"You: {command}")

        # Delete temporary file
        os.remove(temp_filename)

        return command.lower()

    except sr.UnknownValueError:

        print("Maddy: I couldn't understand that.")

        return ""

    except sr.RequestError:

        speak(
            "Sorry, I cannot connect to the speech recognition service."
        )

        return ""

    except Exception as e:

        print("Error:", e)

        return ""


# ==========================================
# OPEN CHROME
# ==========================================

def open_chrome():

    chrome_paths = [

        r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",

        os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
        )
    ]

    for path in chrome_paths:

        if os.path.exists(path):

            speak("Opening Chrome.")

            subprocess.Popen(path)

            return

    speak("I couldn't find Chrome on your computer.")


# ==========================================
# OPEN VS CODE
# ==========================================

def open_vscode():

    speak("Opening Visual Studio Code.")

    try:

        subprocess.Popen(
            "code",
            shell=True
        )

    except Exception:

        speak("I couldn't open Visual Studio Code.")


# ==========================================
# OPEN WEBSITES
# ==========================================

def open_youtube():

    speak("Opening YouTube.")

    webbrowser.open(
        "https://www.youtube.com"
    )


def open_google():

    speak("Opening Google.")

    webbrowser.open(
        "https://www.google.com"
    )


# ==========================================
# TIME
# ==========================================

def tell_time():

    current_time = datetime.datetime.now().strftime(
        "%I:%M %p"
    )

    speak(
        f"The time is {current_time}."
    )


# ==========================================
# DATE
# ==========================================

def tell_date():

    current_date = datetime.datetime.now().strftime(
        "%B %d, %Y"
    )

    speak(
        f"Today's date is {current_date}."
    )


# ==========================================
# PROCESS COMMAND
# ==========================================

def process_command(command):

    # Remove wake word
    command = command.replace(
        "hey maddy",
        ""
    )

    command = command.replace(
        "maddy",
        ""
    )

    command = command.strip()

    print(f"Command: {command}")

    # --------------------------------------
    # CHROME
    # --------------------------------------

    if "open chrome" in command:

        open_chrome()

    # --------------------------------------
    # YOUTUBE
    # --------------------------------------

    elif "open youtube" in command:

        open_youtube()

    # --------------------------------------
    # GOOGLE
    # --------------------------------------

    elif "open google" in command:

        open_google()

    # --------------------------------------
    # VS CODE
    # --------------------------------------

    elif (
        "open vs code" in command
        or
        "open visual studio code" in command
    ):

        open_vscode()

    # --------------------------------------
    # TIME
    # --------------------------------------

    elif (
        "what time" in command
        or
        "current time" in command
    ):

        tell_time()

    # --------------------------------------
    # DATE
    # --------------------------------------

    elif (
        "today's date" in command
        or
        "what is the date" in command
        or
        "what's the date" in command
    ):

        tell_date()

    # --------------------------------------
    # EXIT
    # --------------------------------------

    elif (
        "exit" in command
        or
        "quit" in command
        or
        "stop" in command
        or
        "goodbye" in command
    ):

        speak("Goodbye!")

        return False

    # --------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------

    else:

        speak(
            "I don't know that command yet."
        )

    return True


# ==========================================
# MAIN MADDY LOOP
# ==========================================

def main():

    print("=" * 45)
    print("        MADDY V1")
    print("     Voice Assistant")
    print("=" * 45)

    speak(
        "Hello. Maddy is ready."
    )

    while True:

        command = listen()

        if not command:
            continue

        # Only respond when Maddy is mentioned
        if "maddy" in command:

            should_continue = process_command(
                command
            )

            if not should_continue:

                break

        else:

            print(
                "Maddy was not called."
            )


# ==========================================
# START MADDY
# ==========================================

if __name__ == "__main__":

    main()