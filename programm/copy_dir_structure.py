#this programm copies the directry structure, checking if it doesnt exist already 
import os
import sys 
import filecmp 
import subprocess
from subprocess import Popen, PIPE
from subprocess import call #to system call MD5DEEP
import shutil #library for copying recursively
import errno #error catching source is not a dir
import logging #lib for log file
import difflib #to compare the stored hashes

#creating the log file
LOG_FILE = '/Users/yuliasukonkina/Desktop/training/logs/copydir.log'
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG) 

#saving all STD messages to a log file
sys.stdout = open (LOG_FILE, 'a+') 
sys.stderr = open (LOG_FILE, 'a+')

#defining the source and destination diretories
From ='/Users/yuliasukonkina/Desktop/training/source/'
To = '/Users/yuliasukonkina/Desktop/training/target/'

#tracking the status of the copying with shutil.copytree
def _logpath(path, names):
    logging.info('Working in %s' % path)
    return []   # nothing will be ignored


#function to copy dir/subdir recursively
def copy(src, dest, log):
    try:
        print("using COPYTREE")
        shutil.copytree(src, dest, ignore=_logpath)
        shutil.copystat(src, dest)#preserving the timestamps
        print("O-O-O-P-S")

    except OSError as e:
        # If the error was caused because the source directory/folder was actually a file, then we copy the file instead

        print("e.errno = %s" % e.errno)
        if e.errno == errno.ENOTDIR:
            print("THIS ---->", From, "----IS NOT A DIRECTORY")
            """
            if not os.path.exists(direct):  
                os.makedirs(direct)
                shutil.copy(src, dest)
            else: 
                shutil.copy(src, dest)
                print("using copy2")"""
        else:
            print('Directory not copied. Error: %s' % e)
            log.error("Exception occurred", exc_info=True)


#if directory exists do RSYNC to check if copy is true
def ensure_dir(file_path, log):
    directory = os.path.dirname(file_path)
    print(directory, "LOOKING FOR THE DIRECTORY")
    if  not os.path.exists(directory):
        copy(From, To, logging)
        
    else:
        cmd = ["rsync", "-avzh", '-P', From, To]
        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        for line in iter(p.stdout.readline, b''):
            print('>>> {}'.format(line.rstrip()))
        print(cmd)
        call(cmd)

print("++++++++++++++++++++++Insure the dir is not there, else RSYNC")
ensure_dir(To, logging)
print("----------------------Finished copying")


def sortfile(fname):
  f = open(fname)
  s = []
  for i in f:
    s.append(i.split()[0]+'\n')#linebreak works in Python 2, but not in Python 3
  s = sorted(s)
  f.close()
  f = open(fname, 'w+')
  for i in s:
    f.write(i)
  f.close()

print("----------------------Comparing the two directories/subdir function")
dc = filecmp.dircmp(From, To)
dc.report_full_closure()

source = '/Users/yuliasukonkina/Desktop/training/logs/sourcehash.txt'
target = '/Users/yuliasukonkina/Desktop/training/logs/targethash.txt'

print("----------------------Calculating hashes of SOURCE")
MD5DEEP = ["md5deep", "-j16", "-r", From]
sp = subprocess.Popen(MD5DEEP, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = sp.communicate()
if out:
        print ("standard output of subprocess:")
        print (out)
        f = open(source,'w')
        f.write(out.decode("utf-8"))
        f.close()
if err:
        print ("standard error of subprocess:")
        print (err)
print ("returncode of subprocess:")
print (sp.returncode)

print("----------------------Calculating hashes of TARGET")
MD5DEEP1 = ["md5deep", "-j16", "-r", To]
sp = subprocess.Popen(MD5DEEP1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = sp.communicate()  #in python2:  commands.getoutput(MD5DEEP)
if out:
        print ("standard output of subprocess:")
        print (out)
        f = open(target,'w')
        f.write(out.decode("utf-8"))
        f.close()
if err:
        print ("standard error of subprocess:")
        print (err)
print ("returncode of subprocess:")
print (sp.returncode)
print("----------------------MD5DEEP finished its work")


print("----------------------Sorting created SOURCE HASH & TARGET HASH FILES, removing the hash-paths")
sortfile(source)
sortfile(target)

print("----------------------COMPARING SOURCE HASH to TARGET HASH FILES")
compare=filecmp.cmp(source, target)
print('Compare = %s' % compare)
#compare = bool(compare)  -------- compare is already a boolean type
if not compare:
  call(['diff', source, target])
else:
    print('Compare = %s' % compare)
print("----------------------TheEnd")


#direct = os.path.dirname(To)
#    result = commands.getoutput(MD5DEEP) #this is the ONLY possibility to write STDOUT into a log file
 #   print(result)
  #  result1 = commands.getoutput(MD5DEEP1)
   # print(result1)
"""
try:
    MD5DEEP = ["md5deep", "-j16", "-r", "From"]
    with open("source","w") as out, open("LOG_FILE","a") as err:
        subprocess.Popen(MD5DEEP,stdout=out,stderr=err)
    
    MD5DEEP1 = ["md5deep", "-j16", "-r ", "To"]
    with  open(target,"w") as out1, open(LOG_FILE,"a") as err1:
        subprocess.Popen(MD5DEEP1,stdout=out1,stderr=err1)
        print("what's wrong")

except IOError as e:
    logging.error("Exception occurred", exc_info=True)

MD5DEEP = ("md5deep -j16 -r /Users/yuliasukonkina/Desktop/training/target/ > /Users/yuliasukonkina/Desktop/training/logs/targethash.txt")
MD5DEEP1 = ("md5deep -j16 -r /Users/yuliasukonkina/Desktop/training/source/ > /Users/yuliasukonkina/Desktop/training/logs/sourcehash.txt")
os.system(MD5DEEP)
os.system(MD5DEEP1)
#output = subprocess.check_output(["md5deep", "-j16", "-r", "/Users/yuliasukonkina/Desktop/training/target/"])
#print(output)
#output1 = subprocess.check_output(["md5deep", "-j16", "-r", "/Users/yuliasukonkina/Desktop/training/source/"])
#print(output1)"""

#Try to get output to the log in python 3:

#message = u"Stdoutmessage"
#logger = logging.getLogger()
#console_handler = logging.StreamHandler(sys.stdout)
#file_handler = logging.FileHandler(LOG_FILE)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#console_handler.setFormatter(formatter)
#file_handler.setFormatter(formatter)
#logger.addHandler(console_handler)
#logger.addHandler(file_handler)
#logger.setLevel(logging.DEBUG)
#logger.debug(message)
#print ("something")