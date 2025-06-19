fact=1
num=int(input("Dame un numero :"))
inverso = 1
for i in range(1,num+1):
    fact*=i
print("El factorial de",num,"es",fact)

for j in range(num,0,-1):
    inverso*=j
print("El factorial de",num,"es",inverso)
