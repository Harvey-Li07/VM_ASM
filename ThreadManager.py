import threading, typing
from SDK.PackImplementations.IOPack import SysIO_IMPL as SysIO
from Pack.SysIO import VMObject
from SDK.PackImplementations.CompilerPack import ExecutableClass as executable

RunningThreads: list[threading.Thread] = []

__ThreadingExit: dict[str: bool] = {}

def SpawnThread(CompiledObject: VMObject | executable) -> threading.Thread:

    '''
    This function will spawn a thread object in a safe and organized manner but it will
    not start the thread. See function/method ```StartThread(ThreadObject: threading.Thread)```
    to start the thread safely. 
    '''

    if not CompiledObject.__threadable__:
        raise TypeError("Oops! The specified thread call back is not threadable.")
    __thread_args = CompiledObject.args
    __thread = threading.Thread(target=CompiledObject.callback, args=__thread_args, daemon=True)
    return __thread

def StartThread(ThreadObject: threading.Thread):
    ThreadObject.start()
    RunningThreads.append(ThreadObject)
    __ThreadingExit.update({ThreadObject.name: False})

@typing.final
def CheckForExit(ThreadObject: str) -> bool:
    '''
    CheckForExit is decorated by ```@typing.final``` \n
    This will check if the current thread need to be exited, please loop through this function, if needed.
    \n One example may be:

    ```
    while not ThreadManager.CheckForExit("myThread"):
        print("Hello world!")
    print("Ending Thread...")
    ```
    Please be aware that this function will raise a ThreadError if the thread referencing does not
    exist. 
    '''
    if __ThreadingExit.get(ThreadObject, -1) != -1:
        return __ThreadingExit.get(ThreadObject, -1)
    else:
        raise threading.ThreadError("The thread you are referencing does not exist")