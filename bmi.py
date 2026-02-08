def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

try:
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
    else:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        print("Your BMI is:", round(bmi, 2))
        print("Category:", category)


except ValueError:
    print("Please enter valid values.")
