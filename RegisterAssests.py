import Buffers, typing, ReconfiguedPackages, warnings

AviliableRegisters: list = ["ax", "bx", "cx", "dx", "ex", "fx"]

class Null:
    def __init__(self) -> None:
        self.binarify = False
        self.binary = None
        self.booleanfy = False

class Register:
    def __init__(self, name: str) -> None:
        self.name = name
        self.Contents = []
        self.MaxContentsLength = 2**16
        self.Type = "Register"
        self.Restriction = False

    def PushContents(self, InfoBlock: tuple):
        """This will push a value from Buffer to the register. When a push is called, the register will 
        clear all contents for and push the content
        """
        # InfoBlock Format: (Buffer: Buffers.Buffer, Index: int)
        if self.Type == "Register":
            if self.Restriction != True:
                self.Contents.clear()
                self.Contents.append((Null, Buffers.BufferMethods.RetrieveContents(InfoBlock))[

                    len(str(Buffers.BufferMethods.RetrieveContents(InfoBlock))) <= self.MaxContentsLength

                    ])
            else:
                raise ValueError("This register has restrictions")
        else:
            raise ValueError(f"Incorrect type of register, expecting type Register but got {self.Type}")
    
    def PopContents(self):
        "Return the first value in the register ."
        content = self.Contents[0]
       # self.Contents.remove(self.Contents[0])
        return content
    
    @warnings.deprecated("Bad. Although these are valid methods, registers should not be randomly accessed")
    def RandAccess(self, index: int):
        if index + 1 <= len(self.Contents):
            return self.Contents[index]
        else:
            return Null


class PlaceRegister(Register):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.MaxContentsLength = 2
        self.Type = "PlaceRegister"
        self.Contents = Null
    
    @typing.override
    def PushContents(self, InfoBlock: tuple):
        try:
            int(Buffers.BufferMethods.RetrieveContents(InfoBlock))
        except Exception as e:
            raise e
        else:
            self.Contents = int(Buffers.BufferMethods.RetrieveContents(InfoBlock))

    @typing.override
    def PopContents(self):
        return self.Contents

class RegisterMethods:
    def RAWCompare(register1: Register, register2: Register):
        '''A raw form of comparing as they does not push the result to a register'''
        if register1.PopContents() == register2.PopContents():
            result = Buffers.BufferMethods.AutoAllocate("1")
        else:
            result = Buffers.BufferMethods.AutoAllocate("0")
        return result

    def Compare(register1: Register, register2: Register, resultRegister: PlaceRegister):
        '''This will push the result of the comparison register to the result register'''
        result = RegisterMethods.RAWCompare(register1, register2)
        resultRegister.PushContents((result[2], result[3]))

    @warnings.deprecated("This does not check for types or validity of the comparison. Use sub instead")
    def Subtraction(register1: Register, register2: Register):
        try:
            int(register1.PopContents())
            int(register2.PopContents())
        except Exception as e:
            raise e
        else:
            return Buffers.BufferMethods.AutoAllocate(int(register1.PopContents()) - int(register2.PopContents()))
        
def RegisterInit():
    global ax, bx, cx, dx, ex, fx
    global apx, bpx, cpx, dpx, epx, fpx
    ReconfiguedPackages.ConsolePrint("Initializing registers ................... ")
    ax = Register("ax")
    bx = Register("bx")
    cx = Register("cx")
    dx = Register("dx")
    ex = Register("ex")
    fx = Register("fx")

    apx = PlaceRegister("apx")
    bpx = PlaceRegister("bpx")
    cpx = PlaceRegister("cpx")
    dpx = PlaceRegister("dpx")
    epx = PlaceRegister("epx")
    fpx = PlaceRegister("fpx")

    ReconfiguedPackages.ConsolePrint("DONE \n")