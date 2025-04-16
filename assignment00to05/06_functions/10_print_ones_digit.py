# 10_print_ones_digit.py by merchantsons

def print_ones_digit(num: int):
    """
    Prints the ones digit of the given number.
    """
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))  # Prompt the user to enter a number
    print_ones_digit(num)  # Call the print_ones_digit function with the user's input

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
