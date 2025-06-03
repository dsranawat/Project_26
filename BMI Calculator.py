def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
def main():
    try:
        weight = float(input("Enter your weight (kg): "))
        height_cm = float(input("Enter your height (cm): "))
        bmi = calculate_bmi(weight, height_cm)
        category = classify_bmi(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()