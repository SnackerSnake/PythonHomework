#David Hernandez
#Description: The user enters a certain amount of time in seconds, and then this program will calculate the distance,
#measured in meters, an object will fall in that amount of time.

#Creates a variable to define gravity.
gravity=9.8

#Creates a variable for time.
time=0

def falling_distance(time):
    """Calculates distance with a displacement equation.
    Creates a variable called "distance", getting the value of an equation by calculating it for parameter <time>.
    If a negative value is entered, the program will end."""
    if int(time)>=0:
        distance = .5 * gravity * int(time)** 2
        int(distance)
    else:
        quit()
    return int(distance)

#Tells the user what the program does.
print("This program tells you how far an object will fall in a number of second. Enter a negative number to quit.\n")

#Continues the program while time is greater than or equal to 0.
while (int(time)>=0):
    # Asks the user to enter the time for the falling distance in seconds.
    time = input("Enter the falling time in seconds:")
    #Tells the user how far the object will fall for the given time.
    print("The distance the object will fall in",  time, "seconds is:", float(falling_distance(time)), "meters. \n")
