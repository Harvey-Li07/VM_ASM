import sys

sys.path.append('../VM_ASM')

from Pack.SysIO import SysIO, VMObject
from Pack.Decorators import Implementation
from typing import override
from ReconfiguedPackages import ConsolePrint
import pathlib, sys

class SysIO_IMPL(SysIO):
    
    @Implementation
    def __init__(self):
        super().__init__()

    @override
    def Out(a: str):
        ConsolePrint(a)
        ConsolePrint("")

    @override
    def Write(a, destination):
        with open(pathlib.Path(destination).absolute(), "a+") as f:
            f.write(a)
            f.close()
    
    @override
    def SpawnThreadableObject(handle, callback, *args):
        ThreadableObject = VMObject(callable=True, callback=callback, args=args)
        ThreadableObject.__threadable__ = True
        ThreadableObject.__exit_signal__ = False
        return ThreadableObject