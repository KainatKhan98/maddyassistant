# ==========================================
# MADDY V3 - INTENT ENGINE
# ==========================================

import re


def normalize_text(text):
    """Clean and normalize spoken text."""

    text = text.lower().strip()

    wake_words = [
        "hey maddy",
        "hello maddy",
        "hi maddy",
        "maddy"
    ]

    for word in wake_words:
        text = text.replace(word, "")

    filler_words = [
        "please",
        "can you",
        "could you",
        "would you",
        "will you",
        "for me",
        "i want you to",
        "i need you to"
    ]

    for word in filler_words:
        text = text.replace(word, "")

    text = " ".join(text.split())

    return text


def detect_intent(command):

    command = normalize_text(command)

# ==========================================
# CONVERSATION COMMANDS
# ==========================================

    if any(
    phrase in command
    for phrase in [
        "hello",
        "hi",
        "hey"
        ]
    ):

        return {
        "intent": "GREETING",
        "target": None,
        "query": None
     }


    if any(
        phrase in command
        for phrase in [
        "how are you",
        "how are you doing"
        ]
    ):

        return {
        "intent": "HOW_ARE_YOU",
        "target": None,
        "query": None
        }


    if any(
        phrase in command
    for phrase in [
        "thank you",
        "thanks",
        "thank maddy"
        ]
    ):

        return {
        "intent": "THANKS",
        "target": None,
        "query": None
        }


    if any(
        phrase in command
    for phrase in [
        "what can you do",
        "what can you do for me",
        "what are your capabilities"
        ]
    ):

     return {
        "intent": "CAPABILITIES",
        "target": None,
        "query": None
        }

    # ==========================================
    # EXIT
    # ==========================================

    if command in [
        "exit",
        "quit",
        "stop",
        "goodbye",
        "bye",
        "close yourself",
        "shutdown maddy"
    ]:
        return {
            "intent": "EXIT",
            "target": None,
            "query": None
        }

    # ==========================================
    # OPEN APPLICATION
    # ==========================================

    apps = {
        "chrome": [
            "chrome",
            "google chrome",
            "browser",
            "web browser"
        ],

        "vscode": [
            "vscode",
            "vs code",
            "visual studio code",
            "code editor"
        ],

        "notepad": [
            "notepad",
            "text editor"
        ],

        "calculator": [
            "calculator",
            "calc"
        ]
    }

    open_words = [
        "open",
        "launch",
        "start",
        "run"
    ]

    if any(word in command for word in open_words):

        for app_name, aliases in apps.items():

            for alias in aliases:

                if alias in command:

                    return {
                        "intent": "OPEN_APP",
                        "target": app_name,
                        "query": None
                    }

    # ==========================================
    # OPEN WEBSITES
    # ==========================================

    if "open youtube" in command:
        return {
            "intent": "OPEN_WEBSITE",
            "target": "youtube",
            "query": None
        }

    if "open google" in command:
        return {
            "intent": "OPEN_WEBSITE",
            "target": "google",
            "query": None
        }

    # ==========================================
    # GOOGLE SEARCH
    # ==========================================

    google_patterns = [
        r"search google for (.+)",
        r"google (.+)",
        r"search for (.+) on google",
        r"search (.+) on google"
    ]

    for pattern in google_patterns:

        match = re.search(pattern, command)

        if match:

            return {
                "intent": "GOOGLE_SEARCH",
                "target": "google",
                "query": match.group(1).strip()
            }

    # ==========================================
    # YOUTUBE SEARCH
    # ==========================================

    youtube_patterns = [
        r"search youtube for (.+)",
        r"search (.+) on youtube",
        r"youtube search (.+)"
    ]

    for pattern in youtube_patterns:

        match = re.search(pattern, command)

        if match:

            return {
                "intent": "YOUTUBE_SEARCH",
                "target": "youtube",
                "query": match.group(1).strip()
            }

    # ==========================================
    # FOLDERS
    # ==========================================

    if "open downloads" in command:
        return {
            "intent": "OPEN_FOLDER",
            "target": "downloads",
            "query": None
        }

    if "open documents" in command:
        return {
            "intent": "OPEN_FOLDER",
            "target": "documents",
            "query": None
        }

    if "open desktop" in command:
        return {
            "intent": "OPEN_FOLDER",
            "target": "desktop",
            "query": None
        }

    # ==========================================
    # TIME
    # ==========================================

    if any(
        phrase in command
        for phrase in [
            "what time is it",
            "tell me the time",
            "current time",
            "time"
        ]
    ):
        return {
            "intent": "TIME",
            "target": None,
            "query": None
        }

    # ==========================================
    # DATE
    # ==========================================

    if any(
        phrase in command
        for phrase in [
            "what is the date",
            "what's the date",
            "today's date",
            "today date",
            "tell me the date",
            "current date"
        ]
    ):
        return {
            "intent": "DATE",
            "target": None,
            "query": None
        }

    # ==========================================
    # SCREENSHOT
    # ==========================================

    if any(
        phrase in command
        for phrase in [
            "take a screenshot",
            "take screenshot",
            "screenshot",
            "capture screen",
            "capture my screen"
        ]
    ):
        return {
            "intent": "SCREENSHOT",
            "target": None,
            "query": None
        }

    # ==========================================
    # VOLUME UP
    # ==========================================

    if any(
        phrase in command
        for phrase in [
            "increase volume",
            "volume up",
            "turn up volume",
            "make volume louder"
        ]
    ):
        return {
            "intent": "VOLUME_UP",
            "target": None,
            "query": None
        }

    # ==========================================
    # VOLUME DOWN
    # ==========================================

    if any(
        phrase in command
        for phrase in [
            "decrease volume",
            "volume down",
            "turn down volume",
            "make volume lower"
        ]
    ):
        return {
            "intent": "VOLUME_DOWN",
            "target": None,
            "query": None
        }

    # ==========================================
    # MUTE
    # ==========================================

    if "mute" in command:

        return {
            "intent": "MUTE",
            "target": None,
            "query": None
        }

    # ==========================================
    # WINDOW CONTROL
    # ==========================================

    if any(
    phrase in command
    for phrase in [
        "minimize",
        "minimise",
        "minimize window",
        "minimise window",
        "minimize this",
        "minimise this"
     ]
    ):

         return {
        "intent": "MINIMIZE",
        "target": None,
        "query": None
         }

    if any(
        phrase in command
        for phrase in [
            "maximize",
            "maximise",
            "maximize window",
            "maximise window",
            "maximize this",
            "maximise this"
        ]
    ):

        return {
            "intent": "MAXIMIZE",
            "target": None,
            "query": None
        }

    # ==========================================
    # CLOSE CHROME
    # ==========================================

    close_words = [
    "close",
    "exit",
    "quit"
     ]

    if any(word in command for word in close_words):
        for app_name, aliases in apps.items():
            for alias in aliases:
                if alias in command:
                    return {
                    "intent": "CLOSE_APP",
                    "target": app_name,
                    "query": None
                    }

    # ==========================================
    # LOCK COMPUTER
    # ==========================================

    if any(
        phrase in command
        for phrase in [
            "lock computer",
            "lock my computer",
            "lock pc",
            "lock my pc"
        ]
    ):
        return {
            "intent": "LOCK",
            "target": None,
            "query": None
        }

    # ==========================================
    # RESTART
    # ==========================================

    if any(
        phrase in command
        for phrase in [
            "restart computer",
            "restart my computer",
            "restart pc",
            "restart my pc"
        ]
    ):
        return {
            "intent": "RESTART",
            "target": None,
            "query": None
        }

# ==========================================
# SHUTDOWN
# ==========================================

    if any(
    phrase in command
    for phrase in [
        "shutdown computer",
        "shut down computer",
        "shutdown my computer",
        "shut down my computer",
        "shutdown pc",
        "shut down pc",
        "turn off computer",
        "turn off my computer",
        "turn off pc"
    ]
    ):

        return {
        "intent": "SHUTDOWN",
        "target": None,
        "query": None
        }
    
    # ==========================================
    # CANCEL SHUTDOWN
    # ==========================================

    if "cancel shutdown" in command:

        return {
            "intent": "CANCEL_SHUTDOWN",
            "target": None,
            "query": None
        }

    # ==========================================
    # TYPE
    # ==========================================

    if command.startswith("type "):

        text = command[5:].strip()

        return {
            "intent": "TYPE",
            "target": None,
            "query": text
        }

    # ==========================================
    # UNKNOWN
    # ==========================================

    return {
        "intent": "UNKNOWN",
        "target": None,
        "query": command
    }