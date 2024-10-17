def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    return celsius + 273


def kelvin_to_celsius(kelvin):
    return kelvin - 273


def temperature_converter():
    while True:
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Exit")

        choice = input("Enter the value you want to convert (1-5): ")

        if choice == '1':
            temp = float(input("Enter the Celsius temperature value: "))
            result = celsius_to_fahrenheit(temp)
            print(f"{temp} Celsius is equal to {result} Fahrenheit.")
        elif choice == '2':
            temp = float(input("Enter the Fahrenheit temperature value: "))
            result = fahrenheit_to_celsius(temp)
            print(f"{temp} Fahrenheit is equal to {result} Celsius.")
        elif choice == '3':
            temp = float(input("Enter the Celsius temperature value: "))
            result = celsius_to_kelvin(temp)
            print(f"{temp} Celsius is equal to {result} Kelvin.")
        elif choice == '4':
            temp = float(input("Enter the Kelvin temperature value: "))
            result = kelvin_to_celsius(temp)
            print(f"{temp} Kelvin is equal to {result} Celsius.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Please enter a valid option between 1 and 5.")

temperature_converter()