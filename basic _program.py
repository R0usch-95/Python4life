basket = []
grocery_item = str(input("enter the value:  "))
bag = []
bag.append(grocery_item)
for item in bag:

    if item is not "fruits":
        basket.append(grocery_item)
    else:
        print("move to fruits counter")

print("have a good day")


