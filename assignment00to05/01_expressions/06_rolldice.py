# 06_rolldice.py
import random  # Import random library for dice simulation

NUM_SIDES: int = 6  # Number of sides on each die

def main():
    # Simulate rolling two dice
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Calculate total
    total: int = die1 + die2
    
    # Print results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    main()