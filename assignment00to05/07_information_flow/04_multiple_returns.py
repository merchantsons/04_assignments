# 04_multiple_returns.py by merchantsons

def get_user_info():
    """
    Prompts the user for their first name, last name, and email address,
    and returns these values as a tuple.
    """
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")

    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    user_data = get_user_info()  # Call get_user_info to get the user's information
    print("Received the following user data:", user_data)  # Print the returned tuple

if __name__ == "__main__":
    main()
