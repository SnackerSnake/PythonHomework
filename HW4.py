#Author: David Hernandez
#Description: This program finds the average grade of a given list of grades.

#These variables are defined to be used later in the calculations and storage of grades.
i=0
how_many_grades=0
total_of_grades=0

#This while and if statement get the test scores from the user and stores them to later be calculated.
while (i!=-1):
    i = float(input("Enter a test score; put -1 to find the average: "))
    if(i!=-1):
        total_of_grades += i
        #print("") (Comments 14,15,17,and 18 were used during testing.)
        #print("The grade total so far is", total_of_grades)
        how_many_grades += 1
        #print("The current amount of grades is:", how_many_grades)
        #print("")

#This line calculates the grade average with the stored values.
grade_average=total_of_grades/how_many_grades

#This section tells the grade average to the user in the desired format.
grade_average=("%.1f" % grade_average)
str(grade_average)
print("The average for all the grades is: " + grade_average)