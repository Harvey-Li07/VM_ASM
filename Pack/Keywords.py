import sys, os, pathlib

sys.path.append('../VM_ASM')

import Scope as scope
import SDK.SpecificProgramScope.Constants as Constants


def use(*arg):
    if arg[0] in list(scope.PhoneBook.keys()):
        Constants.SDK_PATH = pathlib.Path(scope.PhoneBook[arg[0]]).absolute()
    elif os.path.exists(arg[0]) and os.path.exists(f"{arg[0]}/PackImplementations/.SDK_MARKER"):
        Constants.SDK_PATH = pathlib.Path(arg[0]).absolute()
    else:
        raise FileNotFoundError("Please specify a path to your custom SDK")
    
def global_property(*arg):
    if arg[0] in list(Constants.PROGRAM_METADATA.keys()):
        Constants.PROGRAM_METADATA.update({arg[0].captalize(): arg[1]})
    else:
        raise SyntaxError("The property specified is invalid. For SDK version 1.1+, use @create to create the property")
    
def create(*arg):
    assert Constants.PROGRAM_METADATA["SDK_VERSION"] != "1.0", "This method is not supported in SDK version < 1.1"
    if arg[2] in list(keywords.keys()):
        Constants.PROGRAM_METADATA.update({arg[2]: arg[3]})
    else:
        raise SyntaxError("Invalid data type")


def boolean(*arg):
    if len(arg) != 0:
        return True
    else:
        return False

keywords: dict = {"use": use, "global_property": global_property, "boolean": boolean}