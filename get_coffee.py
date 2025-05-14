from coffee_menu import Menu
from coffee_maker import CoffeeMaker
from money_count import MoneyMachine

menu = Menu()
deliver_coffee = CoffeeMaker()
payment = MoneyMachine()

coffee_maker_on = True
while coffee_maker_on:
    options = menu.get_items()
    drinker_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drinker_choice == "off":
        coffee_maker_on = False

    elif drinker_choice == "report":
        deliver_coffee.report()
        payment.report()

    elif drinker_choice == "maintenance":
        # Entering maintenance mode to allow resource modification
        resource_type = input("Which resource would you like to add (water/milk/coffee)? ").lower()
        try:
            amount = int(input("How much would you like to add? "))

            if resource_type in deliver_coffee.resources:

                    deliver_coffee.resources[resource_type] += amount
                    print(f"Added {amount} to {resource_type}.")
            else:
                print("Invalid resource.")
        except ValueError:
            print("Invalid amount entered.")

    else:
        type_of_drink = menu.find_drink(drinker_choice)
        if type_of_drink and deliver_coffee.is_resource_sufficient(type_of_drink) and payment.make_payment(type_of_drink.cost):
            deliver_coffee.make_coffee(type_of_drink)


