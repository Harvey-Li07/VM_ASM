from Pack.SysIO import VMObject
import abc

class Execuatable(abc.ABC, VMObject):
    def __init__(self, annoations = None): #spawn an execuatble object
        super().__init__(callable=True, annoations=annoations)
        self.TYPE = "Executable"
        self.InstructionSet: list
        self.ValidInstructions: dict
        self.args: list[str]

    @abc.abstractmethod
    def __len__(self) -> int: ...

    @abc.abstractmethod
    def Call(self) -> None: ...



class CompilerBase(abc.ABC):
    
    def __init__(self):
        self.RawInstructions: list

    @abc.abstractmethod
    def CompileInstruction(self) -> None: 
        '''This will compile all the instructions provided in a custom property from self
        in SysIO.VMObject and/or its custom implementations in IOPack
        '''
        ...

    @abc.abstractmethod
    def SpawnExecutable(self) -> tuple: ...

    @abc.abstractmethod
    def GetInstructions(self, FetchedContents: str | list) -> None: ...