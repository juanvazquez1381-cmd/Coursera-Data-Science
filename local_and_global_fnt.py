# Part 1: Global variable declaration
global_variable = "I'm global"


# Part 2: Function definition
def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

# Part 3: Function call
example_function()

# Part 4: Accessing global variable outside the function
print(global_variable)


# Part 5: Attempting to access local variable outside the function
# print(local_variable)  # Error, local variable not visible here





