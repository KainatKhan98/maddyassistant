# ==========================================
# MADDY V3 - COMMAND HANDLER
# ==========================================

from intents import detect_intent
from actions import *
from voice import speak


def process_command(command):

    result = detect_intent(command)

    intent = result["intent"]
    target = result["target"]
    query = result["query"]

    print(f"Intent: {intent}")
    print(f"Target: {target}")
    print(f"Query: {query}")

    # ==========================================
    # OPEN APPLICATION
    # ==========================================

    if intent == "OPEN_APP":

        if target == "chrome":
            open_chrome()

        elif target == "vscode":
            open_vscode()

        elif target == "notepad":
            open_notepad()

        elif target == "calculator":
            open_calculator()

    # ==========================================
    # WEBSITE
    # ==========================================

    elif intent == "OPEN_WEBSITE":

        if target == "youtube":
            open_youtube()

        elif target == "google":
            open_google()

    # ==========================================
    # GOOGLE SEARCH
    # ==========================================

    elif intent == "GOOGLE_SEARCH":

        google_search(query)

    # ==========================================
    # YOUTUBE SEARCH
    # ==========================================

    elif intent == "YOUTUBE_SEARCH":

        youtube_search(query)

    # ==========================================
    # FOLDERS
    # ==========================================

    elif intent == "OPEN_FOLDER":

        if target == "downloads":
            open_downloads()

        elif target == "documents":
            open_documents()

        elif target == "desktop":
            open_desktop()

    # ==========================================
    # TIME
    # ==========================================

    elif intent == "TIME":
        tell_time()

    # ==========================================
    # DATE
    # ==========================================

    elif intent == "DATE":
        tell_date()

    # ==========================================
    # SCREENSHOT
    # ==========================================

    elif intent == "SCREENSHOT":
        take_screenshot()

    # ==========================================
    # VOLUME
    # ==========================================

    elif intent == "VOLUME_UP":
        increase_volume()

    elif intent == "VOLUME_DOWN":
        decrease_volume()

    elif intent == "MUTE":
        mute_volume()

    # ==========================================
    # WINDOW
    # ==========================================

    elif intent == "MINIMIZE":
        minimize_window()

    elif intent == "MAXIMIZE":
        maximize_window()

    # ==========================================
    # CHROME
    # ==========================================

    elif intent == "CLOSE_CHROME":
        close_chrome()

    # ==========================================
    # SYSTEM
    # ==========================================

    elif intent == "LOCK":
        lock_computer()

    elif intent == "RESTART":

        speak(
            "Restarting your computer in ten seconds."
        )

        restart_computer()

    elif intent == "CANCEL_SHUTDOWN":
        cancel_shutdown()

    # ==========================================
    # TYPE
    # ==========================================

    elif intent == "TYPE":

        if query:
            type_text(query)

    # ==========================================
    # EXIT
    # ==========================================

    elif intent == "EXIT":

        speak("Goodbye.")
        return False

    # ==========================================
    # UNKNOWN
    # ==========================================

    else:

        speak(
            "I'm not sure what you want me to do."
        )

        print(
            f"Unknown command: {query}"
        )

    return True