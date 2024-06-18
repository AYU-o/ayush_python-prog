def cm_to_feet_inches(cm):
    inches = cm / 2.54
    feet = inches // 12
    remaining_inches = inches % 12
    return feet, remaining_inches

# Input from user
cm = float(input("Enter the length in centimeters: "))

# Conversion
feet, inches = cm_to_feet_inches(cm)

# Output
print(f"{cm} cm is equal to {int(feet)} feet and {inches} inches.")
