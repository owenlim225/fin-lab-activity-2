import sys
import os
import time

#LIMOSNERO, SHERWIN P.

#Cost of each item
burger = 30.00
fries = 25.00
softdrink = 15.00

#Starting value
num_burgers = 0
num_fries = 0
num_softdrinks = 0


#Clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()


#user input
def user_input():
    global num_burgers, num_fries, num_softdrinks
    
    #introduction


    while True:
        try:
            print(" ")
            print(" ")
            print("                                 Welcome to Symex fastfood!")
            print(" ")
            print(" ")
            print('                                 "Sa unang kagat, omaygad!"')
            print(" ")
            print(" ")
            print("Hamburger for just ₱30.00!         Fries for just ₱25.00!         Soft drinks for just ₱15.00!")
            print(" ")
            print(" ")
        
            num_burgers = int(input("How many hamburger would you like?      "))
            num_fries = int(input("How many fries would you like?          "))
            num_softdrinks = int(input("How many soft drinks would you like?    "))
            
        except ValueError:
            print(" ")
            print("Invalid input. Please try again.")
            time.sleep(3)
            clear_screen()
            continue

        if num_burgers > 0 or num_fries > 0 or num_softdrinks > 0:
            break
        else:
            print(" ")
            print("Please order at least one item.")
            time.sleep(3)
            print(" ")
            clear_screen()
        
        

user_input()

clear_screen()

#order correction
def correct_order():
    while True:
        clear_screen
        print(" ")
        print(" ")
        print("                                 Welcome to Symex fastfood!")
        print(" ")
        print(" ")
        print('                                 "Sa unang kagat, omaygad!"')
        print(" ")
        print(" ")
        print("Hamburger for just ₱30.00!         Fries for just ₱25.00!         Soft drinks for just ₱15.00!")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        
        print("You ordered:")
        print(" ")
        print("Hamburger:    ", num_burgers, "pcs")
        print("Fries:        ", num_fries, "pcs")
        print("Soft drinks:  ", num_softdrinks, "pcs")
        print(" ")
        order = input("Are your orders correct? Y/N ").upper()
        
        if order == 'N':
            clear_screen()
            print(" ")
            print("Thank you for your time, come again!")
            time.sleep(2)
            clear_screen()
            sys.exit()
                
        elif order == 'Y':
            clear_screen()
            break

        else:
            print(" ")
            print("Your input is invalid")
            time.sleep(2)
            clear_screen()
            continue

correct_order()


#Calculation
cost_burger = num_burgers * burger
cost_fries = num_fries * fries
cost_softdrink = num_softdrinks * softdrink


#cost of burger and fries combined
cost_food = cost_burger + cost_fries


#total amount (pre-taxed)
item_cost = cost_burger + cost_fries + cost_softdrink


#4% tax
cost_tax = item_cost * 0.04


#total amount (post-taxed)
cost_total = item_cost + cost_tax



#Receipt + Amount paid
while True:
    
    print(" ")
    print(" ")
    print("                                 Welcome to Symex fastfood!")
    print(" ")
    print(" ")
    print('                                 "Sa unang kagat, omaygad!"')
    print(" ")
    print(" ")
    print("Hamburger for just ₱30.00!         Fries for just ₱25.00!         Soft drinks for just ₱15.00!")
    print(" ")
    print(" ")
    
    #Receipt
    print(" ")
    print("            Receipt:")
    print(" ")
    print(f"Cost of food:          ₱{cost_food:.2f}")
    print(f"Cost of beverage:      ₱{cost_softdrink:.2f}")
    print(f"Total tax (4%)         ₱{cost_tax:.2f}")
    print(" ")
    print(f"Total cost:            ₱{cost_total:.2f}")
    print(" ")
    
    
    print(" ")
    try:
        num_amount = int(input("How much would you like to pay? ₱"))
        
    except ValueError:
        print(" ")
        print("Invalid input. Please try again.")
        time.sleep(2)
        print(" ")
        continue
    
    if num_amount < cost_total:
        print(" ")
        print("You have insufficient money. Try again")
        time.sleep(2)
        clear_screen()
        continue
    
    elif num_amount >= cost_total:
        change = num_amount - cost_total
        clear_screen()
        
        print(" ")
        print(" ")
        print("                                 Welcome to Symex fastfood!")
        print(" ")
        print(" ")
        print('                                 "Sa unang kagat, omaygad!"')
        print(" ")
        print(" ")
        print("Hamburger for just ₱30.00!         Fries for just ₱25.00!         Soft drinks for just ₱15.00!")
        print(" ")
        print(" ")
            
        #Receipt
        print(" ")
        print("            Receipt:")
        print(" ")
        print(f"Cost of food:          ₱{cost_food:.2f}")
        print(f"Cost of beverage:      ₱{cost_softdrink:.2f}")
        print(f"Total tax (4%)         ₱{cost_tax:.2f}")
        print(" ")
        print(f"Total cost:            ₱{cost_total:.2f}")
        print(f"Amount paid:           ₱{num_amount:.2f}")     
        print(" ")
        print(f"Change:                ₱{change:.2f}")
        print(" ")
        break
        
        
    else:
        print("Your input is invalid")
        time.sleep(2)
        continue


#Ending
while True:
    order = input("Is everything to your satisfaction? Y/N ").upper()
    
    if order == 'N':
        print(" ")
        print("Thank you for your testing this out! --> Sherwin")
        time.sleep(2)
        clear_screen()
        sys.exit()
            
    elif order == 'Y':
        print(" ")
        
        print("Thank you dear customer, come again!")
        time.sleep(2)
        clear_screen()
        sys.exit()

    else:
        print(" ")
        print("Thank you for your testing this out! --> Sherwin")
        time.sleep(2)
        clear_screen()
        sys.exit()