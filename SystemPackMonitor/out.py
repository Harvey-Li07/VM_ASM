import sys, time ,threading as mtp
sys.path.append('../VM_ASM')

import Scope as scope

import pathlib

def PRINT():
    '''the reconfigured type of print. This will write to the output file and from which it will display the value to the screen'''
    while True:
        with open(pathlib.Path(scope.PhoneBook["DEFAULT_OUT"]).absolute(), 'r+') as f:
            contents = f.readlines()
            if len(contents) > 0:
                print(contents[contents.__len__() - 1], end="")
            f.truncate(0)

if __name__ == "SystemPackMonitor.out":
    print("Starting monitor thread")
    process = mtp.Thread(target=PRINT, name="Console Print Support", daemon=True)
    process.start()
