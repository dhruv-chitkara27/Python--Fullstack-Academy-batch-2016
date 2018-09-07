x = input("Enter the string=")
y=len(x)
count1=0
count2=0
count3=0
for i in range(y):
    if(x[i]>='a' and x[i]<='z'):
        count1=count1+1
    if(x[i]>='A' and x[i]<='Z'):
        count2=count2+1
    if(x[i]>='0' and x[i]<='9'):
        count3=count3+1
print("small",count1)
print("large",count2)
print("digit",count3)
print("alpha",count1+count2)
