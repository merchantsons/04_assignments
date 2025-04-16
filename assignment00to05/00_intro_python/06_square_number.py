def main():
    # Prompt user for a number and convert to float
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square
    square = number * number
    
    # Print the result
    print(f"{number} squared is {square}")

if __name__ == '__main__':
    main()