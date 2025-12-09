players = {"Serena Williams":['Tennis',23], "Lionel Messi":['Soccer', 7] ,
"Michael Phelps": ['Swimming', 23], "Usain Bolt": ['Athletics',	8],
"Roger Federer":['Tennis',20], "Cristiano Ronaldo":['Soccer',5]}

for player, info in players.items():
    sport = info[0]
    awards = info[1]

    if sport == "Tennis" and awards > 10:
        print(f'{player} has won {awards} in the game of {sport}.')

        
    
players_detailed = {
    "Serena Williams": {'Sport': 'Tennis', 'Trophies': 23},
    "Lionel Messi": {'Sport': 'Soccer', 'Trophies': 7},
    "Michael Phelps": {'Sport': 'Swimming', 'Trophies': 23},
    "Usain Bolt": {'Sport': 'Athletics', 'Trophies': 8},
    "Roger Federer": {'Sport': 'Tennis', 'Trophies': 20},
    "Cristiano Ronaldo": {'Sport': 'Soccer', 'Trophies': 5}
}


for player, info in players_detailed.items():
    sport = info['Sport']
    awards = info['Trophies']

    if sport == "Tennis" and awards > 10:
        print(f'{player} has won {awards} in the game of {sport}.')

