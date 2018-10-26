import os
import stat
import os.path, time

my_file = "/Users/yuliasukonkina/Desktop/training/source/a.txt"

#printing the time created and last modified
print("last modified: %s" % time.ctime(os.path.getmtime(my_file)))
print("created: %s" % time.ctime(os.path.getctime(my_file)))

#checking permissions for user, group and others
st = os.stat(my_file)
oct_perm = oct(st.st_mode)
print(oct_perm)
"""
def isgroupreadable(my_file):
  st = os.stat(my_file)
  return bool(st.st_mode & stat.S_IRGRP)
"""
#checking permissions for logged in user
read=os.access(my_file, os.R_OK) # Check for read access
print ('Read access = %s' % read)
write=os.access(my_file, os.W_OK) # Check for write access
print ('Write access = %s' % write)
exe=os.access(my_file, os.X_OK) # Check for execution access
print ('Execute access = %s' % exe)
exist=os.access(my_file, os.F_OK) # Check for existance of file
print ('Existance = %s' % exist)
