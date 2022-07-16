from data import resources, recipes

def get_report(resources):
    return resources

def get_order(recipes):

    hot_drink = input("What would you like to drink? 'Espresso', 'Latte', or 'Cappacino': ").lower()

    for drink in recipes:
    
        name = drink["drink"]
        # water = drink["water"]
        # milk = drink["milk"]
        # coffee = drink["coffee"]
        # price = drink["price"]

        if hot_drink == name:
            # return name, water, milk, coffee, price
            return drink
    
order = get_order(recipes)
print(order)

def check_resources(order, resources):

    updated_resources = {}
    order_keys = set(order.keys())
    resource_keys = set(resources.keys())
    order_values = set(order.values())
    resource_values = set(resources.values())

    return order_keys, resource_keys

    if resource_keys > order_keys:
        water = resources["water"] - order["water"]
        updated_resources["water"].append(water)
    
    return updated_resources

print(check_resources(order, resources))

report = get_report(resources)


