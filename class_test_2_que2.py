"""
Write a program that accepts comma separated sequence of words as input and print the words in a comma separated sequence after sorting them in alphabatical order.
 
 SAMPLE INPUT :
 without , hello , bag , world
 
 SAMPLE OUTPUT :
 bag,hello,without,world
 
"""

seq = input("Enter the string : ").split(',')
seq.sort()
print(seq[0],end='')
for i in range(1,len(seq)):
    print(f',{seq[i]}',end='')



