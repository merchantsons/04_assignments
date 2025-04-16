# This program converts feet to inches.
INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    # Prompt user for feet and convert to float
    feet: float = float(input("Enter number of feet: "))
    
    # Calculate inches by multiplying feet by conversion factor
    inches: float = feet * INCHES_IN_FOOT
    
    # Print the result
    print("That is", inches, "inches!")

if __name__ == '__main__':
    main()