#Author: David Hernandez

#This program asks the user for their height and weight to determine their BMI
#in order to tell if they have a healthy weight for their height.

#This part asks the user for their height and weight.
height = float(input("Enter your height in inches:"))
weight = float(input("Enter your weight in pounds:"))

#Line 11 calculates the BMI based on the given height and weight values.
BMI = (weight*703)/(height**2)

#This section tells the user their result based on the previous calculations,
#and it makes the conditions to distinguish between underweight, overweight, and normal.
if( BMI > 25):
    print("Your BMI is:", BMI)
    print("Your BMI indicates that you are overweight.")
elif(BMI<18.5):
    print("Your BMI is:", BMI)
    print("Your BMI indicates that you are underweight.")
else:
    print("Your BMI is:", BMI)
    print("Your BMI indicates that you have an optimal weight")
