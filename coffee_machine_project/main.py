from data import resources, recipes

espresso = recipes[0]
latte = recipes[1]
cappacino = recipes[2]

def get_report(resources):
    return resources

# def check_resources(resources, order):
#     if order == 

def get_order( recipes):
    order = input("What would you like to drink? 'Espresso', 'Latte', or 'Cappacino': ").lower()
    for item in recipes:
        for key in item:
            if order == item[key]:
                return item[key]
report = get_report(resources)
guess = get_order(recipes)

print(guess)
# print(report)