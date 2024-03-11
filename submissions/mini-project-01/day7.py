list = []
choice = None
running = True

while(running):
    print("\n")
    print("Options")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Quit")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        item = input("Enter the item you want to add: ")
        item_added = list.append(item)
        print(f"{item_added} has been added to your shopping list")
    
    elif choice == 2:
        i = 0 
        print("Your Shopping List:\n")
        for i in list:
            
            print(i)
    elif choice == 3:
        if not list:
            print("Shopping list is empty")
        else:
            remove_item = int(input("Enter the item you want to remove:"))
            if 1 <= remove_item <= len(list):
                removed_item = list.pop(remove_item - 1)
                print(f"{removed_item} has been added to your shopping list")
            else:
                print("Invalid item number. Try again.")

    elif choice == 4:
        running = False
        
print("\nThank you! Goodbye.")



