import math  # Import the math library for sqrt function

def main():
    # Prompt user for the lengths of the two perpendicular sides
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))
    
    # Calculate hypotenuse using Pythagorean theorem: BC² = AB² + AC²
    bc: float = math.sqrt(ab**2 + ac**2)
    
    # Print the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

if __name__ == '__main__':
    main()