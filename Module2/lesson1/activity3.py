print("Select your vehicle type:")
print("1. Car")
print("2. Bike")

vehicle_type = int(input("Enter your choice (1 or 2): "))
if vehicle_type == 1:
    print("You have selected Car.")
    car_type = input("Enter the type of car (Supercar/Hypercar): ").strip()
    if car_type == "Supercar":
        print("You have selected a Supercar.")
    elif car_type == "Hypercar":
        print("You have selected a Hypercar.")
    else:
        print("Invalid car type selected.")

elif vehicle_type == 2:
    print("You have selected Bike.")
    bike_type = input("Enter the type of bike (Superbike/Classic): ").strip()
    if bike_type == "Superbike":
        print("You have selected a Superbike.")
    elif bike_type == "Classic":
        print("You have selected a Classic bike.")
    else:
        print("Invalid bike type selected.")