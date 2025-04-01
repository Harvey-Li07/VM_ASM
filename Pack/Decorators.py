import sys
sys.path.append('../VM_ASM')

import Panics, warnings

def Implementation(func):
    '''To annotate that this is an implementation of the class/object'''
    def setter(self, *args, **kwargs):
        self.__is_implementation__ = True
    return setter

def ThrowsErrorType(ErrorType: str | object):
    '''try to annotate the error type which the decorated will throw'''
    def Decorator(func):
        def setter(self, ErrorType):
            if type(ErrorType) is str:
                self.__ErrorType__ = ErrorType
            else:
                self.__ErrorType__ = ErrorType.__name__
        return setter(func, ErrorType=ErrorType)
    return Decorator

@warnings.deprecated("Use try ... except instead of this. ")
def ExitShield(func):
    '''Shield for the exit signal. Deprecated. dont use it. '''

    def shield(func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except Panics.ExitSignal:
            ...
        except Exception as e:
            raise e
    return shield