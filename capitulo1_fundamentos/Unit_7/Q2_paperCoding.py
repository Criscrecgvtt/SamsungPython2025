int1,int2= input("Enter two integers: ").split()
int1, int2 = int(int1),int(int2)
if int1%int2 == 0:
    print(int1,"is a multiple of",int2)
else:
    print(int1,"is NOT a multiple of",int2)
   