# ==========================================
# MADDY V2
# ==========================================

from voice import listen, speak
from commands import process_command


# ==========================================
# MAIN
# ==========================================

def main():

    print("=" * 50)
    print("             MADDY V2")
    print("       Voice Computer Assistant")
    print("=" * 50)

    speak(
        "Hello. Maddy is ready."
    )

    while True:

        command = listen()

        if not command:
            continue

        print(
            f"\nHeard: {command}"
        )

        # ----------------------------------
        # CHECK WAKE WORD
        # ----------------------------------

        if "maddy" in command:

            should_continue = process_command(
                command
            )

            if not should_continue:

                break

        else:

            print(
                "Wake word not detected."
            )


# ==========================================
# START
# ==========================================

if __name__ == "__main__":

    main()