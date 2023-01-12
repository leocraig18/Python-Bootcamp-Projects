from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

on = True

while on:
    options = menu.get_items()
    move_on = False
    while not move_on:
        order_name = input(f"What would you like? ({options}):")
        if order_name == "espresso" or order_name == "latte" or order_name == "cappuccino" or order_name == "off" or order_name == "report":
            move_on = True
    if order_name == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order_name == 'off':
        on = False
    else:
        drink = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
