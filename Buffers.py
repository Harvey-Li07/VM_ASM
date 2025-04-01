import typing, sys, ReconfiguedPackages

AviliableBuffers: list = ["Buffer1", "Buffer2", "Buffer3", "Buffer4", "Buffer5"]
ReservedBufferInfo: dict = {}

class Buffer:
    def __init__(self, name) -> None:
        self.WriteCounter = -1
        self.name: str = name
        self.CapSize = 8
        self.RemainingSize = self.CapSize
        self.contents: list = [ ]
        self.UsedReservedBufferSpace = 0
        self.type = "BUFFER"

    def ChangeCapSize(self, power: int):
        self.RemainingSize = 2**(abs(power), 16)[abs(power) > 63]
    
    def PushContents(self, contents: any) -> tuple: #return index of the content in the given buffer
        if type(contents) != bool:
            self.contents.append(contents)
            self.LastUsedSize: int = len(str(contents))
            self.RemainingSize -= len(str(contents))
        elif type(contents) == bool:
            self.contents.append(contents)
            self.RemainingSize -= 1
            self.LastUsedSize: int = 1
        else:
            raise ValueError(f"Not Enough Space in {self.name}")
        self.WriteCounter += 1
        return (self.name, True)
    
    def Clear(self):
        self.contents = []
        self.RemainingSize = self.CapSize

    def ReserveSpace(self, AmountReserved):
        if AmountReserved <= self.RemainingSize:
            self.UsedReservedBufferSpace = AmountReserved
            self.RemainingSize -= AmountReserved
            ReservedBufferInfo.update({self.name: AmountReserved})
            return (self.name, AmountReserved)
        else:
            raise ValueError(f"Not Enough Aviliable Space in Buffer Named {self.name}")
        
    def YieldOnIndex(self, index: int):
        if index <= len(self.contents):
            return self.contents[index]
        else:
            raise IndexError(f"Attempted to access an unexplored field of {self.name}")
        
    def ClearReserve(self):
        self.RemainingSize += self.UsedReservedBufferSpace
        ReservedBufferInfo.pop(self.name)
        self.UsedReservedBufferSpace = 0

class BufferMethods:

    def NamedAllocate(BufferName: Buffer, Contents) -> tuple: #(RemainingSize, UsedSize)
        _BufferName: Buffer = BufferName

        _BufferName.PushContents(contents=Contents)

        return (_BufferName.RemainingSize, _BufferName.LastUsedSize)
    
    def AutoAllocate(Contents: any) -> tuple:
        ContentSize: int = str(Contents).__len__()
        "Output Structure: (RemainingSize, ContentLength, BufferUsed, Index_in_Buffer)"
        UsableBuffers: list = []
        SizesOfBuffers: list = []

        for x in AviliableBuffers:
            BufferSize:int = globals()[x].RemainingSize
            if ContentSize <= BufferSize:
                UsableBuffers.append(x)
                SizesOfBuffers.append(BufferSize)

        if len(UsableBuffers) > 0 and len(SizesOfBuffers) > 0:
            ResultBuffer: Buffer = globals()[UsableBuffers[SizesOfBuffers.index(max(SizesOfBuffers))]]
        else:
            raise ValueError("Not enough Buffers with aviliable space")
    

        ResultBuffer.ReserveSpace(ContentSize)
        ResultBuffer.PushContents(contents=Contents)
        ResultBuffer.ClearReserve()

        return (ResultBuffer.RemainingSize, ResultBuffer.LastUsedSize, ResultBuffer.name, ResultBuffer.WriteCounter)
    
    def RetrieveContents(LocationInfo: tuple):
        ResultBuffer: Buffer = globals()[LocationInfo[0]]
        return ResultBuffer.contents[LocationInfo[1]]
    
    def ClearUp(Buffers: str):
        if Buffers == 'all':
            for x in AviliableBuffers:
                target_Buffer: Buffer = globals()[x]
                target_Buffer.Clear()
        else:
            target_Buffer: Buffer = globals()[Buffers]
            target_Buffer.Clear()
    
    def ReleaseBuffer(): ...

def BufferInit():
    '''this will initialize all the buffers.'''
    global Buffer1, Buffer2, Buffer3, Buffer4, Buffer5
    global DynBuffer1, DynBuffer2, DisplBuffer

    ReconfiguedPackages.ConsolePrint("Initializing Buffers ............ ")
    # Regular Buffer
    Buffer1 = Buffer("Buffer1")
    Buffer2 = Buffer("Buffer2")
    Buffer3 = Buffer("Buffer3")
    Buffer4 = Buffer("Buffer4")
    Buffer5 = Buffer("Buffer5")

    ReconfiguedPackages.ConsolePrint(" DONE \n")
    
    ReconfiguedPackages.ConsolePrint("Buffer Configuration ")
    for x in AviliableBuffers:
        globals()[x].ChangeCapSize(8)
        ReconfiguedPackages.ConsolePrint("...")
    ReconfiguedPackages.ConsolePrint(" DONE \n")