import Buffers, RegisterAssests, ReconfiguedPackages, SystemPackMonitor.out #this is just to initialize it.
NumberedContents: dict = {}
CodeStructure: dict = {}

def freshBoot():
    '''Make sure it is a fresh boot'''
    Buffers.BufferInit()
    RegisterAssests.RegisterInit()
    ReconfiguedPackages.ConsolePrint("VM Init. finished\n")
    ReconfiguedPackages.ConsolePrint("")
