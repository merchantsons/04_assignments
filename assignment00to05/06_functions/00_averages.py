# 00_averages.py by merchantsons

def average(a: float, b: float) -> float:
    """
    Returns the average of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The average of a and b
    """
    return (a + b) / 2

def main():
    # Test cases
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()