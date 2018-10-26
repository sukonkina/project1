#this pgm compares two files (example.log, example1.log) and prints the lines which differ into compare_logs.txt
#the drawback of this pgm is that the number of lines differ it doesn't complete the comparison 

file1 = open ('/Users/yuliasukonkina/Desktop/training/logs/example.log', 'r')
file2 = open ('/Users/yuliasukonkina/Desktop/training/logs/example1.log', 'r')
FO = open ('/Users/yuliasukonkina/Desktop/training/target/compare_logs.txt', 'w')
"""
for line1 in file1:
    for line2 in file2:
       if line1 == line2:
            FO.write("%s\n" %(line1))
"""
#zip is looping over the two file at the same time, and if the lines are not the same then print the line from file1
for i,j in zip(file1,file2):
  if i!=j:FO.write('First file:' +str(i)+'Second File:'+str(j)+'\n')


FO.close()
file1.close()
file2.close()
