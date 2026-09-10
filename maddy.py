
# ==========================================
# MADDY V3.6.1 - SMART LISTENING
# ==========================================

from voice import listen, speak
from commands import process_command
from conversation import start_conversation


# ==========================================
# SMART LISTENING MODE
# ==========================================

SMART_LISTENING = False


def main():

    global SMART_LISTENING

    print("=" * 60)
    print("                    MADDY V3.6.1")
    print("             Voice Computer Assistant")
    print("=" * 60)

    speak("Hello. I am Maddy. How can I help you?")

    while True:

        # ==========================================
        # LISTEN FOR COMMAND
        # ==========================================

        command = listen()

        if not command:
            continue

        print(f"\nHeard: {command}")

        command_lower = command.lower().strip()

        # ==========================================
        # SMART LISTENING MODE
        # ==========================================

        if SMART_LISTENING:

            # Commands that stop smart listening
            sleep_phrases = [
                "go to sleep",
                "stop listening",
                "stop listening maddy",
                "that's enough",
                "thats enough",
                "sleep",
                "exit listening mode"
            ]

            if any(
                phrase in command_lower
                for phrase in sleep_phrases
            ):

                speak("Okay. I'll wait until you need me.")

                SMART_LISTENING = False

                print("\nSmart Listening: OFF")

                continue

            # Process command without requiring wake word
            should_continue = process_command(command)

            if not should_continue:
                break

            continue

        # ==========================================
        # WAKE WORD DETECTION
        # ==========================================

        if "maddy" in command_lower:

            # Remove wake word
            cleaned_command = (
                command_lower
                .replace("hey maddy", "")
                .replace("hello maddy", "")
                .replace("hi maddy", "")
                .replace("maddy", "")
                .strip()
            )

            # ==========================================
            # ONLY "HEY MADDY"
            # ==========================================

            if not cleaned_command:

                speak(
                    "I'm listening. What would you like me to do?"
                )

                SMART_LISTENING = True

                print("\nSmart Listening: ON")

                continue

            # ==========================================
            # COMMAND WITH WAKE WORD
            # ==========================================

            should_continue = process_command(command)

            if not should_continue:
                break

        else:

            print("Wake word not detected.")


if __name__ == "__main__":
    main()

