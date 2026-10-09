weight_unit = str(input("Enter weight unit you prefer in lower case: "))
if weight_unit == "kilograms":
    print("You have chosen kilograms as your weight unit.")
elif weight_unit == "pounds":
    print("You have chosen pounds as your weight unit.")
elif not weight_unit == "kilograms" and not weight_unit == "pounds":
    print("You have not chosen a valid weight unit.")

if weight_unit == "kilograms":
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in feet: "))

    bmi = weight / ((height*0.3048) ** 2)  # Convert feet to meters

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 24.9:
        print("You are normal weight.")
    else:
        print("You are overweight.")

elif weight_unit == "pounds":
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in feet: "))

    bmi = (weight*0.45359237 / ((height*0.3048) ** 2))  # Convert feet to meters

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 24.9:
        print("You are normal weight.")
    else:
        print("You are overweight.")