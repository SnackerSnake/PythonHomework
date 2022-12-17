#David Hernandez
#The purpose of this code is to calculate the discount for buying a certain amount of a software products.

#This part creates a function to round costs and discounts calculated later to 2 decimal places.
def get_two_decimals():
    global cost
    global discount
    cost = ("%.2f" % cost)
    discount = ("%.2f" % discount)

#This section asks the user for the quantity of software that they would like to buy.
package_quantity = round(abs(float(input("How many packages would you like to buy?:"))))
print("You bought", package_quantity, "packages.")

#These if-else statements calculate the discounts and costs for a certain amount of packages.
#They will check to see what quantity they're dealing with and determine the discounts and costs based off that.
#Then they will show the user the results.
if(package_quantity<10):
    discount = 0
    cost=package_quantity*100
    get_two_decimals()
    print("The total cost of your purchase was $" + str(cost) + " with a discount of $" + str(discount) +".")

elif(package_quantity<20):
    cost = package_quantity * 100
    discount = cost * .1
    cost = cost-discount
    get_two_decimals()

    print("The total cost of your purchase was $" + str(cost) + " with a discount of $" + str(discount) + ".")

elif (package_quantity < 50):
    cost = package_quantity * 100
    discount = cost * .2
    cost = cost - discount
    get_two_decimals()
    print("The total cost of your purchase was $" + str(cost) + " with a discount of $" + str(discount) + ".")

elif (package_quantity < 100):
    cost = package_quantity * 100
    discount = cost * .3
    cost = cost - discount
    get_two_decimals()
    print("The total cost of your purchase was $" + str(cost) + " with a discount of $" + str(discount) + ".")

elif (package_quantity >= 100):
    cost = package_quantity * 100
    discount = cost * .4
    cost = cost - discount
    get_two_decimals()
    print("The total cost of your purchase was $" + str(cost) + " with a discount of $" + str(discount) + ".")