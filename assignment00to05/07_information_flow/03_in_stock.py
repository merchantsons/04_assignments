# 03_in_stock.py by merchantsons

def main():
    fruit = input("Enter a fruit: ")  # Prompt the user to enter a fruit
    stock = num_in_stock(fruit)  # Call num_in_stock to get the number of that fruit in stock
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# There is no need to edit code beyond this point

def num_in_stock(fruit: str) -> int:
    """
    This function returns the number of fruit Sophia has in stock.
    """
    inventory = {
        'apple': 2,
        'durian': 4,
        'pear': 1000
    }
    return inventory.get(fruit, 0)

if __name__ == '__main__':
    main()
