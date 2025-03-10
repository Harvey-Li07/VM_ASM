import VMInit, sys, Commands, PublicVariables as pv, readline

VMInit.freshBoot()

print("VM State: RUNNING \n")
while True:
    try:
        CommandInput: str = input("> ")
        CommandSplited : list[str] = CommandInput.split()
        getattr(Commands, CommandSplited[0])(*CommandSplited[1:])
    except KeyboardInterrupt:
        if pv.CommandLineBehavior["allow_control_c_override"]:
            sys.exit(0)
        else:
            print("Shell: Exit upon Control + C failed, change this by using command: ```set allow_control_c_override true```")
    except IndexError as e:
        print(f"Shell: {e}")
    except FileNotFoundError as f:
        print(f'Shell: {f}')
    except AttributeError as a:
        print(f'Shell: {a}. Command Not Found')
    except ValueError as v:
        print(f'Shell: {v}')
    except Exception as e:
        print(f"\n Shell: Fatal Exception: {e}")
        if pv.CommandLineBehavior["exit_on_fatal_error"]:
            print("VM State: STOPPED \n")
            sys.exit(1)
        