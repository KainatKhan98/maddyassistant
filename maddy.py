# ==========================================
# MADDY V3.4
# CONVERSATION MODE
# ==========================================

from voice import listen, speak
from commands import process_command
from conversation import start_conversation


# ==========================================
# MAIN
# ==========================================

def main():

    print("=" * 60)
    print("                    MADDY V3.4")
    print("             Voice Computer Assistant")
    print("=" * 60)

    speak(
        "Hello. I am Maddy. How can I help you?"
    )

    while True:

        # ----------------------------------
        # Wake-word listening
        # ----------------------------------

        command = listen()

        if not command:
            continue

        print(f"\nHeard: {command}")

        command_lower = command.lower()

        # ----------------------------------
        # Wake word detected
        # ----------------------------------

        if "maddy" in command_lower:

            # --------------------------------
            # If the wake word is followed
            # by a command, execute it
            # --------------------------------

            cleaned_command = (
                command_lower
                .replace("hey maddy", "")
                .replace("hello maddy", "")
                .replace("hi maddy", "")
                .replace("maddy", "")
                .strip()
            )

            # --------------------------------
            # Just saying "Maddy"
            # --------------------------------

            if not cleaned_command:

                should_continue = start_conversation()

                if not should_continue:
                    break

                continue

            # --------------------------------
            # Wake word + command
            # --------------------------------

            should_continue = process_command(command)

            if not should_continue:
                break

            # --------------------------------
            # Ask whether user wants
            # conversation mode
            # --------------------------------

            continue

        else:

            print(
                "Wake word not detected."
            )


# ==========================================
# START MADDY
# ==========================================

if __name__ == "__main__":

    main()