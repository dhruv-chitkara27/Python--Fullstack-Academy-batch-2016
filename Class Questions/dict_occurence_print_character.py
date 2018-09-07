dict1 = { }
str = input("Enter the string")
for i in str:
    dict1[i]=str.count(i)
print(dict1)
for key,val in dict1.items():
    print(key,'*' *val)
