# 02_in_range.py by merchantsons

def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high

def main():
    # Example usage of the in_range function
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(n, low, high):
        print(f"{n} is within the range [{low}, {high}].")
    else:
        print(f"{n} is not within the range [{low}, {high}].")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
