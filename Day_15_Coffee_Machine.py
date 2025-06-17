MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 25,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 35,
    },
    "cappuccino": {   
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 40
    }
}

def coffee_logo():
    print("""
   ( (
    ) )
  ........
  |      |]    ☕ COFFEE MACHINE
  \\      /     ----------------
   `----'
""")

coffee_logo()  # ✅ show logo at the beginning

profit = 0
resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many ₹10 coins? ")) * 10
    total += int(input("How many ₹5 coins? ")) * 5
    total += int(input("How many ₹2 coins? ")) * 2
    total += int(input("How many ₹1 coins? ")) * 1
    return total

def make_coffee(choice, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {choice} ☕. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()  # ✅ normalize input

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['Water']}ml")
        print(f"Milk: {resources['Milk']}ml")
        print(f"Coffee: {resources['Coffee']}g")
        print(f"Money: ₹{profit}")

    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                if change > 0:
                    print(f"Here is ₹{change} in change.")
                profit += drink["cost"]
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Invalid input. Please choose espresso, latte, or cappuccino.")


