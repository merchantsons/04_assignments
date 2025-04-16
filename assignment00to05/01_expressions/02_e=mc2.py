C: int = 299792458  # The speed of light in m/s

def main():
    # Prompt user for mass and convert to float
    mass_in_kg: float = float(input("Enter kilos of mass: "))
    
    # Calculate energy using E = m * c^2
    energy_in_joules: float = mass_in_kg * (C ** 2)
    
    # Display the calculation steps and result
    print("e = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")

if __name__ == '__main__':
    main()