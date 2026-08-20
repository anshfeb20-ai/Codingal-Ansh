Temp = float(input("Enter the temperature in Celsius: "))
Mood = input("Enter your mood (fashionable/practical): ")
if Temp < 0:
    if Mood == "fashionable":
        print("Wear a stylish coat and scarf with pants!")
    elif Mood == "practical":
        print("Wear a warm jacket and gloves with waterproof pants!")
if 0 <= Temp < 25:
    if Mood == "fashionable":
        print("Wear a light jacket open with a t-shirt inside and cargo pants!")
    elif Mood == "practical":
        print("Wear a full sweater and warm pants!")
if 25 <= Temp:
    if Mood == "fashionable":
        print("Wear a half-sleeve shirt and knee-length pants!")
    elif Mood == "practical":
        print("Wear a light shirt and shorts!")
