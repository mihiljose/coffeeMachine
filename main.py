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

choice = input("What would you like? (espresso/latte/cappuccino): ")
choice = choice.lower()

print("Please insert Coins")
quarters = input("How many Quarters? :")
dimes = input("How many dimes? :")
nickels = input("How many nickels? :")
pennies = input("How many pennies? :")

money = (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
if choice == "report":
    print (resources)
elif choice == "espresso":
    if(money<1.5):
        print("Sorry! not enough Money has been inserted")





