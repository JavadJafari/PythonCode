items = []

def add_item():
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    price = input("Enter item price: ")
    count = input("Enter item count: ")

    with open("text.txt" , "a") as file:
        file.write(f"{item_id},{name},{price},{count}\n")

    print("Your Item added successfully.")

def search_item():
    search_id = input("Enter item ID to search: ")

    with open("text.txt" , "r") as file:
        for l in file:
            product = l.strip().split(",")
            if product[0] == search_id:
                print("Item found:")
                print("ID:", product[0])
                print("Name:", product[1])
                print("Price:", product[2])
                print("count:", product[3])
                return

    print("Your Item not found.")

def edit_item():
    edit_id = input("Enter your item ID to edit: ")
    new_items = []

    with open("text.txt" , "r") as file:
        for l in file:
            product = l.strip().split(",")
            if product[0] == edit_id:
                name = input("Enter new name: ")
                price = (input("Enter new price: "))
                count = (input("Enter new count: "))
                product = [product[0], name, price, count]
                print("Your products edited successfully.")
                new_items.append(product)
        else:

            print("Your Item not found.")

    with open("text.txt" , "w") as file:
        for item in new_items:
            file.write(",".join(str(i) for i in item) + "\n")
        

def delete_item():
    delete_id = input("Enter item ID to delete: ")
    deleted = False

    with open("text.txt" , "r") as file:
        lines = file.readlines()

    with open("text.txt" , "w") as file:
        for line in lines:
            item = line.strip().split(",")
            if item[0] != delete_id:
                file.write("\n" + line)
            else:
                deleted = True

    if deleted:
        print("Item deleted successfully.")
    else:
        print("Item not found.")
def buy_item():
    cart=[]
    while True:
        barcode = input("enter required barcode or exit")
        if barcode == "exit":
            break

        found = False
        for list in list:
            if int(barcode) == list["barcode"]:
                found = True
                quantity = int(input("enter quantity: "))

                if quantity > list["count"]:
                    print("not enough products")
                    break
                else:
                   list["count"] = list["count"] - quantity
            item = {
                        "barcode": list["barcode"],
                        "name":list["name"],
                        "price": list["price"],
                        "count": quantity
                    }
        cart.append(item)
        break

    if not found:
        print(f"barcode{barcode} not found.")

    print("your list")
    for item in cart:
        print(f"\t price per product{item['name']}: {item['price']} Toman / {item['count']} of {item['name']} (ID: {item['barcode']}) \t your total is: {item['count'] * item['price']}")
    total_cost = 0
    for item in cart:
            total_cost = total_cost + (int(item["count"]) * int(item["price"]))
    print(f"your total is {total_cost}")


def show_items():
    items.clear()
    with open("text.txt" , "r") as file:
        for line in file:
            product = line.split(",")
            dic = {"ID:": product[0], "Name:": product[1], "Price:": product[2], "Quantity:": product[3]}
            items.append(dic)
    print("Items in storage:")
    for obj in items:
        print(obj)

def exit_app():
    print("Exiting the app...")
    exit()

# Main loop
while True:
    print("Menu:")
    print("1. Add item")
    print("2. Search item")
    print("3. Edit item")
    print("4. Delete item")
    print("5. buy item")
    print("6. Show items")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        search_item()
    elif choice == '3':
        edit_item()
    elif choice == '4':
        delete_item()
    elif choice==5:
        buy_item()
    elif choice == '6':
        show_items()
    elif choice == '7':
        exit_app()
    else:
        print("Invalid choice. Please try again.")