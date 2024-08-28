from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#
menu = Menu()
# lists = Menu.get_items()
# User_Choice = input(f"What do you want? {lists}")
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
coffee_maker.report()
# is_sufficient = coffee_maker.is_resource_sufficient(User_Choice)
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like {options} or want report")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # is_sufficient = coffee_maker.is_resource_sufficient(choice) # Showing ERROR because it wants an object as paramaeter
        drink = menu.find_drink(choice)
        is_sufficient = coffee_maker.is_resource_sufficient(drink)
        if is_sufficient:
            is_successful = money_machine.make_payment(drink.cost)
            if is_successful is True:
                coffee_maker.make_coffee(drink)
            # Total = money_machine.process_coins()
            # is_successful = money_machine.make_payment()







