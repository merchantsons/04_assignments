def main():
    # Outer scope variables
    roll_count = 3
    
    print("Simulating rolling two dice, three times:")
    
    # Perform three rolls
    for i in range(roll_count):
        # Inner scope variables - new ones created each loop
        die1 = roll_die()  # First die roll
        die2 = roll_die()  # Second die roll
        total = die1 + die2
        
        # Print results for this roll
        print(f"Roll {i + 1}: Die 1 = {die1}, Die 2 = {die2}, Total = {total}")
    
    # If we tried to print die1 here, it would work because it's still in main's scope
    # print(die1)  # This would show the last roll's value
    
    # But we can't access 'result' from roll_die() here - it's out of scope
    # print(result)  # This would cause an error

def roll_die():
    # This function has its own scope
    result = random.randint(1, 6)  # Generate random number 1-6
    return result

# Need to import random for dice rolling
import random

if __name__ == '__main__':
    main()