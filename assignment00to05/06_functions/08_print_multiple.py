# 08_print_multiple.py by merchantsons

def print_multiple(message: str, repeats: int):
    """
    Prints the message a specified number of times.
    """
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")  # Prompt the user to enter a message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Prompt the user to enter the number of repeats
    print_multiple(message, repeats)  # Call the print_multiple function with the user's input

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
