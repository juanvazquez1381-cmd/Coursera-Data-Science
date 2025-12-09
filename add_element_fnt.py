# Part 1: Initialize an empty list

# Define an empty list as the initial data structure
my_list = []

# Part 2: Define a function to add elements

# Functon to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)

# Part 3: Define a function to remove elements

def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

# Part 4: Add elements to the list

# Add elements to the list using the add_element function
add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)

# Part 5: Print the current list

# Print the current list
print("Current list:", my_list)

# Part 6: Remove elements from the list

# Remove an element from the list using the remove_element function
remove_element(my_list, 17)
remove_element(my_list, 55)  # This will print a message since 55 is not in the list

# Part 7: Print the updated list

# Print the updated list
print("Updated list:", my_list)
