#Present David's Shop
print("#"*50)
print('This is David’s fruit shop.')
print('1: Apple( price : 5000 won)')
print('2: Grape( price : 6000 won)')
print('3: Melon( price : 8000 won)')
print('4: Orange( price: 2000 won)')
print("#"*50)

#Get input from the client
item_num = int(input("Enter item number (between 1-4) >> "))
num_items = int(input("Enter item number (between 1-4) >> "))

#Fijar precios y fruta
if item_num==1:
    price = 5000
    fruit = "Apple"
elif item_num==2:
    price = 6000
    fruit = "Grape"
elif item_num==3:
    price = 8000
    fruit = "Melon"
elif item_num==4:
    price = 2000
    fruit = "Orange"
else:
    print("The item selected is not in the list")

#Calculo precios
total_price = price*num_items  
print("Fruit selected:",fruit)
print("Price:",price)
print("Quantity:",num_items)
print("Total price is",total_price,"won")

#Insertar dinero
inserted_money = int(input("Insert money please(ex: 15000) >>> "))
change = inserted_money-total_price
if change >= 0:
    print(inserted_money,"won received.Your change is", change,"won")
else:
    print("You don't have enough money to buy",fruit+"s")
