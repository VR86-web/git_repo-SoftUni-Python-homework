def stock_availability(flavors, *args):
    action, *types = args

    if action == "delivery":
        flavors.extend(types)
    elif action == "sell":
        if types:
            for type in types:
                if str(type).isdigit():
                    flavors = flavors[type:]
                else:
                    while type in flavors:
                        flavors.remove(type)
        else:
            flavors.pop(0)

    return flavors


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))