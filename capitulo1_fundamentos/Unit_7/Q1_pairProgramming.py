print("1)Addition","\t","2) Substraction","\t","3) Multiplication","\t","4) Division")
op_num=int(input("Enter the desire number of operation : "))
op_types =[1,2,3,4]
if not(op_num in op_types):
    print("The operation selected is not valid")
else:
    a,b= input("Enter two numbers for the operation: ").split()
    a,b = int(a),int(b)
    #a = int(input())
    #b = int(input())
    print(a)
    print(b)
    if op_num == 1:
        print(a,"+",b,"=",a+b)
    elif op_num == 2:
        print(a,"-",b,"=",a-b)
    elif op_num == 3:
        print(a,"*",b,"=",a*b)
    else:
        print(a,"/",b,"=",a/b)