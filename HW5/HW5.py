#Author: David Hernandez
#Description: This application asks the user for a list of Celsius degrees to turn into Fahrenheit in a time table.

#This part asks the user how many celsius degrees to convert into fahrenheit.
amount_of_conversions = int(input("Enter the amount of celsius temperatures to display: "))

#This line ets celsius to -1 so that it starts at 0 in the for loop.
celsius = -1

#This print command labels the numbers on the columns as Celsius and Fahrenheit.
print("Celsius\tFahrenheit")

#This loop uses the requested amount of celsius temperatures to convert them into fahrenheit.
#It will then print out the celsius and fahrenheit amounts side by side under the labels with one decimal place.
for i in range(amount_of_conversions+1):
    celsius += 1
    fahrenheit = 9 / 5 * celsius + 32
    fahrenheit = ("%.1f" % fahrenheit)
    print(celsius , "\t   " , fahrenheit)
