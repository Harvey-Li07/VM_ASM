import sys
sys.path.append('../VM_ASM')
from SDK.PackImplementations.VMMethods import *
mov('ax', '1')
mov('bx', '2')
add('ax', 'bx')
mov('cx', '3')
sub('cx', '1')
syscall('3', 'ax')
syscall('3', 'cx')
