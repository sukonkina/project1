#this pgm compares two files, and if FALSE uses system call for 'diff' to show where is the difference

from subprocess import call
import filecmp


compare=filecmp.cmp('/Users/yuliasukonkina/Desktop/training/logs/example.log', '/Users/yuliasukonkina/Desktop/training/logs/example1.log')
print(compare)

compare = bool(compare)
if not compare:
  call(['diff', '/Users/yuliasukonkina/Desktop/training/logs/example.log', '/Users/yuliasukonkina/Desktop/training/logs/example1.log'])


###for f1, f2 in zip(file_list_1, file_list_2): # takes first, second, etc files corresponding to each list 
#    output = subprocess.check_output(['diff', f1, f2]) # generate diff of both file
#    with open('diff-{}-{}'.format(f1, f2), 'w+') as f:
#        f.write(output)  # write the diff to third file
###
