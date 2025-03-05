import sys

sys.path.append('../VM_ASM')

from Pack.SysIO import SysIO, VMObject
from Pack.Decorators import Implementation
from typing import override
from ReconfiguedPackages import ConsolePrint
from Pack.Syscall import SysCall
import pathlib, sys, RegisterAssests, Buffers, ThreadManager

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
        

class SystemCall(SysCall):
    '''The implementation of Pack.Syscall.SysCall class'''
    def call(callnum, *args):
        #try:
            #raise Warning("All code for syscall has *not* been throughly tested. Unexpected behaviors may occur.\
            #              Use with caution. ")
        #except Warning as w:
            #print(w)
        if hasattr(SystemCall, f"syscall_{callnum}"):
            func = getattr(SystemCall, f"syscall_{callnum}")
            func(*args)
        else:
            raise AttributeError("The System Call is not defined.")
    
    def __SuperRegister__(register: str) -> RegisterAssests.Register:
        '''Check if the register exists, if so, get the register otherwise raise an AttributeError'''
        if hasattr(RegisterAssests, register):
            return getattr(RegisterAssests, register)
        else:
            raise AttributeError(f"The register {register} cannot be found.")

    @override
    def syscall_0(*args):
        r: RegisterAssests.Register = SystemCall.__SuperRegister__(args[0])
        r.Contents.clear()
    
    @override
    def syscall_1(*args) -> tuple:
        r: RegisterAssests.Register = SystemCall.__SuperRegister__(args[0])
        return Buffers.BufferMethods.AutoAllocate(r.PopContents())
    
    @override
    def syscall_2(*args):
        raise DeprecationWarning("Don't do that.")
    
    @override
    def syscall_3(*args):
        r: RegisterAssests.Register = SystemCall.__SuperRegister__(args[0])
        print(r.PopContents())
    
    @override
    def syscall_4(*args):
        r: RegisterAssests.Register = SystemCall.__SuperRegister__(args[0])
        r.Restriction = True

    @override
    def syscall_5(*args):
        ConsolePrint("Redirecting syscall to syscall_0")
        SystemCall.syscall_0(args)

    @override
    def syscall_6(*args):
        raise NotImplementedError("This will be implemented in SDK v1.1+")
    
    @override
    def syscall_7(*args):
        if args[0] in ThreadManager.RunningThreads:
            ThreadManager.__ThreadingExit.update({args[0]: True})
        else:
            raise ValueError("The specified Thread cannot be found.")
        