import sys
sys.path.append('../VM_ASM')

import Panics

def Implementation(func):
    def setter(self, *args, **kwargs):
        self.__is_implementation__ = True
    return setter

def ThrowsErrorType(ErrorType: str | object):
    def Decorator(func):
        def setter(self, ErrorType):
            if type(ErrorType) is str:
                self.__ErrorType__ = ErrorType
            else:
                self.__ErrorType__ = ErrorType.__name__
        return setter(func, ErrorType=ErrorType)
    return Decorator

def ExitShield(func):
    def shield(func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except Panics.ExitSignal:
            ...
        except Exception as e:
            raise e
    return shield