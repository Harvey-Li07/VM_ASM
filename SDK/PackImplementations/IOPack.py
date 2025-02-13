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
    def SpawnThreadableObject(callback, *args):
        if len(args) > 0:
            ThreadableObject = VMObject(callable=True, callback=callback, AutoCall=True,args=list(args))
            ThreadableObject.__threadable__ = True
            return ThreadableObject
        else:
            ThreadableObject = VMObject(callable=True, callback=callback, AutoCall=True)
            ThreadableObject.__threadable__ = True
            return ThreadableObject