class IOPanic(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class ObjectPanic(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class ExitSignal(Exception):
    def __init__(self, *args):
        super().__init__(*args)