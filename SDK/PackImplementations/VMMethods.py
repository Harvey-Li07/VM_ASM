import sys

sys.path.append('../VM_ASM')

import RegisterAssests, Buffers, pathlib, ReconfiguedPackages as rp
from SDK.PackImplementations.IOPack import SystemCall

def mov(*args):
    if args[0] in RegisterAssests.AviliableRegisters:
        Register1: RegisterAssests.Register = getattr(RegisterAssests, args[0])
        if args[1] in RegisterAssests.AviliableRegisters:
            Register2: RegisterAssests.Register = getattr(RegisterAssests, args[1])
            Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(Register2.PopContents())
            Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
        else:
            Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(args[1])
            Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
    else:
        raise NameError("Designated Register cannot be found.")

def add(*args):
    if args[0] in RegisterAssests.AviliableRegisters: 
        Register1: RegisterAssests.Register = getattr(RegisterAssests, args[0])
        if args[1] in RegisterAssests.AviliableRegisters:
            Register2: RegisterAssests.Register = getattr(RegisterAssests, args[1])
            try: 
                Register1.PopContents()
            except IndexError:
                Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(Register2.PopContents())
                Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
            else:
                try:
                    int(Register1.PopContents())
                    int(Register2.PopContents())
                except IndexError:
                    Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(Register1.PopContents() + Register2.PopContents())
                    Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
                else:
                    Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(int(Register1.PopContents()) + int(Register2.PopContents()))
                    Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
        else:
            Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(args[1])
            Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
    else:
        raise NameError("Designated Register cannot be found.")

def sub(*args):
    if args[0] in RegisterAssests.AviliableRegisters:
        Register1: RegisterAssests.Register = getattr(RegisterAssests, args[0])
        if args[1] in RegisterAssests.AviliableRegisters:
            Register2: RegisterAssests.Register = getattr(RegisterAssests, args[1])
            try: 
                Register1.PopContents()
            except IndexError:
                raise IndexError("Nothing can be found in register 1.")
            else:
                Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(int(Register1.PopContents()) - int(Register2.PopContents()))
                Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
        else:
            Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(int(Register1.PopContents()) - int(args[1]))
            Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
    else:
        raise NameError("Designated Register cannot be found.")
    
def syscall(*args):
    #conduct a syscall
    SystemCall.call(args[0],args[1])