def flights(*args):
    flights_dict = {}
    for idx in range(0, len(args), 2):
        destination_name = args[idx]

        if destination_name == "Finish":
            break
        else:
            passengers = args[idx + 1]

        if destination_name not in flights_dict:
            flights_dict[destination_name] = 0

        flights_dict[destination_name] += passengers

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
