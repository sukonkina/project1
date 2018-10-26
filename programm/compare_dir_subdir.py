#this pgm compares recursively dirs and subdirs and prints the files that differ
import os

def ls(path):
    all = []
    walked = os.walk(path)
    for base, sub_f, files in walked:           
        for sub in sub_f:           
            entry = os.path.join(base,sub)
            entry = entry[len(path):].strip("\\")
            all.append(entry)

        for file in files:          
            entry = os.path.join(base,file)
            entry = entry[len(path):].strip("\\")
            all.append(entry)
    all.sort()
    return all

def folder_diff(folder1_path, folder2_path):
    folder1_list = ls(folder1_path)
    folder2_list = ls(folder2_path)
    diff = [item for item in folder1_list if item not in folder2_list]
    diff.extend([item for item in folder2_list if item not in folder1_list])
    return diff

folder_diff("/Users/yuliasukonkina/Desktop/training/source", "/Users/yuliasukonkina/Desktop/training/target")
print(return diff)
"""
import os

def fileIsSame(right, left, path):
    return os.path.exists (os.path.join(left, path.replace(right, '')))

def compare(right, left):
    difference = list()
    for root, dirs, files in os.walk(right):
        for name in files:
            path = os.path.join(root, name)
            # check if file is same
            if fileIsSame(right, left, path):
                if os.path.isdir(path):
                    # recursively check subdirs
                    difference.extend(compare(path, left))
            else:
                # count file as difference
                difference.append(path)

    return difference
    print (compare(r'/Users/yuliasukonkina/Desktop/training/source', r'/Users/yuliasukonkina/Desktop/training/target'))
"""