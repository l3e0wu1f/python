# INF322 Python
# Josh Lewis
# Final Project: Interactive Shopping Cart
#   An application for users to shop at a farmer's market produce stand. It pulls the inventory from an external file, logs errors to an
#   external log file if the inventory file is not found, and uses OOP to modify and display the contents of a shopping cart, via three
#   classes for Item, Quantity, and ShoppingCart objects.

import os
import logging

# Log error externally to log file
logging.basicConfig(filename='myCartLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Toggle below to turn off logging. Even if there's no error to log, a blank log file will be created unless below is un-commented.
# logging.disable(logging.DEBUG) 

allItems = []

# Item object class
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price
        
# Quantity object class
class Quantity:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

    def getName(self):
        return self.name

    def getPrice(self):
        return self.qty

# Cart object class
class ShoppingCart:
    def __init__(self):
        self.list = []

    def addItem(self, quantity):
        # Adds the specified quantity of an item to cart
        self.list.append(quantity)

    def getTotal(self):
        # Tallies up the price of all items in cart
        total = 0
        price = 0
        for item in self.list:
            name = item.name
            for it in allItems:
                if name == it.name:
                    price = it.price
            qty = item.qty
            total = total + (price * qty)
        return total

    def getNumItems(self):
        # Counts the number of each item in cart
        count = 0
        for c in self.list:
            count = count + 1
        return count

    def removeItem(self, name):
        # Removes all of one type of item from the cart's item list
        for it in self.list:
            if name == it.name:
                self.list.remove(it)

    def itemsInCart(self):
        # Displays a list of all items in cart
         if self.getNumItems() == 0:
             print("Your cart is currently empty.")
         else:
            print("\nItems currently in your cart: ")
            for it in self.list:
                if it.qty > 1:
                    print("%i %ss"%(it.qty, it.name))
                else:
                    print("%i %s"%(it.qty, it.name))

def welcomeMessage():
    print("Welcome to the farmstand! Please use the menu below to browse our inventory.")

def getInventory():
    # Check for valid inventory file. Log the error to external log if file not found.
    try:
        with open("inventory.txt") as fd:
            for line in fd:
                name, price = line.split(",")
                it = Item(name, float(price.strip()))
                allItems.append(it)
    except:
        # if os.path.isfile("inventory.txt") == False:
        logging.debug("Attempted to open 'inventory.txt'. File does not exist!")
        print("Inventory file not found!")

def listAll():
    # List every item available for purchase
    if os.path.isfile("inventory.txt") == False:
        print("Inventory file not found!")
    else:
        print("Inventory of produce: ")
        for it in allItems:
            print("%s $%.2f"%(it.name, it.price))

# Main program
def main():
    c = ShoppingCart()

    # Retrieve inventory from file
    getInventory()

    # Welcome user to shop   
    welcomeMessage()
    choice = 1
    while choice != 6:
        print ("\n*** MAIN MENU ***")
        print ("1. List avaiable items and their prices.")
        print ("2. Add an item to your cart.")
        print ("3. List items in your cart.")
        print ("4. Remove an item from your cart.")
        print ("5. Go to checkout.")
        print ("6. Exit.")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 6:
                print("Thanks for stopping by!")
                return
            elif choice == 1:
                listAll()
            elif choice == 2:
                name = input("Add the following product to cart: ")
                quantity = int(input("Quantity: "))
                q = Quantity(name.lower(), quantity)
                c.addItem(q)  
            elif choice == 3:
                c.itemsInCart()
            elif choice == 4:
                name = input("Remove all of the following product from cart: ")
                c.removeItem(name.lower())
            elif choice == 5:
                if c.getNumItems() == 0:
                     print("Your cart is currently empty. Please add an item.")
                else:
                    print("You are purchasing: ")
                    for it in c.list:
                        if it.qty > 1:
                            print("%i %ss"%(it.qty, it.name))
                        else:
                            print("%i %s"%(it.qty, it.name))
                    if c.getTotal() == 0.0:
                        print ("The item(s) you have enetered are invalid. \nThey will not be included with your purchase.\nPlease add some valid items and try again.")
                    subTotal = c.getTotal()
                    tax = subTotal * 0.08
                    total = subTotal + tax
                    print("Order subtotal: $%.2f" %(subTotal))
                    print("Tax: $%.2f" %(tax))
                    print("Order total: $%.2f" %(total))
            elif choice > 6:
                print("Please choose a valid option (1 – 6).")
                continue
        except:
            print("You've entered non-numeric characters. Please choose a valid option between 1 and 6.")
            continue
        
# Run the program      
main()  
