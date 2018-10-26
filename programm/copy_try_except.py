#this pgm copies a file handling the exceptions "no such command" or build in exceptions

import subprocess 
import sys

command = ['cp', '/Users/yuliasukonkina/Desktop/training/source/test.hdf5', '/Users/yuliasukonkina/Desktop/training/target/test_copy2.hdf5']

try:
 subprocess.call(command)
except Exception:
 print ("no such command", Exception.message._str_)
