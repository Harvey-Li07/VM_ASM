import VMInit, sys

exit_counter: int = 1

while True:
    try:
        CommandInput: str = input("\n> ")
        print(CommandInput)
    except KeyboardInterrupt:
        if exit_counter != 2:
            print("\nTo exit, click on Control + C again.")
            exit_counter += 1
        else:
            sys.exit()