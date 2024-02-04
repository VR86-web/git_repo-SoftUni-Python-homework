from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employees_capacity = deque(int(x) for x in input().split(", "))

total_pizzas_made = 0
EMPLOYEES_SINGLE_ORDER_CAPACITY = 10

while pizza_orders and employees_capacity:
    pizza_order = pizza_orders.popleft()

    if 0 < pizza_order <= 10:
        employee_capacity = employees_capacity.pop()

        if pizza_order <= employee_capacity:
            total_pizzas_made += pizza_order
        else:
            total_pizzas_made += employee_capacity
            pizza_orders.appendleft(pizza_order - employee_capacity)


if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join([str(x)for x in employees_capacity])}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x)for x in pizza_orders])}")
