# ==========================================
# MADDY V3
# ==========================================

from voice import listen, speak
from commands import process_command


def main():

    print("=" * 60)
    print("                    MADDY V3")
    print("              Voice Computer Assistant")
    print("=" * 60)

    speak(
        "Hello. I am Maddy. How can I help you?"
    )

    while True:

        command = listen()

        if not command:
            continue

        print(f"\nHeard: {command}")

        # Check whether Maddy was called
        if "maddy" in command.lower():

            should_continue = process_command(command)

            if not should_continue:
                break

        else:

            print(
                "Wake word not detected."
            )


if __name__ == "__main__":
    main()