Menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 200, "milk": 50, "coffee": 24, "cost": 3.0}
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0

}

def print_report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money:$ {resources['money']}")

def check_resources(drink):
    for item in Menu[drink]:
        if item != "cost" and Menu [drink][item] > resources[item]:
            print(f"Sorry,not enough {item}.")
            return False
        return True
    
def process_coins():
    print("please insert coins:")
    total = 0
    total += int(input("How many ₹10 coins? ")) * 10
    total += int(input("How many ₹5 coins?")) * 5
    total += int(input("How many ₹2 coins?")) * 2
    total += int(input("How many ₹1 coins?")) * 1
    return total
def make_coffee(drink):
    for item in Menu[drink]:
        if item != "cost":
            resources[item] -= Menu[drink][item]
    print(f"Here is your drink ☕. Enjoy!")

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        
        elif choice == "report":
            print_report()
        
        elif choice in Menu:
            if not check_resources(choice):
                continue  # Not enough ingredients, skip to next loop
            
            payment = process_coins()
            if payment >= Menu[choice]["cost"]:
                change = payment - Menu[choice]["cost"]
                if change > 0:
                    print(f"Here is ₹{change} in change.")
                resources["money"] += Menu[choice]["cost"]
                make_coffee(choice)
            else:
                print("Sorry, that's not enough money. Money refunded.")
        
        else:
            print("Invalid selection, please try again.")

coffee_machine()


                

