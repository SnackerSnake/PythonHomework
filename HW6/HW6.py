#Author: David Hernandez
#Description: This program asks the user for a certain amount of numbers to randomly
#generator between 1 and 500, and then the program writes them on a text file.

#This import allows the random number generation commands to be used in this program.
import random

#This print command explains the program to the user.
print("This program writes random numbers to the random.txt file.")

#This line asks the user to enter an amount of numbers to randomly generate.

amount_of_numbers = input("How many numbers would you like to write?:")

#This section of code opens the random text file to write on it, randomly generates numbers between
#1 through 500 in the amount of times set by the user, and then it writes those randomly generated numbers
#on the text file, and then it closes the file.
number_writing = open("random.txt","w")
for number_generation in range (int(amount_of_numbers)):
    number=random.randint(1,500)
    number_writing.write(str(number) + "\n")
number_writing.close()

#This line lets the user know that the specified amount of numbers were written on the text file.
print(amount_of_numbers , "numbers were written to the random.txt file.")
