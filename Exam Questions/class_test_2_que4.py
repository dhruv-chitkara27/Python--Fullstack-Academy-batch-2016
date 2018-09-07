"""

Write a program which will find all such numbers between 1000 and 3000 both included such that each digit of a number is a even number

"""

print('Required Output : ',end='')
for i in range(2000,3001,2):
    if((i >= 2010 and i < 2020) or (i >= 2030 and i < 2040) or (i >= 2050 and i < 2060)):
        pass
    elif((i >= 2070 and i < 2080) or (i >= 2090 and i < 3000)):
        pass
    else:
        print(f'{i}',end=' ')

  
