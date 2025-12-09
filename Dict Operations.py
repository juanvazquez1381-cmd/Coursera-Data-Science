# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)

# Access to the value by the key
print(Dict["key1"])

# Access to the value by the key
print(Dict[(0, 1)])

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                     "The Dark of the Moon": "1973", "The Bodyguard": "1992",\
                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                     "Saturday Night Fever": "1977", "Rumours": "1977"}

print(release_year_dict)

# Get value by keys
print(release_year_dict['Thriller'])
print("Thrillers was realse in",release_year_dict['Thriller'])

# Get value by key
print(release_year_dict['The Bodyguard'] )

# Get all the keys in dictionary
print(release_year_dict.keys() )

# Get all the values in dictionary
print(release_year_dict.values() )

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
print(release_year_dict)

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print(release_year_dict)


