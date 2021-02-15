import math
def get_orders(names, egg_order):
    """
    Collects order information - name, number of eggs – in a loop. Store in 2 lists.
    Call read_int function to ensure you have a valid input
    """

    print ("Collecting Orders")
    cont = "Y"
    while cont == "Y":
        name = input("What is the name for the order? ").capitalize()
        names.append(name)
        num_eggs = int(input("How many eggs are being ordered? "))
        egg_order.append(num_eggs)
        while cont != "N": #So that characters other than N or Y are not valid
            cont = input("Do you wish to enter more orders? Enter N if No or Y if Yes: ").upper()
            if cont == "Y":
                break
            else:
                print ("That is not a valid answer. Please enter N for No or Y for Yes")
    return egg_order, names

def show_orders(names, egg_order):
    """
    calculates price for each egg order, and displays order information - name, number of eggs, price
    """
    PRICE_PER_DOZEN = 6.5
    print("")
    print("Showing orders")
    for i in range (len(egg_order)):
        price = egg_order [i] * PRICE_PER_DOZEN
        print("Name: {}".format(names[i]))
        print("Number of eggs: {}".format(egg_order[i]))
        print("Cost: ${:.2f}".format(price))
        print("")
    return 
    
def show_report(egg_order):
    """
    displays summary - total eggs, number of dozens to be ordered, average eggs per customer.
    Print "No orders" if no orders received otherwise print "Summary , Total eggs and Dozens required (call get_dozens function)
    as well as Average"
    """
    print("")
    print("Summary")
    total_eggs = 0
    for i in range(len(egg_order)):
        total_eggs+=egg_order[i]
    print("Total eggs: {}".format(total_eggs))
    get_dozens(total_eggs)
    avg = total_eggs / len(egg_order)
    print("The average number of eggs per customer is {:.2f}".format(avg))

def get_dozens (total_eggs):
    """
    returns whole number of dozens required to meet required number of eggs
    """
    dozens_ordered = total_eggs /12
    dozens_ordered = math.ceil(dozens_ordered) #So that the amount of dozens cover all the eggs
    print("Amount of dozens to be ordered: {}".format(dozens_ordered))

def read_pos_int(prompt):
   
      print("Not sure what this is for?")


#main routine
names = []
egg_order = []
get_orders(names, egg_order)
show_orders(names, egg_order)
show_report(egg_order)

