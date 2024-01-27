# def grocery_store(**product_data):
#   product_data = sorted(product_data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

#    result = []
#    for name, quantity in product_data:
#        result.append(f"{name}: {quantity}")

#    return "\n".join(result)

def grocery_store(**product_data):
    product_data = sorted(product_data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    return "\n".join(f"{p}: {q}" for p, q in product_data)


print(grocery_store(bread=5,pasta=12,eggs=12,))