#this programm copies the directry structure, checking if it doesnt exist already 
import shutil #library for copying recursively
import errno #error catching source is no a dir
import logging #lib for log file
import filecmp 
import difflib #to compare the stored hashes
import sys 
import os
from filecmp import dircmp
from subprocess import call
from hashdeep import hashdeep #importing the hashdeep function

#creating the log file
logging.basicConfig(filename='/Users/yuliasukonkina/Desktop/training/logs/copydir.log',level=logging.DEBUG) 

From ='/Users/yuliasukonkina/Desktop/training/source/'
To = '/Users/yuliasukonkina/Desktop/training/target/'

#function to copy dir/subdir recursively
def copy(src, dest, log):
    try:
        print("using copytree")
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source directory/folder was actually a file, then we copy the file instead
        if e.errno == errno.ENOTDIR:
            shutil.copy2(src, dest)
            print("using copy2")
        else:
       #     print('Directory not copied. Error: %s' % e)
            log.error("Exception occurred", exc_info=True)


#if directory exists do RSYNC to check if copy is true
def ensure_dir(file_path, log):
    directory = os.path.dirname(file_path)
    print(directory, "...................")
    if  not os.path.exists(directory):
        copy(From, To, logging)
    else:
        print("rsync", "-avzh", "From, To")
        command = ["rsync", "-avzh", From, To]
#        try:
        print(command)
        call(command)
#        except Exception:
   #         print("EXCEPTION")
#            log.error("no such command", Exception.message._str_)   



 
 
#insure the dir is not there, else RSYNC
ensure_dir(To, logging)

print("finished copying")

source = '/Users/yuliasukonkina/Desktop/training/logs/sourcehash.txt'
target = '/Users/yuliasukonkina/Desktop/training/logs/targethash.txt'

#calculating hashes of source and destination
hashdeep(From, source, logging)
hashdeep(To, target, logging)

#comparing source hash to target hash files
compare=filecmp.cmp(source, target)
print('Compare = %s' % compare)
#compare = bool(compare)  -------- compare is already a boolean type
if not compare:
  call(['diff', source, target])
else:
    print('Compare = %s' % compare)


#comparing the two directories/subdir function
def print_diff_files(dcmp):
     for name in dcmp.diff_files:
         print("different file %s found in %s and %s" % (name, dcmp.left, dcmp.right))
            
     for sub_dcmp in dcmp.subdirs.values():
         print_diff_files(sub_dcmp)
dcmp = dircmp(From, To) 
print_diff_files(dcmp) 

"""
with open(source, 'r') as hosts0:
    num = sum(1 for line in hosts0)
    with open(target, 'r') as hosts1:        
        diff = difflib.unified_diff(
            hosts0.readlines(),
            hosts1.readlines(),
            fromfile=source,
            tofile=target, n=num
        )
        for line in diff:
            sys.stdout.write(line)

"""
