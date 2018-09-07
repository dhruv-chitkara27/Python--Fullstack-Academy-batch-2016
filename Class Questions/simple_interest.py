def simple_interest(interest):
    p = int(input("Enter the principle amount"))
    t = int(input("Enter the time period"))
    sim_int = (p*interest*t)//100
    return sim_int
age = input("Enter the age of the person_____s for SENIOR y for young")
if(age == 's'):
    interest = 12
    si = simple_interest(interest)
    print("Simple Interest : ",si)
if(age == 'y'):
    interest = 10
    si = simple_interest(interest)
    print("Simple Interest : ",si)
