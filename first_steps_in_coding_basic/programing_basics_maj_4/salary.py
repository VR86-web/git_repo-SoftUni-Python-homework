
num_of_open_tabs = int(input())
salary = int(input())

for current_tab in range(num_of_open_tabs):
    name_of_open_tabs = input()
    if name_of_open_tabs == "Facebook":
        salary -= 150
    elif name_of_open_tabs == "Instagram":
        salary -= 100
    elif name_of_open_tabs == "Reddit":
        salary -= 50

    if salary <= 0:
        break
if salary > 0:
    print(int(salary))
else:
    print("You have lost your salary.")