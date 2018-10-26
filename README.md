# project1
copying files, counting hashes, creating logs

copy_dir_structure.py 

-creates a log file for the copying process (logging)
-copies the directories/files from source to target (copy)
-uses RSYNC to makes sure the target is the same as source (ensure_dir)
-calculates hashes for source and target (hashdeep)
-compares the hash files (compare)
-compares the source and target directories (print_diff_files)
