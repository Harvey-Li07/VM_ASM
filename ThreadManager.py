import threading
from SDK.PackImplementations.IOPack import SysIO_IMPL as SysIO
from Pack.SysIO import VMObject
from SDK.PackImplementations.CompilerPack import ExecutableClass as executable

RunningThreads: list[threading.Thread] = []

def SpawnThread(CompiledObject: VMObject | executable) -> threading.Thread:
    if not CompiledObject.__threadable__:
        raise TypeError("Oops! The specified thread call back is not threadable.")
    __thread_args = CompiledObject.args
    __thread = threading.Thread(target=CompiledObject.callback, args=__thread_args, daemon=True)
    return __thread

def StartThread(ThreadObject: threading.Thread):
    ThreadObject.start()
    RunningThreads.append(ThreadObject)