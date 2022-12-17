#Author: David Hernandez
#Description: The program will ask the user to enter a number n.
#Then, it will ask the user to enter different numbers one time less than the entered number.
#The program will then determine which number is missing between 1 and the entered.

#Asks the user to insert a number.
number = int(input("Enter n: "))

#Variables created to calculate the missing number later.
#Inferior numbers is the numbers less than the given number by the user but greater than 0.
#List of possibilities is the total of the inferior numbers and entered/given number by the user.
inferior_number = number
list_of_possibilities = number

#The first loop adds all numbers between 1 and the entered number.
for addition in range(number):
    inferior_number-=1
    list_of_possibilities += inferior_number

#The second loop will subtract unique numbers from a list given by the user.
#It will simultaneously determine the missing number in that list.
for subtraction in range (number-1):
    eliminate=input("Please enter a unique number between 1 and " + str(number) + ": ")
    list_of_possibilities-=float(eliminate)

#This line lets the program tell the user the missing number from the list given earlier.

print("The missing number is:", float(round(list_of_possibilities)))
