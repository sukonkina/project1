
f1 = open('targethash.txt')
f2 = open('sourcehash.txt')

for i,j in zip(f1,f2):
  if i!=j: print(i,j)
