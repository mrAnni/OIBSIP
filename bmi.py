def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_bmi(weight, height):
    return weight / (height * height)


def main():

    while True:
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))
            if weight <= 0:
                raise ValueError("Weight cannot be zero or negative.")
            height = float(input("Enter your height in meters (m): "))
            if height <= 0:
                raise ValueError("Height cannot be zero or negative.")
            break
        except ValueError as e:
            print("Error:", e)
            print("Please enter valid numerical values for weight and height.")

    bmi = calculate_bmi(weight, height)
    bmi_category_result = bmi_category(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {bmi_category_result}")


if __name__ == "__main__":
    main()
