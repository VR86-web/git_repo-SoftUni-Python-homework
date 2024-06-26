def team_lineup(*args):

    country_players = {}

    for player_name, country in args:
        if country not in country_players:
            country_players[country] = []

        country_players[country].append(player_name)

    result = ""

    sorted_players = sorted(country_players.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for country, players in sorted_players:
        result += f"{country}:\n"
        for player_name in players:
            result += f"  -{player_name}\n"

    return result
