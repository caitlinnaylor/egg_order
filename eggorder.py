def get_orders(names, egg_order):
    """
    Collects order information - name, number of eggs – in a loop. Store in 2 lists.
    Call read_int function to ensure you have a valid input
    """

    print ("Collecting Orders")
    cont = "Y"
    while cont != "N":
        name = input("What is the name for the order? ")
        names.append(name)
        num_eggs = int(input("How many eggs are being ordered? "))
        egg_order.append(num_eggs)
        cont = input("Do you wish to enter more order? Enter N to stop or Y to continue")

    return egg_order, names

def show_orders(names, egg_order):
    """
    calculates price for each egg order, and displays order information - name, number of eggs, price
    """
    PRICE_PER_DOZEN = 6.5
    print("Showing orders")
    for i in range (len(egg_order)):
        price = egg_order [i] * PRICE_PER_DOZEN
        print("Name: {}".format(names[i]))
        print("Number of eggs: {}".format(egg_order[i]))
        print("Total cost: {}".format(price))
    
    #?
    #?



  
#main routine
names = []
egg_order = []
get_orders(names, egg_order)
show_orders(names, egg_order)
show_report(egg_order)

