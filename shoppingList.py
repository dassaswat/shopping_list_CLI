import sys
shopping_list = []

def add_items(things):
    shopping_list.append(things)


def print_list(things_added):
    print("=====> Your List <=====")
    value = 1
    for thing in things_added:
        print(">> {}: {}".format(value, thing))
        value += 1


def show_help():
    print("""
 ENTER "YES"  to add items.
 Enter "DONE" to get the final list.
 Enter "HELP" for this help.
 Enter "LIST" to see this  list.
""")


def if_yes():
    print('TO ADD ITEM (TYPE THE ITEM NAME AND TO GO BACK TYPE "Back"')
    while True:
        user_item = input(">>  ")
        add_items(user_item)
        if user_item.lower() == "back":
            del shopping_list[-1]
            loop()


def show_list():
    print("ITEM ADDED")
    print("Your current items in the cart are as follow: ")
    print_list(shopping_list)


def show_done():
    print_list(shopping_list)
    sys.exit("Thank you for using our Application")


def loop():
    while True:
        user_entry = input("Kindly choose between(YES/DONE/LIST/HELP)  ")
        print("Currently you have {} items in your cart".format(len(shopping_list)))

        if user_entry.lower() == "help":
            show_help()

        elif user_entry.lower() == "list":
            show_list()

        elif user_entry.lower() == "done":
            show_done()

        elif user_entry.lower() == "yes":
            if_yes()

name= input("Welcome, Please enter your name:      ")
print ("Hey {}, welcome to the Cart's App. I will help you create a shopping list.".format(name))
print("\n")
show_help()
loop()
