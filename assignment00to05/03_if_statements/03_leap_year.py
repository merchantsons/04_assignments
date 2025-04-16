# 03_leap_year.py by merchantsons

def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    if year % 4 == 0:  # Checking whether the provided year is evenly divisible by 4
        if year % 100 == 0:  # Checking whether the provided year is evenly divisible by 100
            if year % 400 == 0:  # Checking whether the provided year is evenly divisible by 400
                print("That's a leap year!")
            else:  # (Not divisible by 400)
                print("That's not a leap year.")
        else:  # (Not divisible by 100)
            print("That's a leap year!")
    else:  # (Not divisible by 4)
        print("That's not a leap year.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
