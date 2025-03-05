import VMInit, sys, Commands

exit_counter: int = 1

print("\n VM State: RUNNING \n")
while True:
    try:
        CommandInput: str = input("\n> ")
        CommandSplited : list[str] = CommandInput.split()
        getattr(Commands, CommandSplited[0])(*CommandSplited[1:])
    except KeyboardInterrupt:
        if exit_counter != 2:
            print("\nTo exit, click on Control + C again.")
            exit_counter += 1
        else:
            sys.exit()
    except Exception as e:
        print(f"\n Exception at: {e} \n VM State: STOPPED \n")
        sys.exit(1)