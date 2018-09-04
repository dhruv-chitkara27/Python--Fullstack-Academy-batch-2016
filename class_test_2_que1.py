"""
Write a program which takes two digits x and y as input and generates a 2d array. The element value in the ith row and jth column should be i*(j-1).
 
 SAMPLE INPUT :
 3,5
 
 SAMPLE OUTPUT :
 [ [],[],[] ]
 
"""
 
num = input('Enter x and y(with comma) : ').split(',')
i = int(num[0])
j = int(num[1])
main_list = []
sub_list = []

for a in range(1,i+1):
    for b in range(1,j+1):
        value = a*(b-1)
        sub_list.append(value)
    main_list.append(sub_list)
    sub_list = []

print(f'Required Output : {main_list}')
