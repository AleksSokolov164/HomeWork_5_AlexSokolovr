
from functions_Console_file_manager import *


def f (x):
    return x*2

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print (new_list)

A = list(map(f, new_list))  # Вернет [2, 4, 6, 8]
print(A)

print( list(map(f, [5,4]) ))