# Task :
#
# Given the list of n numbers contains positive and negative values.
# Write a program using modules :
#     - to find unique triples whose 3 elements gives the sum 0 from the given numbers
#     - form the given list find the possible 2 digit valid numbers
#     - find a random number which can be both positive and negative from the sepicified range entered by the user

import unique_triplets, valid_numbers, random_numbers

n = int(input('Enter the List Size : '))
my_list = []

for i in range(n):
    num = int(input('Enter Number : '))
    my_list.append(num)

print('Enter your choice : ')
print('1 for finding triplets with sum 0')
print('2 for finding 2 digit valid numbers')
print('3 for finding a random number')

choice = int(input('Enter your choice : '))

while(choice < 1 or choice > 3):
    print('Wrong Choice Entered...TRY AGAIN')
    choice = int(input('Enter your choice : '))

if(choice == 1):
    unique_triplets.triplets(my_list)
elif(choice == 2):
    valid_numbers.validate(my_list)
elif(choice == 3):
    random_numbers()
