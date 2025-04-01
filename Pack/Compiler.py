from Pack.SysIO import VMObject
import abc


class Execuatable(abc.ABC, VMObject):
    '''
    The Base/Abstract class for Executable and the majority of the methods are inherited from ```Pack.SysIO.VMObject```.
      This acts as an executable "file" that can be called to perform operations with the registers in the VM. 
      '''
    def __init__(self, annoations = None): #spawn an execuatble object
        '''This will spawn a blank executable with no instructions, annotations are set to ```None``` and I
        intended to keep it that way. '''
        super().__init__(callable=True, annoations=annoations)
        self.TYPE = "Executable"
        self.InstructionSet: list
        self.ValidInstructions: dict
        self.args: list[str]

    @abc.abstractmethod
    def __len__(self) -> int: 
        '''Gives the Executable class length, used to calculate the size occupied by this object'''
        ...

    @abc.abstractmethod
    def __code__(self) -> list[str]: 
        '''Throws out all the instructions stored in this executable object'''
        ...

    @abc.abstractmethod
    def Call(self) -> None: 
        '''Call this executable object; THIS SHOULD NOT RETURN ANYTHING'''
        ...



class CompilerBase(abc.ABC):

    '''The interface/base class for the compiler which takes input from the user's file and 
        compile all the instructions into an executable class (defined above). This instance and
        this _particular_ implementation of the SDK is located at SDK/PackImplmentations/CompilerPack.
    '''
    
    def __init__(self):
        '''Again, spawns a Compiler Object'''
        self.RawInstructions: list

    @abc.abstractmethod
    def CompileInstruction(self) -> None: 
        '''This will compile all the instructions provided in a custom property from self
        in ```CompilerBase``` and/or its custom implementations in IOPack
        '''
        ...

    @abc.abstractmethod
    def SpawnExecutable(self) -> tuple: 
        '''This will pack all the compiled instructions into the executable class which is then pushed to Buffer.
        The return is the location in the buffer, which is a tuple. 
        '''
        ...

    @abc.abstractmethod
    def GetInstructions(self, FetchedContents: str | list) -> None: 
        '''This function intakes a list of contents in a file and stores them into the compiler.'''
        ...