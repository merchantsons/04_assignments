# 07_print_divisor.py by merchantsons

def print_divisors(num: int):
    """
    Prints all divisors of the given number.
    """
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
        if num % i == 0:  # Check if i is a divisor of num
            print(i)

def main():
    num = int(input("Enter a number: "))  # Prompt the user to enter a number
    print_divisors(num)  # Call the print_divisors function with the user's input

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
