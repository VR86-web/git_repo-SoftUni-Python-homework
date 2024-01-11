
username_dict = {}
message_capacity = int(input())
while True:
    command = input()
    if command == 'Statistics':
        break
    token = command.split('=')
    action = token[0]
    if action == 'Add':
        username = token[1]
        sent = int(token[2])
        received = int(token[3])
        if username not in username_dict:
            username_dict[username] = {'sent': sent, 'received': received}

    elif action == 'Message':
        sender = token[1]
        receiver = token[2]
        if sender in username_dict:
            if username_dict[sender]['sent'] + username_dict[sender]['received'] + 1 >= message_capacity:
                del username_dict[sender]
                print(f'{sender} reached the capacity!')
            else:
                username_dict[sender]['sent'] += 1
        if receiver in username_dict:
            if username_dict[receiver]['sent'] + username_dict[receiver]['received'] + 1 >= message_capacity:
                del username_dict[receiver]
                print(f'{receiver} reached the capacity!')
            else:
                username_dict[receiver]['received'] += 1

    elif action == 'Empty':
        username = token[1]
        if username == 'All':
            username_dict.clear()
        else:
            if username in username_dict:
                del username_dict[username]

print(f'Users count: {len(username_dict.keys())}')
for key, value in username_dict.items():
    print(f"{key} - {value['sent'] + value['received']}")
