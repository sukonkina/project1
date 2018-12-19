1. Copy_dir_structure is a Python script which makes a recursive copy of all files and directories in the destination folder to target folder. 
2. The destination directory, named TARGET, must not already exist; it will be created as well as missing parent. 
3. If the destination directory already exists, RSYNC function is used to check if the copy is true.
4. MD5DEEP is called as a subprocess to calculate the hashes of the files in SOURCE and TARGET.
5. The hash files are then sorted and hash-paths being removed.
6. SOURCEHASH.txt and TARGETHASH.txt hash files are compared, and TRUE or FALSE result is returened.
7. All info and error messages are recorded in a COPYDIR.log file. This file is appended with each run of a programm. 