import threading
from SDK.PackImplementations.IOPack import SysIO_IMPL as SysIO
from Pack.SysIO import VMObject
from SDK.PackImplementations.CompilerPack import ExecutableClass as executable

RunningThreads: list[threading.Thread] = []

def SpawnThread(CompiledObject: VMObject | executable) -> None:
    if not CompiledObject.__threadable__:
        raise TypeError("Oops! The specified thread call back is not threadable.")
    __thread_args = (CompiledObject.args, CompiledObject.Arguments)[len(CompiledObject.Arguments) > 0]
    __thread = threading.Thread(target=CompiledObject.callback, args=__thread_args, name=CompiledObject.LocationInBuffer, daemon=True)
    __thread.start()
    __thread.join()
    RunningThreads.append(__thread)