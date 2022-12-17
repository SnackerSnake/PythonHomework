#Author: David Hernandez
#Description: This program make an annual sales report from data files of salespeople's revenues from selling a company's products.

#This function creates two list, one with ids and another blank 2d list.
def get_IDs(filename):

    #This line opens the file of ids.
    ID_file = open(filename, "r")

    #It reads the ids and puts them in a list.
    ID_data_list = [line.strip() for line in ID_file.readlines()]

    #This puts the list in order.
    ID_data_list.sort()

    #These lines create a 2d list that creates a blank space to put the sales data later.
    sales_data_list=[]
    for line in range(len(ID_data_list)):
        sales_data_list.append([0.00,0.00,0.00,0.00])

    #This closes the file.
    ID_file.close()

    #This line returns the values wanted for the main program.
    return ID_data_list, sales_data_list

#This function adds values to the 2d blank list from the sales list.
def process_sales_data(filename, id_list, sales_data):

    # This line opens the file of sales.
    sales_data_file = open(filename, "r")

    #This reads each line in the file and adds each line to the blank list.
    sales_data_list_from_file = [line.strip() for line in sales_data_file.readlines()]

    #This part closes the file.
    sales_data_file.close()

    #This line created a sorted list.
    sales_data_list_sorted = sorted(sales_data_list_from_file)

    #How to add sales_data[1][1]=sales_data_list_sorted[1] print(sales_data) to list.

    #Initial ID for comparison
    ID_to_check = id_list[0]
    str(ID_to_check)

    #Initial place to add revenues to sales_data
    row=0
    column=0

    #This loop checks each part of the sorted 2d list.
    for element in range(len(sales_data_list_sorted)):

        #Convert element to string
        index=str(sales_data_list_sorted[element])
        #Compare IDs to see if the row is still the same
        ID=index[0:5]

        #If a new ID is found, the data is place in the next row of the 2d list.
        if(ID_to_check!=ID):
            ID_to_check=ID
            row+=1

        #Remove ID from index
        quarter_and_revenue = index.replace(ID,"")

        #Get quarter
        quarter=quarter_and_revenue[1:3]

        #If quarter is 1-4, first quarter which means first column, etc.
        if(int(quarter)>=1 and int(quarter)<=3):
            column=0
        elif(int(quarter)>=4 and int(quarter)<=6):
            column=1
        elif (int(quarter) >=7 and int(quarter) <= 9):
            column = 2
        elif (int(quarter) >= 10 and int(quarter) <= 12):
            column = 3

        #Remove quarter and space
        revenue=quarter_and_revenue.replace(quarter,"")
        revenue = revenue.replace(" ", "")

        #Adds element to sales_data_list based on which row and column determined earlier in the loop.
        if(sales_data[row][column]!=0.00):
            sales_data[row][column]=float(sales_data[row][column])+float(revenue)
            sales_data[row][column]=round(sales_data[row][column], 2)
        else:
            sales_data[row][column]=float(revenue)

