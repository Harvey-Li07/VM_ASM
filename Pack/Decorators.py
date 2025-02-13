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