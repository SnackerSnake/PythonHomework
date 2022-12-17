#Author: David Hernandez
#Description: This program draws polygons with different amount of sides for the user.

#Imports modules to use functions from modules turtle and random.
from turtle import *
from random import randint

# The makePolygon function draws a polygon with the number of sides,
# side length, border color, border width, and fill color as specified.
def make_polygon (sides, border_color, fill_color, width, length):

    #This command gets the pen to look like a turtle.
    shape("turtle")

    #These commands set the pen wifth, color, and the angle of each turn for the pen.
    pensize(width)
    pencolor("green")
    angle= 360/sides

    #These lines set the color of the polygon; begins filling the polygon.
    color(border_color)
    pencolor(fill_color)
    begin_fill()

    #This for loop draws each side of the polygon.
    for times in range(sides):
        pendown()
        forward(length)
        left(angle)

    #This part ends filling the polygon
    end_fill()

#This function randomly determines the color of the polygon.
def determine_color():

    #These lines allow these two variables to be used in the entire program.
    global border_color_wanted
    global fill_color_wanted

    #This list makes a list of colors.
    colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
              'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']

    #These commands randomly determine the color for the polygon based on the color list and a random number generator.
    random_color = randint(1, 12)
    border_color_wanted = colors[random_color]
    random_color = randint(1, 12)
    fill_color_wanted = colors[random_color]

#This print tells the user what the program does.
print("This program will draw a polygon with 3 or more sides. \n")

#This command asks the user how many sides he or she would like to draw for the polygon.
sides_wanted = int(input("Enter the number of sides, less than 3 to exit:"))

#If the user wants 3 or more sides, it will proceed with this section of the program.
if (sides_wanted>=3):

    #These lines determine the color, width, and length of the polygon based on calculations and chance.
    determine_color()
    width_wanted = (sides_wanted % 20) + 1
    side_length = 600 / sides_wanted

    #This line draws the polygon based off previous variables.
    make_polygon(sides_wanted, border_color_wanted, fill_color_wanted, width_wanted, side_length)

#This while loop continues the program until the user inputs an invalid amount of sides.
while (sides_wanted>=3):

    #This command asks the user how many sides he or she would like to draw for the polygon.
    sides_wanted = int(input("Enter the number of sides, less than 3 to exit:"))

    #This line clears the drawing board.
    reset()

    #If the user wants 3 or more sides, it will proceed with this section of the program.
    if (sides_wanted>=3):

        # These lines determine the color, width, and length of the polygon based on calculations and chance.
        determine_color()
        width_wanted = (sides_wanted % 20) + 1
        side_length = 600 / sides_wanted

        #This line draws the polygon based off previous variables.
        make_polygon(sides_wanted, border_color_wanted, fill_color_wanted, width_wanted, side_length)

#Thanks the user for using the program.
print("\n")
print("Thanks for using the polygon generator program.")