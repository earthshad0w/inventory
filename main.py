#This program will allow its user to list and edit the inventory for their guitar shop.
import csv
import sys

# Inventory csv file
FILENAME = "inventory.csv"

# Defining a function terminate the program
def quit_program():
    print("Quitting...")
    sys.exit()

# Defining a class for each item in inventory
class Item:
    def __init__(self, id, manufacturer, model, price, qty):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.qty = qty

# Defining a function to read the inventory csv file
def read_items():
    # if csv file exists, open file for reading
    try:
        items = []
        # Read from file and create reader object from csv module
        with open("inventory.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 5:
                    continue

                id = row[0]
                manufacturer = row[1]
                model = row[2]
                price = row[3]
                qty = row[4]

                # create Item object using id, manufacturer, model, price, qty and append to items
                items.append(Item(id, manufacturer, model, price, qty))
            return items

    except FileNotFoundError:
        print(f"Could not find {FILENAME} file.")
        quit_program()


    # reader = csv reader object

    # for each row in reader
    #     if length of elements in row < 5
    #         continue

        # from the first element at index 0 in row
        

#     return items
# else:
#     return empty items list



# Defining a function to list inventory
def list_items(items):

    # Print a table of the inventory for pretty formatting
    print("Inventory")
    print(
        "Item I.D.".ljust(10) + "  " +
        "Manufacturer".ljust(20) +
        "Model".ljust(20) +
        "Price".ljust(15) +
        "Quantity".ljust(10)
    )
    print("-" * 75)

    # Printing item per line
    for item in items:
        print(
            item.id.ljust(10) +
            item.manufacturer.ljust(20) +
            item.model.ljust(20) +
            item.price.ljust(15) +
            item.qty.ljust(10)
        )
    print()



# Defining a function to display the menu
def display_menu():
    print()
    print("CHOOSE FROM THE FOLLOWING SELECTION")
    print("-" * 60)
    print("list - List items")
    print("add -  Add an item")
    print("del -  Delete an item")
    print("exit - Exit program")

# Defining main function
def main():

    items = read_items()

    ###### MAIN PROGRAM ######
    print("Inventory Program")

    # Using a while loop for menu selection
    while True:
        display_menu()
        command = input("Command: ")

        if command == "list":
            list_items(items)
        # elif command == add:
        #     add_item(items)
        # elif command == del:
        #     del_item(items)
        elif command == exit:
            quit_program()
        else:
            print("Invalid command.")

# Program entry
if __name__ == "__main__":
    main()