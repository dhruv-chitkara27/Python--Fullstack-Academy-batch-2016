"""

A robot moves in a plane starting from the origin point (0,0). The robot can move UP , DOWN , LEFT , RIGHT with a given steps. The trace of the robot movement is shown as: 
 			   UP 5 
 			   DOWN 3 
 			   LEFT 3 
 			   RIGHT 2  
 			   i->number

The number after the directions  are the steps. Write a program to compute the distance from the current position after a sequence of movement and the original point. If the distance is a float then print the nearest integer.

SAMPLE INPUT :
               UP 5
               DOWN 3
 	       LEFT 3
 	       RIGHT 2


SAMPLE OUTPUT :
               2  

"""

print("Enter the Coordinates")
for i in range (4):
    a=input("Enter the Movement: ").split()
    b=int(a[1])
         
    if (a[0]=='UP'):
        up=b
    if (a[0]=='DOWN'):
        down=b
    if (a[0]=='LEFT'):
        left=b
    if (a[0]=='RIGHT'):
        right=b

if (up>down):
    a=up-down
else:
    a=down-up
if  (left>right):
    b=left-right
else:
    b=right-left

distance= (a*a+b*b)**0.5
print(int(distance))
