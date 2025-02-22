def get_non_negative_integer():
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number >= 0:
                return number
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
