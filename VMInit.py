import Buffers, RegisterAssests, ReconfiguedPackages, SystemPackMonitor.out #this is just to initialize it.
NumberedContents: dict = {}
CodeStructure: dict = {}

def freshBoot():
    Buffers.BufferInit()
    RegisterAssests.RegisterInit()
    ReconfiguedPackages.ConsolePrint("VM Init. finished")
    ReconfiguedPackages.ConsolePrint("")
