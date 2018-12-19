#filecmp_cmpfiles.py
import filecmp
import os

# Determine the items that exist in both directories
d1_contents = set(os.listdir('/Users/yuliasukonkina/Desktop/training/source'))
d2_contents = set(os.listdir('/Users/yuliasukonkina/Desktop/training/target'))
common = list(d1_contents & d2_contents)
common_files = [f for f in common if os.path.isfile(os.path.join('/Users/yuliasukonkina/Desktop/training/source', f))]
print('Common files:', common_files)

# Compare the directories
match, mismatch, errors = filecmp.cmpfiles('/Users/yuliasukonkina/Desktop/training/source', '/Users/yuliasukonkina/Desktop/training/target', common_files)
print('Match       :', match)
print('Mismatch    :', mismatch)
print('Errors      :', errors)

"""

#this pgm compares recursively dirs and subdirs and prints the files that differ

import os
import filecmp 
import filecmp 
from filecmp import dircmp
def print_diff_files(dcmp):
    
    print("start print_diff_files")
    print(dcmp.diff_files)
    for name in dcmp.diff_files:
         try:
          print("different file %s found in %s and %s" % (name, dcmp.left_only, dcmp.right_only))
         except Exception:
          print("EXCEPTION")
    print("subdir compare")       
    for sub_dcmp in dcmp.subdirs.values():
         print_diff_files(sub_dcmp)

dir1 = '/Users/yuliasukonkina/Desktop/training/source'
dir2 = '/Users/yuliasukonkina/Desktop/training/target'

print("anything")

filecmp.cmpfiles(dir1, dir2, common, shallow=True)¶

dcmp = dircmp(dir1, dir2) 
dcmp.report_full_closure()
print("printing diff files")

print_diff_files(dcmp) 
print("end")
"""