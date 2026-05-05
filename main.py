# Inventory Management Program
# Allows user to:
# - View inventory
# - Add new items or update existing ones
# - Remove quantity from items
# Data is stored in a CSV file and loaded into memory as Item objects
import csv
import sys

# Inventory csv file constant
FILENAME = "inventory.csv"

# Defining a class for each item in inventory
class Item:
    def __init__(self, id, manufacturer, model, price, qty):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.qty = qty

# Defining a function terminate the program
def quit_program():
    print("Quitting...")
    sys.exit()

# Defining a function to validate user input for the price for item
def get_valid_price():
    while True:
        try:
            price = float(input("Enter item price: "))
            if price < 0:
                print("Price must be non-negative")
            else:
                return price
        except ValueError:
            print( "Invalid input. Please enter a vaild price.")

# Defining a function to validate user input for the item quantity 
def get_valid_quantity():
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty < 0:
                print("Quantity must be non-negative")
            else:
                return qty

        except ValueError:
            print("Invalid input. Please enter a valid quantity.")



# Defining a function to read the inventory csv file
def read_items():
    # if csv file exists, open file for reading
    try:
        items = []
        # Read from file and create reader object from csv module
        with open(FILENAME, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader: 
                # Omit rows with any missing fields
                if len(row) < 5:
                    continue
                # Assign variables for each element per row
                id = row[0]
                manufacturer = row[1]
                model = row[2]
                price = float(row[3])
                qty = int(row[4])

                # Instantiate Item object using id, manufacturer, model, price, qty and append to items
                items.append(Item(id, manufacturer, model, price, qty))
            # Sort items alphabetically by manufacturer
            items.sort(key=lambda item: item.manufacturer)
            return items

    except FileNotFoundError:
        print(f"Could not find {FILENAME} file.")
        quit_program()
    except Exception as e:
        print(type(e), e)
        quit_program()

def write_items(items):
    # open file for writing
    try:
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            # Converting object into list and then writing row
            for item in items:
                row = [item.id, item.manufacturer, item.model, item.price, item.qty]
                writer.writerow(row)
    except Exception as e:
        print(type(e), e)
        quit_program()

# Defining a function to add items
def add_items(items):
    found = False
    item_id = input("Enter item ID: ").upper()
    # Check if item id is in inventory. Update quantity if True
    for item in items:
        if item.id == item_id:
            qty_to_add = get_valid_quantity()
            item.qty += qty_to_add
            found = True
            write_items(items)
            return
    # If item is not found, prompt the user to add the rest of the details and store in variables
    if found == False:
        manufacturer = input("Enter manufacturer: ")
        model = input("Enter model: ")
        price = get_valid_price()
        qty = get_valid_quantity()
        # Instantiating Item object using id, manufacturer, model, price, qty and appending to items
        items.append(Item(item_id, manufacturer, model, price, qty))
        # Sorting alphabetically by manufacturer
        items.sort(key=lambda item: item.manufacturer)
        write_items(items)

# Defining a funtion to lower quantity of items if items quantity is greater than 0
def del_item(items):
    found = False
    item_id = input("Enter item ID: ")

    for item in items:
        if item.id == item_id:
            qty_to_remove = get_valid_quantity()
            if qty_to_remove > item.qty:
                print("Not enough items in stock.")
            else:
                item.qty -= qty_to_remove
                found = True
                write_items(items)
            break
    
    if found == False:
        print("Item not found.")

# Defining a function to list inventory
def list_items(items):

    print("Inventory Program\n" + ("-" * 80))

    print(
        "Item ID".ljust(12) +
        "Manufacturer".ljust(20) +
        "Model".ljust(20) +
        "Price".rjust(10) +
        "Qty".rjust(8)
    )

    print("-" * 80)

    for item in items:
        print(
            item.id.ljust(12) +
            item.manufacturer.ljust(20) +
            item.model.ljust(20) +
            f"${item.price:.2f}".rjust(10) +
            str(item.qty).rjust(8)
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
    # Reading items from FILENAME
    items = read_items()

    print("Inventory Program")

    # Using a while loop for menu selection
    while True:
        display_menu()
        command = input("Command: ")

        if command == "list":
            list_items(items)
        elif command == "add":
            add_items(items)
        elif command == "del":
            del_item(items)
        elif command == "exit":
            quit_program()
        else:
            print("Invalid command.")

# Program entry point
if __name__ == "__main__":
    main()