#Prints the annual sales report.
def print_report(id_list, sales_data):
    #This starts each quarter at 0.
    sum_of_QT1 = 0
    sum_of_QT2 = 0
    sum_of_QT3 = 0
    sum_of_QT4 = 0

    #Display gathered data, starting with the heading.
    print("")
    print("--------Annual Sales Report--------\n")
    print("ID\t\t\tQT1\t\t   QT2\t\t  QT3\t\t  QT4\t\t  Total")

    #Loops for each id in the id_list.
    for salesperson in range(len(id_list)):

        #This creates a blank list for later to make blank spaces in the report.
        extra_space=[]

        #Checks all 4 quarters
        for quarter in range(4):

            #Gets a number from the sales data and sets the digits counted to 0.
            test_number=sales_data[salesperson][quarter]
            amount_of_digits = 0

            #Counts the digit of the number from the sales data.
            while(test_number>0):

                test_number=test_number//10
                amount_of_digits+=1

            #Appropriately gives each number the amount of spaces they need when printing out the Annual Sales Report.
            if(amount_of_digits==0):
                extra_space.append("   ")
            elif(amount_of_digits==3):
                extra_space.append(" ")
            elif(amount_of_digits==2):
                extra_space.append("  ")
            elif(amount_of_digits == 1):
                extra_space.append(" ")
            elif(amount_of_digits==4):
                extra_space.append("")

        # Prints each id and revenue in an order based off their position in the list.
        print(id_list[salesperson],
        extra_space[0],
        '%.2f'%sales_data[salesperson][0],
        extra_space[1],
        '%.2f'%sales_data[salesperson][1],
        extra_space[2],
        '%.2f'%sales_data[salesperson][2],
        extra_space[3],
        '%.2f'%sales_data[salesperson][3],
        "\t",
        '%.2f'%round(sum(sales_data[salesperson][:]),2),
            sep="  ")

        #Adds each quarter's revenue into a sum.
        sum_of_QT1 += sales_data[salesperson][0]
        sum_of_QT2 += sales_data[salesperson][1]
        sum_of_QT3 += sales_data[salesperson][2]
        sum_of_QT4 += sales_data[salesperson][3]

    #Rounds each quarter.
    sum_of_QT1 = round(sum_of_QT1, 2)
    sum_of_QT2 = round(sum_of_QT2, 2)
    sum_of_QT3 = round(sum_of_QT3, 2)
    sum_of_QT4 = round(sum_of_QT4, 2)

    #Adds all the quarters and rounds the value.
    sum_of_all_QTs = sum_of_QT1+sum_of_QT2+sum_of_QT3+sum_of_QT4
    sum_of_all_QTs = round(sum_of_all_QTs, 2)

    #Prints the sum of each quarter and their combined total.
    print("Total  ", '%.2f'%sum_of_QT1+ "  ", '%.2f'%sum_of_QT2,  "\t"+ '%.2f'%sum_of_QT3, "  "+ '%.2f'%sum_of_QT4, "\t "+ '%.2f'%sum_of_all_QTs, sep="  ")
    print("")
    #Makes a blank list.
    max_per_salesperson = []

    #Checks each id's maximum revenue and puts it into the blank list above.
    for salesperson in range(len(id_list)):
        # Make a list of each salesperson's largest revenue as second column with id as first column
        max_salesperson = max(sales_data[salesperson])
        max_per_salesperson.append(max_salesperson)

    #Finds the maximum revenue from the modified list and which id got that value.
    total_max_of_salespeople = max(max_per_salesperson)
    id_of_max = max_per_salesperson.index(total_max_of_salespeople)

    #Makes a list of the sum of each quarter, determines what the most revenue was for a quarter, and finds which qurter made the most revenue.
    all_quarters_totals = [sum_of_QT1, sum_of_QT2, sum_of_QT3, sum_of_QT4]
    max_quarter = max(all_quarters_totals)
    which_quarter = all_quarters_totals.index(max_quarter)
    which_quarter += 1

    #Prints quarter with the most revenue, the id with the most revenue, and how much for each.
    print("Max sales by Salesperson is: ID = ", str(id_list[id_of_max]) +"," , "Amount = $" + str(total_max_of_salespeople))
    print("Max sales by Quarter is: Quarter = ", str(which_quarter) +"," , "Amount = $" + str(max_quarter))

#This function does the rest of the program.
def main():

    #This line creates two lists, one for ids and another blank 2d one.
    input_sales_IDs_list, input_sales_data_list = get_IDs(sales_IDs_input)

    #This line adds values to the 2d blank list.
    process_sales_data(sales_data_input, input_sales_IDs_list, input_sales_data_list)

    #This function prints the entire sales report.
    print_report(input_sales_IDs_list, input_sales_data_list)

#These lines ask the user to input the data files that the user wants the program to work with.
sales_IDs_input = input("Enter the name of the sales ids file:")
sales_data_input = input("Enter the name of the sales data file:")

#This function does the rest of the program.
main()