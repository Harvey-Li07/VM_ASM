import VMInit
import Commands
import SDK.PackImplementations.VMMethods as vm

Commands.compile("sample.vma")
Commands.do("sample.vma")

vm.syscall("1", "ax")
vm.syscall('1', "cx")
