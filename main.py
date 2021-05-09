MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def is_resources_sufficient(order_ingredients):
    """Checking if Resources are sufficient==>returns True, else False"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total value of coins inserted in Dollars"""
    print("Please insert Coins")
    quarters = int(input("How many Quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickels = int(input("How many nickels? :"))
    pennies = int(input("How many pennies? :"))
    money = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return money

def is_transaction_successful(money_received, drink_cost):
    """Return True is Transaction is completed, else False"""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit+=drink_cost
        return True
    else:
        print("Sorry thats not enough money. Money Refunded.")
        return False

def make_coffee(drink_name,  order_ingredients ):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}☕️")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    choice = choice.lower()
    if choice =="off":
        is_on=False
    elif choice =="report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: {profit}")

    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])








