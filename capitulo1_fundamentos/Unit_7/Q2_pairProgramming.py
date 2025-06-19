x,y= input("Enter x,y coordinates: ").split()
x,y = int(x),int(y)

if x>=0 and y>=0:
    print("You are in the first quadrant")
elif x<0 and y >= 0:
     print("You are in the second quadrant")
elif  x<0 and y<0:
    print("You are in the third quadrant")
else: 
    print("You are in the fourth quadrant")

