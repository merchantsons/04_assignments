def main():
    # Prompt user for temperature in Fahrenheit and convert to float
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius using the provided formula
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    # Print the result showing both temperatures
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()