#WAP TO CHECK FOR ODD NUMBERS VALUE GIVEN IN A STRING.IF MORE THAN TWO VALUES THEN SEPARATE BY COMMA.

a = input("Enter the string : ")
for i in range(a):
    if(a[i]%2!=0):
        print(a[i])
