from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
coffee_machine = CoffeeMaker()
money_dispense = MoneyMachine()

machine_on = True

while machine_on:

    options = menu_list.get_items()

    user_order = input(f"What would you like to drink? {options}: ").lower()

    if user_order == "off":
        machine_on = False
    elif user_order == "report":
        coffee_machine.report()
        money_dispense.report()
    else:
        drink = menu_list.find_drink(user_order)

        if coffee_machine.is_resource_sufficient(drink):
            if money_dispense.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
