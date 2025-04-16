# 04_tall_enough_to_ride.py by merchantsons

MINIMUM_HEIGHT: int = 50  # arbitrary units :)

def main():
    while True:
        user_input = input("How tall are you? (Press Enter to quit) ")
        if user_input == "":
            break
        try:
            height = float(user_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
