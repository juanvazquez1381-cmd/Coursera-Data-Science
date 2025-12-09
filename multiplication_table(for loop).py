def simple_multiplication():
    """
    This function will ask for a number and a limit. Based on the inputs it will
    generate a multiplication table

    for example if the the number is 5 and limit is 5 then we will have:
    5 x 1 = 5
    5 x 2 = 10
    .
    .
    5 x 5 = 25
    """
    try:
        number = int(input("Enter a number to generates its multiplication table: "))

    except ValueError:
        print("Invalid input. Please enter an integer.")

    else:
        try:
            limit = int(input("Enter the upper limit for the multiplication(e.g., 10 for 1 to 10): "))

        except ValueError:
            print("Invalid input for the limit. Please enter an integer.")

        else:
            print(f"\nMultiplication Table {number} up to {limit}:\n")
        
            for i in range(1,limit + 1):
                result = number * i
                print(f"{number} x {i} = {result}")

simple_multiplication()



    
