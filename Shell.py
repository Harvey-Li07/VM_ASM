import VMInit, sys, Commands, PublicVariables as pv

exit_counter: int = 1

VMInit.freshBoot()

print("\n VM State: RUNNING \n")
while True:
    try:
        CommandInput: str = input("> ")
        CommandSplited : list[str] = CommandInput.split()
        getattr(Commands, CommandSplited[0])(*CommandSplited[1:])
    except KeyboardInterrupt:
        if exit_counter != 2:
            print("\nTo exit, click on Control + C again.")
            exit_counter += 1
        else:
            if pv.CommandLineBehavior["allow_ctrl_c_override"]:
                sys.exit()
            else:
                print("Shell: Cannot exit upon Control + C, change this by using command: set allow_control_c_override true")
    except IndexError as e:
        print(f"Shell: Exception at: {e}")
    except FileNotFoundError as f:
        print(f'Shell: Exception at {f}')
    except AttributeError as a:
        print(f'Shell: Exception at {a}. Command Not Found')
    except ValueError as v:
        print(f'Shell: Exception at {v}')
    except Exception as e:
        print(f"\n Shell: Fatal Exception at: {e} \n VM State: STOPPED \n")
        if pv.CommandLineBehavior["exit_on_fatal_error"]:
            sys.exit(1)
