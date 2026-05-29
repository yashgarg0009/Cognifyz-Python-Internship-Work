# Task: Temperature Conversion
# Create a Python program that converts temperatures
# between Celsius and Fahrenheit.
# Prompt the user to enter a temperature value and
# the unit of measurement, and then display the
# converted temperature.

temperature = float(input("Enter temperature value: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C = {fahrenheit:.2f}°F")
elif unit == "F":
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F = {celsius:.2f}°C")
else:
    print("Invalid unit! Please enter C or F.")