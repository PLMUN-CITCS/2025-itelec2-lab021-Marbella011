def get_non_negative_integer():
    """Obtains a non-negative integer input from the user."""
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number >= 0:
                return number
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_factorial(n: int) -> int:
    """Calculates the factorial of a given non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The factorial of n.  Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

def main():
    """Main function to get input and display factorial."""
    number = get_non_negative_integer()
    factorial = calculate_factorial(number)
    print(f"The factorial of {number} is: {factorial}")

if __name__ == "__main__":
    main()
    
