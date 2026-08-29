def calculate_bmi():
    try:

        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
           print("Weight and height must be greater than zero.")
           return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
              category = "Underweight"
        elif bmi < 25:
              category = "Normal"
        elif bmi < 30:
              category = "Overwight"
        else:
              category = "Obese"

        print(f"\n Your BMI is: {bmi:.2f}")  
        print(f"Category: {category}")

    except ValueError:
        print("Please enter valid numeric values.")   

calculate_bmi()          
