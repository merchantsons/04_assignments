# 05_rendom_numbers.py by merchantsons

import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=' ')
    print()  # To move to the next line after printing the numbers

if __name__ == '__main__':
    main()
