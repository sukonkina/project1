"""
This pgm builds recursive hashes of files in current directory tree in hashdeep format and saves them to example1.log

in VI operates correctly but here 
"""

import os
import os.path as osp
import hashlib

#logging.basicConfig(filename='/Users/yuliasukonkina/Desktop/training/logs/hash.log', level=logging.DEBUG)

# --- helpers ---

def write(text):
    """ helper for writing output, as a single point for replacement """
    logging.info(text)
    print(text)

def filehash(filepath):
    blocksize = 64*1024
    sha = hashlib.sha256()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() 

# --- /helpers ---

#write("""\
#%%%%%%%% HASHDEEP-1.0
#%%%%%%%% size, sha256, filename
##
## $ hashdeep.py
##""")

def hashdeep(ROOT, filename, logging):
    hashfile = open(filename, 'w+')
    for root, dirs, files in os.walk(ROOT):
     try:
      for fpath in [osp.join(root, f) for f in files]:
        size = osp.getsize(fpath)
        sha = filehash(fpath)
        name = osp.relpath(fpath, ROOT)
        hashfile.write('%s,%s,%s,%s' % (size, sha, name, '\n'))

     except OSError as e:
       logging.error("Exception occurred", exc_info=True)
        #for ignored in ['.hg', '.svn', 'git']:
        #     if ignored in dirs:
        #         dirs.remove(ignored)

    hashfile.close()

"""
Hashdeep format description:
http://md5deep.sourceforge.net/start-hashdeep.html
hashdeep.py differences from original hashdeep:
 - if called without arguments, automatically starts to build
   recursive hash starting from the current directory
   (original hashdeep waits for the output from stdin)
 - uses only sha256 (original uses md5 and sha256)
 - uses relative paths only (original works with absolute)
hashdeep.py output example:
$ hashdeep.py
%%%% HASHDEEP-1.0
%%%% size,sha256,filename
##
## $ hashdeep.py
## 
5584,28a9b958c3be22ef6bd569bb2f4ea451e6bdcd3b0565c676fbd3645850b4e670,dir/config.h
9236,e77137d635c4e9598d64bc2f3f564f36d895d9cfc5050ea6ca75beafb6e31ec2,dir/INSTALL
1609,343f3e1466662a92fa1804e2fc787e89474295f0ab086059e27ff86535dd1065,dir/README
"""
"""
__author__ = 'anatoly techtonik <techtonik@gmail.com>'
__license__ = 'Public Domain'
__version__ = '1.0'
"""
