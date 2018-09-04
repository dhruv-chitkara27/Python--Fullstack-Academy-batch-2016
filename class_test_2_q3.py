"""

WAP that accepts a sequence of wide space separated words and print the words after removing all duplicates words and sorting them alphanumerically
 
SAMPLE INPUT :

hello world practice makes perfect and hello world again
 
SAMPLE OUTPUT :

again and hello makes perfect practice world
 
"""

seq = input("Enter the string(with space) : ").split(' ')

seq = list(set(seq))
seq.sort()
print(seq[0],end='')
for i in range(len(seq)):
    print(f' {seq[i]}',end='')





