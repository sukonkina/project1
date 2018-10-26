#this pgm creates single directory1 using mkdir, defining access rights to it, 
# and drops an exception when dir already exists

#import the os module 
import os

#detect the current working directory and print it
dirpath = os.getcwdb()
print ("The current working directory is %s" % dirpath)

#define the name of the directory to be created
path = "/Users/yuliasukonkina/Desktop/training/source/directory1"

#define the access rights 777(r$w by all)

access_rights = 0o755

try: 
   os.mkdir(path, access_rights)
except OSError:
   print ("Creation of the directory %s failed" % path)
else:
   print ("Successfully created the directory %s " % path)
