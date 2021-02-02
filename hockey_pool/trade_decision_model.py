import pandas as pd

nhl21_schedule = [
    {"Month": "Jan", "Day": 27, "Home": "Nashville", "Away": "Chicago"},
    {"Month": "Jan", "Day": 27, "Home": "Ottawa", "Away": "Vancouver"},
    {"Month": "Jan", "Day": 28, "Home": "Pittsburgh", "Away": "Boston"},
    {"Month": "Feb", "Day": 1, "Home": "Pittsburgh", "Away": "NY Rangers"},
]

nhl_roster = {
    "Pittsburgh": ["Evgeni Malkin", "Bryan Rust", "Teodors Blueger"],
    "Nashville": ["Viktor Arvidsson", "Roman Josi", "Ryan Johansen"],
    "Chicago": ["Patrick Kane", "Alex Debrincat", "Pius Suter"],
    "Ottawa": ["Nikita Zaitsev", "Nick Paul", "Brady Tkachuk"],
    "Vancouver": ["Bo Horvat", "Brock Boeser", "Nils Höglander"],
    "NY Rangers": ["Mika Zibanejad", "Adam Fox", "Phil Di Giuseppe"],
}


schedule_df = pd.DataFrame.from_dict(nhl21_schedule)

roster_df = pd.DataFrame.from_dict(nhl_roster)


y = 0  # expected nb of pts for the rest of the mth of player 's'
p = 1.10  # current points per game average for the present season of player 's'
d = 2.39  # current goals against average of team 'j'
i = 1  # position of a game in the sequence of n games before the end of the month
n = 4  # nb of games remaining in the month
j = "Boston"  # team facing player 's' in the ith game
s = "Evgeni Malkin"  # full name of the player of interest
e = "Pittsburgh"  # team of player 's'

for g in range((i - 1), n, 1):
    y += p * (d / 2)


if __name__ == "__main__":
    print(y)
