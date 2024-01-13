from collections import deque

clients_name = input()
customers = deque()

while clients_name != "End":
    if clients_name == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(clients_name)
    clients_name = input()

print(f"{len(customers)} people remaining.")