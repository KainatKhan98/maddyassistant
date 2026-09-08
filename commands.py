# ==========================================
# MADDY V3 - COMMAND HANDLER
# ==========================================

from intents import detect_intent
from actions import *
from app_manager import open_app, close_app
from voice import speak
from system_control import (
    increase_volume,
    decrease_volume,
    mute_volume,
    minimize_window,
    maximize_window,
    lock_computer,
    restart_computer,
    shutdown_computer,
    cancel_shutdown,
    take_screenshot
)

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

        open_app(target)

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

    elif intent == "MINIMIZE" :
        minimize_window()

    elif intent == "MAXIMIZE":
        maximize_window()

    # ==========================================
    # CHROME
    # ==========================================

    elif intent == "CLOSE_APP":

        close_app(target)

    # ==========================================
    # SYSTEM
    # ==========================================

   # ==========================================
# SYSTEM CONTROL
# ==========================================

    elif intent == "VOLUME_UP":

     increase_volume()


    elif intent == "VOLUME_DOWN":

        decrease_volume()


    elif intent == "MUTE":

        mute_volume()


    elif intent == "MINIMIZE":

        minimize_window()


    elif intent == "MAXIMIZE":

        maximize_window()


    elif intent == "SCREENSHOT":

        take_screenshot()


    elif intent == "LOCK":

        lock_computer()


    elif intent == "RESTART":

         restart_computer()


    elif intent == "SHUTDOWN":

     shutdown_computer()


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