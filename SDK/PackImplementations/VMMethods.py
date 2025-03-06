import sys

sys.path.append('../VM_ASM')

import RegisterAssests, Buffers, pathlib, ReconfiguedPackages as rp
from SDK.PackImplementations.IOPack import SystemCall
from SDK.SpecificProgramScope.Constants import DEBUG_MODE

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
    
def write(*args):
    if args[0] in Buffers.AviliableBuffers:
        bufferResult: Buffers.Buffer = getattr(Buffers, args[0])
        print(Buffers.BufferMethods.NamedAllocate(bufferResult, args[0:]))
    else:
        raise NameError("Designated Buffer cannot be found")

def syscall(*args):
    #conduct a syscall
    SystemCall.call(args[0],args[1])

def DebugMode():
    DEBUG_MODE = True
    print('WARNING: This mode is not tested and it grant you access to directly write to a register \
          or into the buffer area. USE WITH CAUSION; WE HAVE WARNED YOU ABOUT THE ISSUE')
    while DEBUG_MODE:
        try:
            debug_in: list[str] = input("DEBUG SHELL> ").split()
            locals()[debug_in[0]](*debug_in[0:])
        except KeyboardInterrupt:
            DEBUG_MODE = False
        except Exception as e:
            print(f"Debug Shell: Exception at {e}")
    DEBUG_MODE = False