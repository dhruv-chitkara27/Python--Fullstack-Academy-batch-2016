w1=0
d1=0
deposit=0
withdraw=0
balance=0
entries = int(input("Enter the no. of transactions you want to do : "))
for i in range(entries):
    choice = input("Enter b for balance, d for deposit , w for withdrawl")
    if(choice=='d'):
        deposit = input("Enter the amount of cash you want to deposit : ")
        d1=d1+int(deposit)
    if(choice=='w'):
        withdraw = input("Enter the amount of cash you want to withdraw : ")
        w1=w1+int(withdraw)
    if(choice=='b'):
        balance = d1-w1
        print("Balance = ",balance)
