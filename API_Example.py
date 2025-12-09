import pandas as pd
import matplotlib.pyplot as plt

dict1 = {'a':[11,21,31],'b':[12,22,32]}

df = pd.DataFrame(dict1)
print(type(df))

# When you call the method head the dataframe communicates with the API
# displaying the first few rows of the dataframe.
print(df.head())

# The same happen when you use the method mean
print(df.mean())

from nba_api.stats.static import teams
import matplotlib.pyplot as plt

def one_dict(list_dict):
    '''The one_dict() function takes a list of dictionaries
    (each representing one team's details) and combines
    them into a single dictionary where each key contains a list of
    all corresponding values.'''

    keys = list_dict[0].keys()
    out_dict = {key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()

print(nba_teams[0:3])

# To make things easier, we can convert the dictionary to a table.
dict_nba_team = one_dict(nba_teams)
nba_teams = pd.DataFrame(dict_nba_team)
print(nba_teams.head())

df_warriors = nba_teams[nba_teams['nickname']=='Warriors']
print(df_warriors)

id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
print(id_warriors)

from nba_api.stats.endpoints import leaguegamefinder
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
print(gamefinder.get_json())
games = gamefinder.get_data_frames()[0]
print(games.head())
