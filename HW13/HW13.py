#Author: David Hernandez
#Description: This program finds the average and sum of a given list of numbers by the user.

def calculate_average(sum,count):
    """This function calculates the average of the parameter [sum] by dividing it by the parameter [count]."""
    global average
    try:
        if (count==0):
            raise ValueError
        average = sum /count
        return average
    except ValueError:
        print("What you entered was not a valid number. Try again.")

#Defines variables to be used later in the program or functions above.
number=0
sum_of_numbers=0
count_of_numbers=0
average=0
test=0

#Continues the loop as long the user inputs positive values.
while (number >= 0):

    #Continues the loop until break is reached.
    while (True):

        #Check for errors.
        try:
            #Asks the user to input a number. Positive continues the program. Negative lets the program move on to calculating the results.
            number = int(input("Enter a positive number to the total or a negative number to calculate the average: "))

            #Adds values by the user into the sum and counts each input.
            if (number >= 0):
                sum_of_numbers += float(number)
                count_of_numbers += 1

            #Divides the sum of numbers by the amount put to check the except 2nd condition.
            test = sum_of_numbers / count_of_numbers

            #Stops the loop.
            break

        #Checks to see if the user input a number and not a word.
        except ValueError:
            print("What you entered was not a valid number. Try again.")

        #Checks to see if the user actually entered any numbers.
        except ZeroDivisionError:
            print("You did not enter any numbers to average.")

#Calculates the average of the given numbers by the user.
calculate_average(sum_of_numbers, count_of_numbers)


#This section tells the sum and average to the user in a neat format.
average=("%.1f" % average)
sum_of_numbers=("%.1f" % sum_of_numbers)
str(average)
str(sum_of_numbers)
print("The sum of the numbers is: " + sum_of_numbers)
print("The average of the numbers is: " + average)
