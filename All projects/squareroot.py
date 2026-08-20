Value = float(input("Enter a number: "))
if Value < 0:
    print("Error: Cannot compute the square root of a negative number.")
else:
    print("The square root of", Value, "is", Value ** 0.5)