def lookup_team(player, rosters):
    for k, v in rosters.items():
        if player in v:
            return k


if __name__ == "__main__":
    rosters = {
        "Pittsburgh": ["Evgeni Malkin", "Bryan Rust", "Teodors Blueger"],
        "Nashville": ["Viktor Arvidsson", "Roman Josi", "Ryan Johansen"],
        "Chicago": ["Patrick Kane", "Alex Debrincat", "Pius Suter"],
        "Ottawa": ["Nikita Zaitsev", "Nick Paul", "Brady Tkachuk"],
        "Vancouver": ["Bo Horvat", "Brock Boeser", "Nils Höglander"],
        "NY Rangers": ["Mika Zibanejad", "Adam Fox", "Phil Di Giuseppe"],
    }
    print(lookup_team("Pius Suter", rosters))
