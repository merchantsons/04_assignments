# 01_greetings.py by merchantsons

def main():
    name = input("What's your name? ")  # Prompt the user to enter their name
    greet(name)  # Call the greet function with the user's input

# There is no need to edit code beyond this point

def greet(name: str):
    """
    Prints a greeting message for the given name.
    """
    print("Greetings " + name + "!")

if __name__ == '__main__':
    main()
