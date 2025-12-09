# Conditional Equal
a = 5
print(a==6)

# Greater than Sign
i = 6
print(i > 5)

# Greater than sign
i = 2
print(i>5)

# Inequality Sign
i = 2
print(i!=6)

# Inequality Sign
i = 6
print(i!= 6)

# Use Equality sign to compare the strings
print("ACDC" == "The Bodyguard")

# Use Inequality sign to compare the strings
print("ACDC" != "The Bodyguard")

# Compare characters
print('B' > 'A')

# When there are multiple letters, the first letter takes precedence in ordering:
print('BA' > 'AB')

# If statment example

age = 19

#Expression that can be true or false
if age > 18:
    print("You can enter")

print("Move on")

# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")

# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


# Condition statment example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")

print('do something. .')

# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
