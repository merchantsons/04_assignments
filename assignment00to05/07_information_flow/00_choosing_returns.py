# 00_choosing_returns.py by merchantsons

ADULT_AGE = 18  # U.S. age

def is_adult(age: int) -> bool:
    """
    Returns True if the age is greater than or equal to ADULT_AGE, otherwise returns False.
    """
    return age >= ADULT_AGE

########## No need to edit code beyond this point :) ##########

def main():
    age = int(input("How old is this person?: "))  # Prompt the user to enter an age
    print(is_adult(age))  # Call the is_adult function and print the result

if __name__ == "__main__":
    main()
