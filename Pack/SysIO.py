import Scope as scope

import Panics as Panics, abc

class VMObject:

    def __init__(self, callable: bool, annoations: str = "", AutoCall: bool = False, args:list[str] = None):
        #it will spawn a new VMObject
        self.callable = callable
        self.callback: list
        self.annotations = annoations
        self.args = args
        self.TYPE: str
        self.AcceptableAnnotations = {"[silent]": VMObject.__silent, 
                                      "[verbal]": VMObject.__verbal, 
                                      "[init]": VMObject.__initializer}
        self.__threadable__ = False
        self.__AutoCall__ = AutoCall
        if self.__AutoCall__:
            self.Run()
    
    def __call(self):
        if not self.callable:
            raise Panics.ObjectPanic("Calling an uncallable object ... nothing will be done")
        else:
            for x in self.callback:
                for j in self.args:
                    x(j)
    
    def CompileAnnotations(self): # annotations contained in brakets connected with &
        if len(self.annotations.split("&")) > 0 or self.annotations != "":
            annot = self.annotations.split("&")
            for x in annot:
                if x in list(self.AcceptableAnnotations.keys()):
                    self.AcceptableAnnotations[x]()
                else:
                    raise Panics.ObjectPanic("An invalid annotation has been specified")
    
    def Run(self):
        self.CompileAnnotations()
        self.__call()

    #Below are definition of annotations
    def __silent():
        scope.PhoneBook.update({"DEFAULT_OUT":None})

    def __verbal():
        scope.PhoneBook.update({"DEFAULT_OUT":"Register"})

    def __initializer(): #PLEASE FOR THE LOVE OF GOD, OVERRIDE THIS METHOD WHEN USE
        '''WARNING: Please override this method in your own implementation of the SysIO_Object or SysDynamic_Object
         if you wish to use this annotation. For now, it will yell at your face if you call it raw. 

         PLEASE FOR THE LOVE OF GOD OVERRIDE THIS METHOD BEFORE USE

        '''
        assert getattr(VMObject.initializer, '__override__', False) is True, \
            "This method is not overriden, do not do this again"


class SysIO(abc.ABC):

    def __init__(self):
        self.__is_implementation__ = False
        self.Name = "SysIO(abc.ABC)"

    @abc.abstractmethod
    def Out(a: str) -> None:
        """This pushes the string object (from parameter) to 
        the display pack at SystemPack/out.vmp
        """
        ...
    @abc.abstractmethod
    def Write(a: any, destination) -> None: 
        '''Write the argument 'a' to the destination'''
        ...

    @abc.abstractmethod
    def Syscall(a: str, *args) -> None: 
        '''Conduct a syscall. Should only be implemented **once**.'''
        ...

    @abc.abstractmethod
    def Kill(a: str, *args) -> None :
        '''Kill the current thread'''
        ...

    @abc.abstractmethod
    def SpawnThreadableObject(handle: str, callback: any, *args) -> VMObject: 
        '''This will spawn a what is known as _threadable_ object 
        which should only be used to register a thread using provided methods \n
        **How does this work?**

        + This will spawn a new VMObject and attempt to set a property ```__threadable__``` to be true.
        '''
        ...