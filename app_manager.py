# ==========================================
# MADDY V3.6.2 - DYNAMIC APP DISCOVERY
# ==========================================

import os
import subprocess
import psutil

from difflib import get_close_matches

from voice import speak


# ==========================================
# KNOWN APPLICATIONS
# ==========================================

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


# ==========================================
# DYNAMIC APP DISCOVERY
# ==========================================

def discover_apps():

    discovered_apps = {}

    start_menu_paths = [

        os.path.expandvars(
            r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
        ),

        os.path.expandvars(
            r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs"
        )
    ]

    for start_menu in start_menu_paths:

        if not os.path.exists(start_menu):
            continue

        for root, dirs, files in os.walk(start_menu):

            for file in files:

                if not file.lower().endswith(".lnk"):
                    continue

                app_name = os.path.splitext(file)[0].strip()

                if not app_name:
                    continue

                key = app_name.lower()

                if key not in discovered_apps:

                    shortcut_path = os.path.join(
                        root,
                        file
                    )

                    discovered_apps[key] = shortcut_path

    return discovered_apps


# ==========================================
# FIND APPLICATION
# ==========================================

def find_app(app_name):

    app_name = app_name.lower().strip()

    # --------------------------------------
    # 1. Known applications
    # --------------------------------------

    if app_name in APPS:
        return APPS[app_name]

    # --------------------------------------
    # 2. Discover Windows applications
    # --------------------------------------

    discovered_apps = discover_apps()

    # --------------------------------------
    # 3. Exact match
    # --------------------------------------

    if app_name in discovered_apps:

        return discovered_apps[app_name]

    # --------------------------------------
    # 4. Partial match
    # --------------------------------------

    for name, path in discovered_apps.items():

        if app_name in name or name in app_name:

            return path

    # --------------------------------------
    # 5. Fuzzy / typo matching
    # --------------------------------------

    matches = get_close_matches(
        app_name,
        discovered_apps.keys(),
        n=1,
        cutoff=0.65
    )

    if matches:

        matched_name = matches[0]

        print(
            f"Fuzzy match: '{app_name}' -> '{matched_name}'"
        )

        return discovered_apps[matched_name]

    return None


# ==========================================
# OPEN APPLICATION
# ==========================================

def open_app(app_name):

    app_path = find_app(app_name)

    if not app_path:

        speak(
            f"I couldn't find {app_name} on your computer."
        )

        print(
            f"App not found: {app_name}"
        )

        return False

    try:

        # ----------------------------------
        # Open Windows shortcut
        # ----------------------------------

        if app_path.lower().endswith(".lnk"):

            os.startfile(app_path)

        else:

            subprocess.Popen(
                app_path,
                shell=False
            )

        speak(
            f"Opening {app_name}."
        )

        print(
            f"Opened: {app_name}"
        )

        return True

    except Exception as e:

        print(
            f"Error opening {app_name}: {e}"
        )

        speak(
            f"I couldn't open {app_name}."
        )

        return False


# ==========================================
# CHECK IF APP IS RUNNING
# ==========================================

def is_app_running(app_name):

    app_name = app_name.lower().strip()

    # --------------------------------------
    # Known application
    # --------------------------------------

    if app_name in APPS:

        process_name = APPS[app_name]["process"]

        for process in psutil.process_iter(["name"]):

            try:

                current_name = process.info["name"]

                if current_name:

                    if current_name.lower() == process_name.lower():

                        return True

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied
            ):

                continue

        return False

    # --------------------------------------
    # Dynamic application
    # --------------------------------------

    discovered_apps = discover_apps()

    matching_name = None

    # Exact match
    if app_name in discovered_apps:

        matching_name = app_name

    # Partial match
    else:

        for name in discovered_apps:

            if app_name in name or name in app_name:

                matching_name = name
                break

    # Fuzzy match
    if not matching_name:

        matches = get_close_matches(
            app_name,
            discovered_apps.keys(),
            n=1,
            cutoff=0.65
        )

        if matches:

            matching_name = matches[0]

    if not matching_name:
        return False

    # --------------------------------------
    # Search running processes
    # --------------------------------------

    for process in psutil.process_iter(["name"]):

        try:

            process_name = process.info["name"]

            if not process_name:
                continue

            process_base = os.path.splitext(
                process_name
            )[0].lower()

            # Normalize names
            normalized_app = (
                matching_name
                .replace(" ", "")
                .replace("-", "")
                .replace("_", "")
                .lower()
            )

            normalized_process = (
                process_base
                .replace(" ", "")
                .replace("-", "")
                .replace("_", "")
                .lower()
            )

            if (
                normalized_app in normalized_process
                or normalized_process in normalized_app
            ):

                return True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):

            continue

    return False


# ==========================================
# CLOSE APPLICATION
# ==========================================

def close_app(app_name):

    app_name = app_name.lower().strip()

    # ======================================
    # KNOWN APPLICATION
    # ======================================

    if app_name in APPS:

        process_name = APPS[app_name]["process"]

        found = False

        for process in psutil.process_iter(["name"]):

            try:

                current_name = process.info["name"]

                if not current_name:
                    continue

                if current_name.lower() == process_name.lower():

                    process.terminate()

                    found = True

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied
            ):

                continue

        if found:

            speak(
                f"Closing {app_name}."
            )

            print(
                f"Closed: {app_name}"
            )

            return True

    # ======================================
    # DYNAMIC APPLICATION
    # ======================================

    discovered_apps = discover_apps()

    matching_name = None

    # --------------------------------------
    # Exact match
    # --------------------------------------

    if app_name in discovered_apps:

        matching_name = app_name

    # --------------------------------------
    # Partial match
    # --------------------------------------

    if not matching_name:

        for name in discovered_apps:

            if app_name in name or name in app_name:

                matching_name = name
                break

    # --------------------------------------
    # Fuzzy match
    # --------------------------------------

    if not matching_name:

        matches = get_close_matches(
            app_name,
            discovered_apps.keys(),
            n=1,
            cutoff=0.65
        )

        if matches:

            matching_name = matches[0]

            print(
                f"Fuzzy match: '{app_name}' -> '{matching_name}'"
            )

    if not matching_name:

        speak(
            f"I couldn't find {app_name}."
        )

        print(
            f"Dynamic app not found: {app_name}"
        )

        return False

    # ======================================
    # SEARCH RUNNING PROCESSES
    # ======================================

    normalized_app = (
        matching_name
        .replace(" ", "")
        .replace("-", "")
        .replace("_", "")
        .lower()
    )

    found_process = False

    for process in psutil.process_iter(
        ["pid", "name"]
    ):

        try:

            process_name = process.info["name"]

            if not process_name:
                continue

            process_base = os.path.splitext(
                process_name
            )[0].lower()

            normalized_process = (
                process_base
                .replace(" ", "")
                .replace("-", "")
                .replace("_", "")
                .lower()
            )

            # ----------------------------------
            # Match application to process
            # ----------------------------------

            if (
                normalized_app in normalized_process
                or normalized_process in normalized_app
            ):

                print(
                    f"Process match: "
                    f"{matching_name} -> "
                    f"{process_name}"
                )

                process.terminate()

                found_process = True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):

            continue

    # ======================================
    # SUCCESS
    # ======================================

    if found_process:

        speak(
            f"Closing {matching_name}."
        )

        print(
            f"Closed: {matching_name}"
        )

        return True

    # ======================================
    # FAILED
    # ======================================

    speak(
        f"I couldn't close {app_name}."
    )

    print(
        f"Could not close: {app_name}"
    )

    return False