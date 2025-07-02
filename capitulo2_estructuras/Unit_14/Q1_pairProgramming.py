items = {"Coffee": 7, "Pen": 3, "Paper cup": 2, "Milk": 1, "Coke": 4, "Book": 5}
menu_option = -1

while menu_option != 4:
    menu_option = int(input("""Select menu:
1) check stock
2) warehousing 
3) release 
4) exit 
Enter: """))
    print()

    if menu_option == 1:
        stock_item = input("Enter item: ").lower().capitalize()
        if stock_item == "Papercup":
            stock_item = "Paper cup"
        print("Stock:", items.get(stock_item, "Item not found"))

    elif menu_option == 2:  # Add item or quantity
        request = input("Enter item and quantity: ").strip().split()
        if len(request) == 3: #El item seleccionado es paper cup, que tiene un espacio
            stock_item = ' '.join([request[0], request[1]])
            stock_item_quantity = request[2]
        else:
            stock_item = request[0]
            stock_item_quantity = request[1]
        stock_item = stock_item.strip().lower().capitalize()
        stock_item_quantity = int(stock_item_quantity)
        items[stock_item] = items.pop(stock_item, 0) + stock_item_quantity
        print(items)

    elif menu_option == 3:  # Release item
        request = input("Enter item and quantity: ").strip().split()
        if len(request) == 3: #El item seleccionado es paper cup, que tiene un espacio
            stock_item = ' '.join([request[0], request[1]])
            stock_item_quantity = request[2]
        else:
            stock_item = request[0]
            stock_item_quantity = request[1]
        stock_item = stock_item.strip().lower().capitalize()
        stock_item_quantity = int(stock_item_quantity)
        if stock_item not in items:
            print("Item not found")
        else:
            real_quantity = items[stock_item]
            if real_quantity < stock_item_quantity:
                print("No tenemos tantos de", stock_item, "- no se puede salir")
            else:
                items[stock_item] -= stock_item_quantity
        print(items)
    print()
print("Program Exited")
