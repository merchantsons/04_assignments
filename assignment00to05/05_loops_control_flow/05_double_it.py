# 05_double_it.py by merchantsons

def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    curr_value = num
    # Loop while current value is less than 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')
    print()  # For a new line after the output

if __name__ == '__main__':
    main()