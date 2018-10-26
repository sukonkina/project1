#this pgm compares recursively dirs and subdirs and prints the files that differ

import os
import filecmp 
from filecmp import dircmp
def print_diff_files(dcmp):
     for name in dcmp.diff_files:
         try:
          print("different file %s found in %s and %s" % (name, dcmp.left, dcmp.right))
         except Exception:
          print("EXCEPTION")
            
     for sub_dcmp in dcmp.subdirs.values():
         print_diff_files(sub_dcmp)
dcmp = dircmp('/Users/yuliasukonkina/Desktop/training/source/directory1', '/Users/yuliasukonkina/Desktop/training/target/directory1') 
print_diff_files(dcmp) 
