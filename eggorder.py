import math
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
        cont = input("Do you wish to enter more order? Enter N to stop or Y to continue: ")

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
        print("Cost: {}".format(price))
    return 
    
def show_report(egg_order):
    """
    displays summary - total eggs, number of dozens to be ordered, average eggs per customer.
    Print "No orders" if no orders received otherwise print "Summary , Total eggs and Dozens required (call get_dozens function)
    as well as Average"
    """
    print("Summary")
    total_eggs = 0
    for i in range(len(egg_order)):
        total_eggs+=egg_order[i]
    get_dozens(total_eggs)
    avg = total_eggs / len(egg_order)
    print("The average number of eggs per customer is {}".format(avg))

def get_dozens (total_eggs):
    """
    returns whole number of dozens required to meet required number of eggs
    """
    dozens_ordered = total_eggs /12
    dozens_ordered = math.ceil(dozens_orders)
    print("Amount of dozens to be ordered: {}".format(dozens_ordered))

def read_pos_int(prompt):
   
      print("Not sure what this is")


#main routine
names = []
egg_order = []
get_orders(names, egg_order)
show_orders(names, egg_order)
show_report(egg_order)

