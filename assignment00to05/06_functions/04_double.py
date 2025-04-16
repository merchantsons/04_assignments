# 04_double.py by merchantsons

def double(num: int) -> int:
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    num = int(input("Enter a number: "))  # Prompt the user to enter a number
    num_times_2 = double(num)  # Call the double function with the user's input
    print("Double that is", num_times_2)  # Print the result

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
