def main():
    # Prompt user for the two integers
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))
    
    # Calculate quotient (integer division) and remainder
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor
    
    # Print the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()