import abc

class SysCall(abc.ABC):

    @abc.abstractmethod
    def call(callnum, *args): ...

    @abc.abstractmethod
    def syscall_0(*args): 
        '''Clear the current register'''
        ...

    @abc.abstractmethod
    def syscall_1(*args): 
        '''write the current value from the register to a Buffer'''
        ...

    @abc.abstractmethod
    def syscall_2(*args):
        '''retrieve the value from Buffer based on the current register value''' 
        ...
    
    @abc.abstractmethod
    def syscall_3(*args):
        '''display the current value of the register on output'''
        ...
    
    @abc.abstractmethod
    def syscall_4(*args): 
        '''reserve the current register/register of operation'''
        ...

    @abc.abstractmethod
    def syscall_5(*args):
        '''reset the current register'''
        ...
    
    @abc.abstractmethod
    def syscall_6(*args):
        '''retrieve and spawn an executable based on the current register value'''
        ...
    
    @abc.abstractmethod
    def syscall_7(*args):
        '''kill the current thread'''
        ...