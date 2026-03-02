import VMInit, sys, Commands, PublicVariables as pv, gnureadline

'''
Module gnureadline is an open-source software by the GNU Foundation and is licensed under GNU General Public License, version 3.
This code wad made freely available by Chet Ramey and the GNU Foundation, the code can be obtained from: 
https://tiswww.cwru.edu/php/chet/readline/rltop.html#Availability
 '''

VMInit.freshBoot()

print("VM State: RUNNING \n")
while True:
    try:
        CommandInput: str = input("> ")
        CommandSplited : list[str] = CommandInput.split()  
        if CommandSplited[0][0:2] == "./":
            Commands.do(CommandSplited[0][2:])
        else:
            getattr(Commands, CommandSplited[0])(*CommandSplited[1:])

    except KeyboardInterrupt:
        if pv.CommandLineBehavior["allow_control_c_override"]:
            sys.exit(0)
        else:
            print("Shell: Exit upon Control + C failed, change this by using command: ```set allow_control_c_override true```")
    except IndexError as e:
        print(f"Shell: ({type(e).__name__}) {e}")
    except FileNotFoundError as f:
        print(f'Shell: ({type(f).__name__}) {f}')
    except AttributeError as a:
        print(f'Shell: {a}. Command Not Found')
    except ValueError as v:
        print(f'Shell: ({type(v).__name__}) {v}')
    except Exception as e:
        print(f"\n Shell: Fatal Exception: ({type(e).__name__}) {e}")
        if pv.CommandLineBehavior["exit_on_fatal_error"]:
            print("VM State: STOPPED \n")
            sys.exit(1)
        