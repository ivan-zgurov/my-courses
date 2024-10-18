# 44 / 100

def team_lineup(*players_data):
    from collections import defaultdict

    country_dict = defaultdict(list)

    for player_name, country in players_data:
        country_dict[country].append(player_name)

    # Sort countries
    sorted_countries = sorted(country_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    # Output
    result = []
    for country, players_list in sorted_countries:
        result.append(f"{country}:")
        for player in sorted(players_list):
            result.append(f"  -{player}")

    return "\n".join(result)


# Examples
print(
    team_lineup(
        ("Harry Kane", "England"),
        ("Manuel Neuer", "Germany"),
        ("Raheem Sterling", "England"),
        ("Toni Kroos", "Germany"),
        ("Cristiano Ronaldo", "Portugal"),
        ("Thomas Muller", "Germany"),
    )
)

print(
    team_lineup(
        ("Lionel Messi", "Argentina"),
        ("Neymar", "Brazil"),
        ("Cristiano Ronaldo", "Portugal"),
        ("Harry Kane", "England"),
        ("Kylian Mbappe", "France"),
        ("Raheem Sterling", "England"),
    )
)

print(
    team_lineup(
        ("Harry Kane", "England"),
        ("Manuel Neuer", "Germany"),
        ("Raheem Sterling", "England"),
        ("Toni Kroos", "Germany"),
        ("Cristiano Ronaldo", "Portugal"),
        ("Thomas Muller", "Germany"),
        ("Bruno Fernandes", "Portugal"),
        ("Bernardo Silva", "Portugal"),
        ("Harry Maguire", "England"),
    )
)
