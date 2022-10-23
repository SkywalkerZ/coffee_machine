menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0.00,
}


def menu_iter(choice):
    item_list = []
    ingredient_list = []
    for value in menu[choice].values():
        item_list.append(value)
    for ingredients in item_list[0].values():
        ingredient_list.append(ingredients)
    ingredient_list.append(item_list[1])
    return list(ingredient_list)


def compare(resources_list, ingredient_list, money, user_input):
    if resources_list[0] >= ingredient_list[0]:
        if resources_list[1] >= ingredient_list[1]:
            if resources_list[2] >= ingredient_list[2]:
                if money >= ingredient_list[3]:
                    print(f"Here is your {user_input}")
                    resources["water"] -= ingredient_list[0]
                    resources["coffee"] -= ingredient_list[1]
                    resources["milk"] -= ingredient_list[2]
                    if money > ingredient_list[3]:
                        money_change = round(money - ingredient_list[3], 2)
                        print(f"Here is your change: ₹ {money_change}")
                        resources["money"] += ingredient_list[3]
                    else:
                        resources["money"] += ingredient_list[3]
                else:
                    print("Insufficient Money")
            else:
                print(f"There is not enough milk. You need {ingredient_list[2]} ml")
        else:
            print(f"There is not enough coffee. You need {ingredient_list[1]} ml")
    else:
        print(f"There is not enough water. You need {ingredient_list[0]} ml\nMoney ₹{money} returned")


def coffee_machine():
    machine_is_on = True
    paisa_insert = "0"
    while machine_is_on:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_input == "report":
            print(resources)
        elif user_input == "off":
            machine_is_on = False
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            user_rupee = input("How many Rupee?: ")
            user_paisa = input("How many Paisa?: ")
            if len(user_paisa) == 1:
                user_paisa = paisa_insert + user_paisa
            if user_paisa == "100":
                user_rupee = str(int(user_rupee) + 1)
                user_paisa = "00"
            user_money = user_rupee + "." + user_paisa
            user_money = float(user_money)
            item_list = menu_iter(user_input)
            resources_list = list(resources.values())
            compare(resources_list, item_list, user_money, user_input)
        else:
            print("Invalid input")
            coffee_machine()


coffee_machine()


