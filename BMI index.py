Weight = float(input("Enter weight in kg: "))
Height = float(input("Enter height in m2: "))

BMI= Weight/(Height*Height)

if BMI < 18.5:
    classification = "Underweight"
elif BMI <= 25:
    classification = "Normal"
elif BMI <= 30:
    classification = "Overweight"
elif BMI <= 35:
    classification = "Class I Obesity"
elif BMI <= 40:
    classification = "Class II Obesity"
elif BMI <= 45:
    classification = "Class III Obesity"
else:
    classification = "How are you still alive?"
print(f"Your BMI is: {BMI}, {classification}")