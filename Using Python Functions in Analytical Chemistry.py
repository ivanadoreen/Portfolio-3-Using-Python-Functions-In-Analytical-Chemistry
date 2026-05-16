print("""     
# PORTFOLIO 3: USING PYTHON FUNCTIONS IN ANALYTICAL CHEMISTRY
    Description: Calculates the volume of stock solution needed for a dilution.
    Concepts Used: Function Definitions (`def`)
    Parameters/Arguments
    Return Values (`return`)
""")

print("\n" + "="*50)
print("USING PYTHON FUNCTIONS IN ANALYTICAL CHEMISTRY")
print("="*50 + "\n")

# ---------------------------------------------------------
# FUNCTION DEFINITIONS
# ---------------------------------------------------------

def calculate_stock_volume(stock_molarity, target_molarity, target_volume):
    """
    Calculates the required volume of stock solution (V1).
    Takes 3 parameters and returns the final mathematical result.
    """
    required_volume = (target_molarity * target_volume) / stock_molarity
    return required_volume

def check_volume_practicality(volume_ml):
    """
    Takes the calculated volume parameter and uses conditionals to check 
    if it is practical to measure with standard lab equipment.
    Returns a string status.
    """
    if volume_ml < 0.1:
        return "Warning: Volume too small. Use a micropipette or serial dilution."
    elif volume_ml > 1000:
        return "Warning: Volume very large. Need bulk glassware."
    else:
        return "Status: Optimal volume for standard volumetric flasks and pipettes."

# ---------------------------------------------------------
# DILUTION CALCULATOR
# ---------------------------------------------------------
# Calculates the volume of stock solution needed using the M1V1 = M2V2 formula
print("\n# DILUTION CALCULATOR")

M1 = 12.0  # Stock concentration in Molar (M)
M2 = 0.5   # Desired concentration in Molar (M)
V2 = 250.0 # Desired final volume in mL

# Calling the first function and storing the return value in V1
V1 = calculate_stock_volume(M1, M2, V2)

# Calling the second function and passing V1 as the argument
practicality_status = check_volume_practicality(V1)

# --- RESULTS ---
print(f"Stock Solution (M1): {M1} M")
print(f"Target Solution (M2): {M2} M")
print(f"Target Volume (V2): {V2} mL")
print("-------------------------------------------------")
print(f"Required Stock Volume (V1): {round(V1, 2)} mL")
print(f"Equipment Check: {practicality_status}")
print("\n" + "="*50)