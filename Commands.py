import SDK.PackImplementations.CompilerPack as Compiler
import SDK.PackImplementations.VMMethods as VMMethods
import pathlib, os, Buffers, sys, random, time, PublicVariables as pv

Set_log: list = []

Executables: dict[str: tuple] = {}
lyrics: list[str] = ["Run freedom run", 'freedom run away', 'my friends you have to run runa runa run', 
                     'freedom run away!', 'that freedom sun', 'will shine someday',
                     'till then you better run', 'runa runa run', 'Freedom run away!', 'There\'s a trickle of sweat', 
                     'Drippin\' in your ear', 'But still, you gotta run', 'runa, runa, run', 'Freedom run away!', 'So now, don\'t you fret',
                     'And never fear!', 'Till freedom\'s', 'Won, wona, wona, won', 'Freedom run away!', 
                     'https://youtu.be/ncQ1dvcHEn8?si=aTHG_9_qysRHWwoz']

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
            print(f"\ncompile: Successfully compiled {args[:1][0]}")
            Executables.update({args[:1][0][0:-4]: (r[2], r[3])})
            with open(pathlib.Path(f"SystemPack/Executables.vmp").absolute(), "a") as f:
                f.write(args[:1][0] + '\n')
        else:
            raise FileNotFoundError("compile: No target file found, stop")
        
        

def do(*args) -> None:
    with open(pathlib.Path("SystemPack/Executables.vmp").absolute(), 'r') as f:
        valid_contents = f.readlines()
    if args[0]+".vma\n" in valid_contents:
        contents: Compiler.ExecutableClass = Buffers.BufferMethods.RetrieveContents(Executables[args[0]])
        contents.Call()
    else:
        raise FileNotFoundError("do: Cannot find the compiled object")
    
def exit(*args) -> None:
    if len(args) != 0:
        sys.exit(int(args[0]))
    else:
        sys.exit(0)

def ClearBuffer(*args):
    with open(pathlib.Path("SystemPack/Executables.vmp").absolute(), 'a+') as f:
        f.truncate(0)
    print("ClearBuffer: Done")

def echo(*args):
    print(*args)

def debug(*args):
    VMMethods.DebugMode()

def run(*args):
    if args[0] == "freedom" and random.randint(1, 4) == 1:
        for x in lyrics:
            time.sleep(0.5)
            print(x,'\n')
        raise ValueError("Urinetown is less of a place but a metaphysical place.")
    else:
        do(*args)


def snap(*args):
    import py_compile
    for x in list(Executables.keys()):
        contents: Compiler.ExecutableClass = Buffers.BufferMethods.RetrieveContents(Executables[x])
        with open(f"Snap/temp.py", 'w+') as f:
            f.write("import sys\nsys.path.append('../VM_ASM')\nfrom SDK.PackImplementations.VMMethods import *\n")
            for i in range(0, len(contents.__code__()[0])):
                c = f"{contents.__code__()[0][i].__name__}('{contents.__code__()[1][i][0]}', '{contents.__code__()[1][i][1]}')\n"
                f.write(c)
        py_compile.compile(file="Snap/temp.py", cfile=f"Snap/Snap{list(Executables.keys()).index(x)}.pyc")

def clear(*args):
    if len(args) > 0:
        try:
            int(args[0])
        except Exception:
            raise 
        for x in range(args[0]):
            print('\n')
        print('\033[%d;%dH' % (0, 0))
    else:
        for x in range(os.get_terminal_size().lines):
            print('\n')
        print('\033[%d;%dH' % (0, 0))

def set(*args):
    t_f: dict = {'true': True, 'false':False}
    if args[0] == 'consolidate':
        with open("SystemPack/operation_on_boot.vmp", 'a+') as f:
            for x in Set_log:
                f.write(x)
                f.write('\n')
    if len(args) <= 1:
        raise ValueError("the command 'set' must have at least 2 arguments")
    if args[0] in list(pv.CommandLineBehavior.keys()):
        if args[1] == 'true' or args[1] == 'false':
            pv.CommandLineBehavior.update({args[0]: t_f[args[1]]})
        else:
            pv.CommandLineBehavior.update({args[0], args[1]})
        Set_log.append(f"set {args[0]} {args[1]}")
    else:
        raise ValueError(f"expected a CommandLineBehavior field, {args[0]} found")
    
def help(*args):
    print('Valid Commands: \n (1) compile \n (2) do \n (3) echo \n (4) debug \n (5) clear \n (6) snap \n (7) set')