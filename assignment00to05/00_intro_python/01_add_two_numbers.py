def main():
    # Prompt user for first number and convert to integer
    first_number = int(input("Please enter the first number: "))
    
    # Prompt user for second number and convert to integer
    second_number = int(input("Please enter the second number: "))
    
    # Calculate the sum
    total = first_number + second_number
    
    # Print the result
    print(f"The sum of {first_number} and {second_number} is: {total}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()