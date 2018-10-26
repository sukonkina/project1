#this pgm calculates the hash for a file test.hdf5 and saves it in sample.txt, appesnding every new calculation

import hashlib
def file_as_bytes(file):
    with file:
        return file.read()

#calculating the hash in binary format 
result = hashlib.md5(file_as_bytes(open('/Users/yuliasukonkina/Desktop/training/source/test.hdf5', 'rb')))

#prints the result in hexadecimal format
print(result.hexdigest())

output = result.hexdigest()
file = open("/Users/yuliasukonkina/Desktop/training/source/sample.txt","a")
file.write(output)
file.write("\n")
file.close()

