import Buffers, RegisterAssests, ReconfiguedPackages, SystemPackMonitor.out #this is just to initialize it. 

NumberedContents: dict = {}
CodeStructure: dict = {}

Buffers.BufferInit()
RegisterAssests.RegisterInit()
ReconfiguedPackages.ConsolePrint("VM Init. finished")
ReconfiguedPackages.ConsolePrint("")