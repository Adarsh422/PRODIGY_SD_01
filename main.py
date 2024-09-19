#Build a Temperature Conversion Program Function to convert Celsius to Fahrenheit and Kelvin
def celsius_to_other(temp_c):
    temp_f = (temp_c * 9/5) + 32  # Celsius to Fahrenheit
    temp_k = temp_c + 273.15       # Celsius to Kelvin
    return temp_f, temp_k

# Function to convert Fahrenheit to Celsius and Kelvin
def fahrenheit_to_other(temp_f):
    temp_c = (temp_f - 32) * 5/9   # Fahrenheit to Celsius
    temp_k = (temp_f - 32) * 5/9 + 273.15  # Fahrenheit to Kelvin
    return temp_c, temp_k

# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_to_other(temp_k):
    temp_c = temp_k - 273.15       # Kelvin to Celsius
    temp_f = (temp_k - 273.15) * 9/5 + 32  # Kelvin to Fahrenheit
    return temp_c, temp_f

# Main function to handle user input and display conversions
def temperature_conversion():
    # Prompt user for input temperature and unit
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the original unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == 'C':
        temp_f, temp_k = celsius_to_other(temp)
        print(f"{temp}°C is equal to {temp_f:.2f}°F and {temp_k:.2f}K")
    elif unit == 'F':
        temp_c, temp_k = fahrenheit_to_other(temp)
        print(f"{temp}°F is equal to {temp_c:.2f}°C and {temp_k:.2f}K")
    elif unit == 'K':
        temp_c, temp_f = kelvin_to_other(temp)
        print(f"{temp}K is equal to {temp_c:.2f}°C and {temp_f:.2f}°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

# Run the temperature conversion program
temperature_conversion()
