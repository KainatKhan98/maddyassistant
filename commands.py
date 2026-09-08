# ==========================================
# MADDY V2 - COMMAND PROCESSOR
# ==========================================

from actions import *
from voice import speak


def clean_command(command):
    command = command.lower().strip()

    # Remove wake words
    command = command.replace("hey maddy", "")
    command = command.replace("hello maddy", "")
    command = command.replace("maddy", "")

    # Remove filler words
    filler_words = [
        "hello",
        "hi",
        "hey",
        "please",
        "can you",
        "could you",
        "would you",
        "will you",
        "for me"
    ]

    for word in filler_words:
        command = command.replace(word, "")

    # Remove extra spaces
    command = " ".join(command.split())

    return command


def process_command(command):

    # CLEAN THE COMMAND FIRST
    command = clean_command(command)

    print(f"Command: {command}")

    # ==========================================
    # OPEN APPLICATIONS
    # ==========================================

    if "open chrome" in command or "launch chrome" in command:
        open_chrome()

    elif (
        "open vscode" in command
        or "open visual studio code" in command
        or "launch vscode" in command
    ):
        open_vscode()

    elif "open notepad" in command or "launch notepad" in command:
        open_notepad()

    elif "open calculator" in command or "launch calculator" in command:
        open_calculator()

    # ==========================================
    # WEBSITES
    # ==========================================

    elif "open google" in command:
        open_google()

    elif "open youtube" in command:
        open_youtube()

    # ==========================================
    # SEARCH
    # ==========================================

    elif command.startswith("search google for"):
        query = command.replace(
            "search google for", "", 1
        ).strip()

        if query:
            google_search(query)
        else:
            speak("What should I search for?")

    elif command.startswith("search youtube for"):
        query = command.replace(
            "search youtube for", "", 1
        ).strip()

        if query:
            youtube_search(query)
        else:
            speak("What should I search for?")

    # ==========================================
    # FOLDERS
    # ==========================================

    elif "open downloads" in command:
        open_downloads()

    elif "open documents" in command:
        open_documents()

    elif "open desktop" in command:
        open_desktop()

    # ==========================================
    # TIME / DATE
    # ==========================================

    elif (
        "what time is it" in command
        or command == "time"
        or "tell me the time" in command
    ):
        tell_time()

    elif (
        "what is the date" in command
        or "what's the date" in command
        or "today's date" in command
        or "tell me the date" in command
    ):
        tell_date()

    # ==========================================
    # SCREENSHOT
    # ==========================================

    elif "take a screenshot" in command:
        take_screenshot()

    elif command == "screenshot":
        take_screenshot()

    # ==========================================
    # TYPING
    # ==========================================

    elif command.startswith("type "):

        text = command.replace(
            "type ", "", 1
        ).strip()

        if text:
            type_text(text)

    # ==========================================
    # VOLUME
    # ==========================================

    elif (
        "increase volume" in command
        or "volume up" in command
        or "turn up volume" in command
    ):
        increase_volume()

    elif (
        "decrease volume" in command
        or "volume down" in command
        or "turn down volume" in command
    ):
        decrease_volume()

    elif "mute" in command:
        mute_volume()

    # ==========================================
    # WINDOW CONTROL
    # ==========================================

    elif "minimize" in command:
        minimize_window()

    elif "maximize" in command:
        maximize_window()

    # ==========================================
    # CHROME
    # ==========================================

    elif "close chrome" in command:
        close_chrome()

    # ==========================================
    # COMPUTER CONTROL
    # ==========================================

    elif (
        "lock computer" in command
        or "lock my computer" in command
    ):
        lock_computer()

    elif (
        "restart computer" in command
        or "restart my computer" in command
    ):
        restart_computer()

    elif "cancel shutdown" in command:
        cancel_shutdown()

    # ==========================================
    # EXIT
    # ==========================================

    elif command in [
        "exit",
        "quit",
        "stop",
        "goodbye",
        "shutdown maddy"
    ]:
        speak("Goodbye.")
        return False

    # ==========================================
    # UNKNOWN COMMAND
    # ==========================================

    else:
        speak("I don't know that command yet.")
        print(f"Unknown command: {command}")

    return True