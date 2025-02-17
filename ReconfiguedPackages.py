import pathlib
import Scope as scope


def ConsolePrint(contents: str):
    if scope.PhoneBook["DEFAULT_OUT"] != None:
        with open(pathlib.Path(scope.PhoneBook["DEFAULT_OUT"]).absolute(), 'a') as f:
            f.write(str(contents))
            f.close()
