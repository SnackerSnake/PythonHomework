#Author: David Hernandez
#Description: This program reads and displays the random text file, and the program also analyzes the file for its minimum, maximum, total, and average values.

###Get Data###

#Creates a list to store numbers in.
list_of_numbers = []

#This line opens the random.txt file to read.
number_file = open("random.txt", "r")

#This line tells the user that the numbers shown are the ones read from the text file.
print("The following numbers were read from the random.txt file:")

#Reads each line in the file.
for linefromfile in number_file:

    #These lines display each number and then put them into the list.
    print(int(linefromfile))
    list_of_numbers.append(int(linefromfile))

#This line closes the random.txt file.
number_file.close()

###Analyze Data and Show Results###

#These commands display the minimum, maximum, total, and average values to the user.
print("The lowest number in the list is:", min(list_of_numbers))
print("The highest number in the list is", max(list_of_numbers))
print("The total of the numbers is:", sum(list_of_numbers))
if len(list_of_numbers)>0:
    print("The average of the numbers in the list is:", "%.1f" % int(sum(list_of_numbers)/len(list_of_numbers)))
