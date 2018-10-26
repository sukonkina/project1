#this pgm creates a newfile.txt (w+) with 10 numbered lines   //running twice overwrites the file

f= open("/Users/yuliasukonkina/Desktop/training/source/directory1/subdirectory/newfile.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close() 
