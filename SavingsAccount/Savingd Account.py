#Get info from user
print("I'll help you determine how long you will need to save.")
name = input("Hello! Enter your name so that we can get to know you. ")
print("Hello", name +"!")
goal = input("What would you like to save for? ")
print("Saving for a", goal, "is a wonderful idea!")
balance = float(input("Ok, "+ name + ". Please enter the cost of the "+ goal+ ": "))
if (balance<0):
    print("Looks like you already have saved enough!")
    balance = 0
    payment = 1
else:
    payment = float(input("Enter how much you will save each period:"))
if (payment<=0):
    payment = float(input("Savings must be positive. Please enter a positive number:"))
    if (payment<=0) :
        print(name+", you still didn't enter a postive number! I am going to assume you save 1 per period.")
        payment=1
#Calculate the number of payments required
number_of_remaining_payments = int(balance/payment)
if (number_of_remaining_payments < balance/payment):
    number_of_remaining_payments+= 1
#Present results to the user
print(name, "You will need to make", number_of_remaining_payments , "amount of payments to reach your goal.")
