# count_even.py by merchantsons

def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # If the current number in the list is even (divisible by 2)
            count += 1  # Add one to our count!

    print(count)  # Print out how many even numbers we counted above

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers
    while True:  # Loop indefinitely
        user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
        if user_input == "":  # If the user presses enter without typing anything
            break  # Exit the loop
        lst.append(int(user_input))  # Cast the user input into an integer and add it to our list

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
