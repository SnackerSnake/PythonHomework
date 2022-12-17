#Author: David Hernandez
#Description: This program reads the numbers from the random.txt file and prints the numbers,
#their sum, and the total amount of numbers.

#This line tells the user a message that the numbers below were read from the file.
print("The following numbers were read from the random.txt file:")

#This part establishes variables to be used later in the code.
amount_of_numbers=0
total_numbers=0

#Opens the random.txt file.
number_file = open("random.txt", "r")

#Reads each line of code in the file.
for linefromfile in number_file:

#This part tells the user the numbers and calculates the total amount of numbers and their sum.
    print(linefromfile)
    amount_of_numbers+=1
    total_numbers+=float(linefromfile)

#Closes the random.txt file.
number_file.close()

#This section tells the value of all numbers added together and how many numbers there were.
print("The total number is:", total_numbers)
print("The file contained:", amount_of_numbers)
