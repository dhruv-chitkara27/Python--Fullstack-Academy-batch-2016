a = int(input("Enter the first range : "))
b = int(input("Enter the second range : "))
if(a%2!=0):
    a=a+1
while(a!=b):
    if(a%2==0):
        flag=1
        c = str(a)
        for j in range(len(c)):
            if(int(c[j])%2==0):
                #print(c[j])
                flag=1
            else:
                flag=0
                break
    if(flag==1):
        print(a)
    a = a+2
    
