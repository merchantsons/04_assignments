# 01_fibonacci.py by merchantsons

MAX_TERM_VALUE = 10000

def main():
    a, b = 0, 1  # Initialize first two terms: Fib(0) = 0, Fib(1) = 1
    while a <= MAX_TERM_VALUE:
        print(a, end=" ")
        a, b = b, a + b  # Update to next pair of terms

if __name__ == '__main__':
    main()