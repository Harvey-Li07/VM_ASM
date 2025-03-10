import SDK.PackImplementations.CompilerPack as Compiler
import pathlib, os, Buffers, sys

Executables: dict[str: tuple] = {}

def FilterFlags(*args) -> list[str]:
    flags: list[int] = []
    for x in args:
        if x[0] == "-":
            flags.append(args[args.index(x)][1:])
    return flags

def CompileFlags(flags: list[str]) -> dict[str: "str"]:
    CommonFlags: dict = {"s": "[silent]", "v": "[verbal]", "p": "..."}
    ...


def compile(*args) -> None:
    LocalCompiler: Compiler.Compiler = Compiler.Compiler() #generate a constructor
    flags = FilterFlags(args)
    try:
        args[:0]
    except IndexError:
        raise NameError("compile: No target file found, stop")
    else:
        if os.path.exists(pathlib.Path(f"Program/{args[:1][0]}").absolute()):
            filepath = pathlib.Path(f"Program/{args[:1][0]}").absolute()
            with open(filepath, 'r') as instruction_file:
                LocalCompiler.GetInstructions(instruction_file.read())
            LocalCompiler.CompileInstruction()
            r = LocalCompiler.SpawnExecutable()
        else:
            raise FileNotFoundError("compile: No target file found, stop")
        with open(pathlib.Path(f"SystemPack/Executables.vmp").absolute(), "a") as f:
            f.write(args[:1][0] + '\n')
        print(f"\ncompile: Successfully compiled {args[:1][0]}")
        Executables.update({args[:1][0][0:-4]: (r[2], r[3])})

def do(*args) -> None:
    with open(pathlib.Path("SystemPack/Executables.vmp").absolute(), 'r') as f:
        valid_contents = f.readlines()
    if args[0]+".vma\n" in valid_contents:
        contents: Compiler.ExecutableClass = Buffers.BufferMethods.RetrieveContents(Executables[args[0]])
        contents.Call()
    else:
        raise FileNotFoundError("do: Cannot find the compiled object")
    
def exit(*args) -> None:
    sys.exit()

def ClearBuffer(*args):
    with open(pathlib.Path("SystemPack/Executables.vmp").absolute(), 'a+') as f:
        f.truncate(0)
    print("ClearBuffer: Done")

def echo(*args):
    print(*args)