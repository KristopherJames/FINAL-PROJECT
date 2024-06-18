#4.MEASUREMENT CONVERTER

def mm_to_cm(mm):
    return mm / 10

def cm_to_inches(cm):
    return cm / 2.54

def inches_to_feet(inches):
    return inches / 12

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_kilometers(meters):
    return meters / 1000

def display_menu():
    print("Measurement Converter")
    print("1. Millimeters to Centimeters")
    print("2. Centimeters to Inches")
    print("3. Inches to Feet")
    print("4. Feet to Meters")
    print("5. Meters to Kilometers")
    print("6. Exit")

def convert_units():
    while True:
        display_menu()
        choice = input("Choose a conversion option (1-6): ")

        if choice == "1":
            mm = float(input("Enter millimeters: "))
            print(f"{mm} mm is {mm_to_cm(mm)} cm\n")
        elif choice == "2":
            cm = float(input("Enter centimeters: "))
            print(f"{cm} cm is {cm_to_inches(cm)} inches\n")
        elif choice == "3":
            inches = float(input("Enter inches: "))
            print(f"{inches} inches is {inches_to_feet(inches)} feet\n")
        elif choice == "4":
            feet = float(input("Enter feet: "))
            print(f"{feet} feet is {feet_to_meters(feet)} meters\n")
        elif choice == "5":
            meters = float(input("Enter meters: "))
            print(f"{meters} meters is {meters_to_kilometers(meters)} kilometers\n")
        elif choice == "6":
            print("Exiting the converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

if __name__ == "__main__":
    convert_units()
