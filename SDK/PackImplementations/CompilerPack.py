import sys, typing

sys.path.append('../VM_ASM')

from Pack.Compiler import CompilerBase, Execuatable 
import Pack.Keywords as keywords
import SDK.PackImplementations.VMMethods as VMMethods
import Buffers as buffer

class ExecutableClass(Execuatable):
    
    def __init__(self, annoations=None):
        super().__init__(annoations)
        self.LocationInBuffer: tuple
        self.callable = True
        self.callback = self.Call
        self.TYPE = "Executable"

    @typing.override
    def Call(self):
        for x in range(0, self.InstructionSet.__len__()):
            self.InstructionSet[x](*self.args[x])

    @typing.override
    def Run(self):
        self.Call()

    @typing.override
    def __code__(self):
        return [self.InstructionSet, self.args]

    @typing.override
    def __len__(self):
        return (int(sys.getsizeof(self)/ 100), 10)[int(sys.getsizeof(self)/ 100) < 1]


class Compiler(CompilerBase):

    def __init__(self):
        super().__init__()
        self.__CompiledInstructions__ = []
        self.FetchedContents = False

    @typing.override
    def GetInstructions(self, FetchedContents):
        if type(FetchedContents) is str:
            self.RawInstructions: list[str] = FetchedContents.split(sep='\n')
        else:
            self.RawInstructions:list[str] = FetchedContents
        self.FetchedContents = True

    @typing.override
    def CompileInstruction(self):
        CompiledInstruction: list = []
        Arguments: list = []
        for x in self.RawInstructions:
            if x[0] == "@":
                line: list = x.split(sep=' ')
                keywords.keywords[x[1:]](*line)
            else:
                line: list[str] = x.split(sep=" ")
                CompiledInstruction.append(getattr(VMMethods, line[0]))
                Arguments.append([line[1].replace(",", ""), line[2]])
        self.__CompiledInstructions__ = [CompiledInstruction, Arguments]
    
    @typing.override
    def SpawnExecutable(self, annot: str = None):
        Exec = ExecutableClass(annot)
        Exec.InstructionSet = self.__CompiledInstructions__[0]
        Exec.args = self.__CompiledInstructions__[1]
        return buffer.BufferMethods.AutoAllocate(Exec)

def VMSnapshot(*args):
    ...