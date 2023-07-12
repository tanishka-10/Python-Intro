cel_temp = int(input("What is the temperature in celsius?"))
def fahrenheit(cel_temp):
    return(18 * cel_temp + 320) / 10


print("The Fahrenheit equivalent of " + str(cel_temp) + " degrees Celsius is " + str(fahrenheit(cel_temp)) + ".")


