import subprocess

if __name__ == "__main__":
    cmd_choice = input("Enter command to run: ").strip().lower()

    # replace commands or have user enter it
    if cmd_choice in ("help", "Help", "HELP"):
        print(
            "Options:\n"
            "- echo: Print user input.\n"
            "- ls: List directory contents. Default is current working directory."
        )
        raise SystemExit(0)

    elif cmd_choice == "echo":
        msg = input("What do you want to input? ").strip()
        result = subprocess.run(["echo", msg], capture_output=True, text=True)

    elif cmd_choice == "ls":  # note windows might be different
        path = input("Directory to list (blank for current): ").strip() or "."
        result = subprocess.run(["ls", path], capture_output=True, text=True)

    else:
        print("Unknown command choice, exiting.")
        raise SystemExit(1)

    print("\nReturn code:", result.returncode)
    print("Stdout:", result.stdout.strip())
    print("Stderr:", (result.stderr or "").strip())
