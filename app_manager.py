# ==========================================
# MADDY V3 - APP MANAGER
# ==========================================

import subprocess
import os
import psutil
from voice import speak


# ------------------------------------------
# APPLICATION CONFIGURATION
# ------------------------------------------

APPS = {

    "chrome": {
        "process": "chrome.exe",
        "paths": [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
    },

    "vscode": {
        "process": "Code.exe",
        "paths": [
            r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        ]
    },

    "notepad": {
        "process": "notepad.exe",
        "paths": [
            r"C:\Windows\System32\notepad.exe"
        ]
    },

    "calculator": {
        "process": "CalculatorApp.exe",
        "paths": [
            r"C:\Windows\System32\calc.exe"
        ]
    }
}


# ------------------------------------------
# FIND APPLICATION
# ------------------------------------------

def find_app(app_name):

    app_name = app_name.lower().strip()

    if app_name not in APPS:
        return None

    for path in APPS[app_name]["paths"]:

        path = os.path.expandvars(path)

        if os.path.exists(path):
            return path

    return None


# ------------------------------------------
# OPEN APPLICATION
# ------------------------------------------

def open_app(app_name):

    app_name = app_name.lower().strip()

    app = APPS.get(app_name)

    if not app:
        speak(f"I don't know how to open {app_name}.")
        return False

    path = find_app(app_name)

    if path:

        try:

            subprocess.Popen(path)

            speak(f"Opening {app_name}.")

            print(f"Opened: {app_name}")

            return True

        except Exception as e:

            print(f"Error opening {app_name}: {e}")

            speak(
                f"I couldn't open {app_name}."
            )

            return False

    # --------------------------------------
    # FALLBACK
    # --------------------------------------

    try:

        subprocess.Popen(app_name)

        speak(f"Opening {app_name}.")

        return True

    except Exception:

        speak(
            f"I couldn't find {app_name} on your computer."
        )

        print(
            f"Application not found: {app_name}"
        )

        return False


# ------------------------------------------
# CHECK IF APPLICATION IS RUNNING
# ------------------------------------------

def is_app_running(app_name):

    app_name = app_name.lower().strip()

    app = APPS.get(app_name)

    if not app:
        return False

    process_name = app["process"]

    for process in psutil.process_iter(
        ["name"]
    ):

        try:

            if process.info["name"]:

                if process.info["name"].lower() == process_name.lower():

                    return True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):

            continue

    return False


# ------------------------------------------
# CLOSE APPLICATION
# ------------------------------------------

def close_app(app_name):

    app_name = app_name.lower().strip()

    app = APPS.get(app_name)

    if not app:

        speak(
            f"I don't know how to close {app_name}."
        )

        return False

    process_name = app["process"]

    closed = False

    for process in psutil.process_iter(
        ["name"]
    ):

        try:

            if process.info["name"]:

                if process.info["name"].lower() == process_name.lower():

                    process.terminate()

                    closed = True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):

            continue

    if closed:

        speak(f"Closing {app_name}.")

        print(f"Closed: {app_name}")

        return True

    else:

        speak(
            f"{app_name} is not currently running."
        )

        return False