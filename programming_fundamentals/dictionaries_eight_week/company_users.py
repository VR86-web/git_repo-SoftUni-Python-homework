data_dict = {}
while True:
    data = input()
    if data == "End":
        break
    company_name, employee_id = data.split("->")
    if company_name not in data_dict:
        data_dict[company_name] = [employee_id]
    else:
        if employee_id not in data_dict[company_name]:
            data_dict[company_name] += [employee_id]
for company_name, employee_ids in data_dict.items():
    print(f"{company_name}")
    for ids in employee_ids:
        print(f"--{ids}")
