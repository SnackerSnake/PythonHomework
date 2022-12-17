#Author: David Hernandez
#Description: This program calculates windchill from the user's input of fahrenheit temperature and wind speed in a GUI format.

#Defines a variable to later be used in the loop.

calculate_another="y"

def getData():
    """Gets values from the user.
    Defines variables temperature and wind_speed from the user's input."""
    global temperature
    global wind_speed
    temperature = input("\nEnter the fahrenheit temperature:")
    wind_speed = input("Enter the wind speed:")
    return temperature
    return wind_speed

def calculateData(temperature, wind_speed):
    """This function calculates the windchill variable from the entered values of
    parameters <temperature, wind_speed> from the function 'getData'."""
    global windchill
    windchill = 35.74 + 0.6215 * int(temperature) - 35.75 * int(wind_speed) ** 0.16 + 0.4275 * int(temperature) * int(
        wind_speed) ** 0.16
    windchill = ("%.1f" % windchill)
    return windchill

#Tells the user what the program does.
print("This program calculates the windchill from fahrenheit temperature and wind speed.")

#Continues the program as long as the user enters y or ends the program when the user enters n.
while calculate_another == "y":

    #Gets input from the user to give values to temperature and wind_speed.
    getData()

    #Takes the input from the previous function to calculate the variable windchill.
    calculateData(temperature, wind_speed)

    #Tells the user the windchill from the given temperature and wind_speed.
    print("The windchill is:", windchill, "\n")

    #Continues the program as long as the user enters y or ends the program when the user enters n.
    calculate_another=input("Would you like to calculate another windchill? Enter y for yes or n for no:")
    while(calculate_another!="y" and calculate_another!="n"):
        calculate_another = input("Would you like to calculate another windchill? Enter y for yes or n for no:")
    if(calculate_another=="n"):
        quit()
