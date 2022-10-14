from data import resources, menu, coins


def check_resources(order_ingredients):
    is_enough = True

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.”")
            is_enough = False
    return is_enough


def make_drink(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


is_off = False
profit = 0


# 1) Take user drink order as an input.

while not is_off:
    user_bank = 0

    choice = input(
        "What would you like to drink? 'Espresso', 'Latte', or 'Cappacino': "
    ).lower()

    # 2) Create on/off prompt to turn coffee machine off
    if choice == "off":
        is_off = True

    # 3) Print report. When user enters report into console, print current resources list
    elif choice == "report":

        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")

    # 4) Check if resources are sufficient. When the user chooses a drink, the program should check if there are enough resources to make that drink.
    else:
        drink = menu[choice]
        check_resources(drink["ingredients"])

        if check_resources(drink["ingredients"]):
            # 5) Process coins.
            for key in coins:
                number_of_coins = float(input(f"how many {key}: "))
                total = number_of_coins * coins[key]
                user_bank += total

            # 6) Check if transaction was successful

            if user_bank >= drink["cost"]:
                profit += drink["cost"]
                user_change = user_bank - drink["cost"]
                user_change = float(round(user_change, 2))

                if user_bank > drink["cost"]:
                    print(f"Here is ${user_change} dollars in change.")

                make_drink(drink["ingredients"])
                print(f"Here is your {choice}. Enjoy! ")

            else:
                print("Sorry that's not enough money. Money refunded.")
