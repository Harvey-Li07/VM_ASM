import Buffers
from typing import override

class RAM(Buffers.Buffer):

    def __init__(self, name):
        super().__init__(name)
        self.CapSize = 1024
        self.type = "RAM"

    @override
    def ChangeCapSize(self, power):
        raise NotImplementedError
    

class RAMMethods(Buffers.BufferMethods):

    def AutoAllocate(Contents):
        return super().AutoAllocate()
    
    @override
    def NamedAllocate(BufferName, Contents):
        raise NotImplementedError
    

def RAMInit():

    RAMField1 = RAM("RAMField1")

    