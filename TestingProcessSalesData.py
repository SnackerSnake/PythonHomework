# Author: David Hernandez
# Description: Make an annual sales report from data files of salespeople's revenues
# from selling a company's products.

def get_IDs(filename):
    ID_file = open(filename, "r")

    ID_data_list = [line.strip() for line in ID_file.readlines()]
    sales_data_list = [[0.00, 0.00, 0.00, 0.00],
                       [0.00, 0.00, 0.00, 0.00],
                       [0.00, 0.00, 0.00, 0.00],
                       [0.00, 0.00, 0.00, 0.00],
                       [0.00, 0.00, 0.00, 0.00],
                       [0.00, 0.00, 0.00, 0.00]]

    ID_file.close()

    print(sales_data_list)
    print("")
    print(ID_data_list)

    return ID_data_list, sales_data_list


def process_sales_data(filename, id_list, sales_data):
    sales_data_file = open(filename, "r")

    sales_data_list_from_file = [line.strip() for line in sales_data_file.readlines()]

    sales_data_file.close()

    sales_data_list_sorted = sorted(sales_data_list_from_file)

    print("")
    print(sales_data_list_sorted)
    print("")
    print("")

    # How to add sales_data[1][1]=sales_data_list_sorted[1] print(sales_data) to list.

    # Initial ID for comparison
    ID_to_check = id_list[0]
    str(ID_to_check)

    # Initial place to add revenues to sales_data
    row = 0
    column = 0

    for element in range(len(sales_data_list_sorted)):
        # Convert element to string
        index = str(sales_data_list_sorted[element])
        # Compare IDs to see if the row is still the same
        ID = index[0:5]
        print(ID)
        if (ID_to_check != ID):
            ID_to_check = ID
            row += 1
        print(ID_to_check)
        print(row)

        # Remove ID from index
        quarter_and_revenue = index.replace(ID, "")
        print(quarter_and_revenue.lstrip())

        # Get quarter
        quarter = quarter_and_revenue[1:3]

        # Check quarter
        print(quarter)
        # if quarter is 1-4, first quarter which means first column, etc.
        if (int(quarter) >= 1 and int(quarter) <= 3):
            column = 0
        elif (int(quarter) >= 4 and int(quarter) <= 6):
            column = 1
        elif (int(quarter) >= 7 and int(quarter) <= 9):
            column = 2
        elif (int(quarter) >= 10 and int(quarter) <= 12):
            column = 3
        print(column)

        # Remove quarter and space
        revenue = quarter_and_revenue.replace(quarter, "")
        revenue = revenue.replace(" ", "")

        print(revenue)
        print(row)
        print(column)
        # Add element to sales_data_list based on which row and column
        if (sales_data[row][column] != 0.00):
            sales_data[row][column] = float(sales_data[row][column]) + float(revenue)
            sales_data[row][column] = round(sales_data[row][column], 2)
        else:
            sales_data[row][column] = float(revenue)
        print("")
        print(sales_data)


# Get quarter and ID for each amount of revenue.


def print_report(id_list, sales_data):
    sum_of_QT1 = 0
    sum_of_QT2 = 0
    sum_of_QT3 = 0
    sum_of_QT4 = 0

    # Display gathered data.
    print("")
    print("--------Annual Sales Report--------\n")
    print("ID\t\t\tQT1\t\t   QT2\t\t  QT3\t\t  QT4\t\tTotal")

    for salesperson in range(len(id_list)):
        print(id_list[salesperson],
              sales_data[salesperson][0],
              sales_data[salesperson][1],
              sales_data[salesperson][2],
              sales_data[salesperson][3],
              round(sum(sales_data[salesperson][:]), 2),
              sep="    ")

        sum_of_QT1 += sales_data[salesperson][0]
        sum_of_QT2 += sales_data[salesperson][1]
        sum_of_QT3 += sales_data[salesperson][2]
        sum_of_QT4 += sales_data[salesperson][3]

    sum_of_QT1 = round(sum_of_QT1, 2)
    sum_of_QT2 = round(sum_of_QT2, 2)
    sum_of_QT3 = round(sum_of_QT3, 2)
    sum_of_QT4 = round(sum_of_QT4, 2)

    sum_of_all_QTs = sum_of_QT1 + sum_of_QT2 + sum_of_QT3 + sum_of_QT4
    sum_of_all_QTs = round(sum_of_all_QTs, 2)

    print("Total\t", sum_of_QT1, sum_of_QT2, sum_of_QT3, sum_of_QT4, sum_of_all_QTs)

    # Calculate max profit by salesperson and quarter.
    # Get max quarter and salesperson revenue
    max_per_salesperson = []
    for salesperson in range(len(id_list)):
        # Make a list of each salesperson's largest revenue as second column with id as first column
        max_salesperson = max(sales_data[salesperson])
        print(max_salesperson)
        max_per_salesperson.append(max_salesperson)
        print(max_per_salesperson)

    total_max_of_salespeople = max(max_per_salesperson)
    id_of_max = max_per_salesperson.index(total_max_of_salespeople)

    print(id_of_max)
    print(total_max_of_salespeople)

    all_quarters_totals = [sum_of_QT1, sum_of_QT2, sum_of_QT3, sum_of_QT4]
    max_quarter = max(all_quarters_totals)
    which_quarter = all_quarters_totals.index(max_quarter)
    which_quarter += 1

    print(all_quarters_totals)
    print(max_quarter)
    print(which_quarter)

    print("Max amount by Salesperson is: ID = ", id_list[id_of_max], "Amount = ", total_max_of_salespeople)
    print("Max amount by Salesperson is: Quarter = ", which_quarter, "Amount = ", max_quarter)


def main():
    input_sales_IDs_list, input_sales_data_list = get_IDs(sales_IDs_input)

    process_sales_data(sales_data_input, input_sales_IDs_list, input_sales_data_list)

    print("")
    print(input_sales_data_list)
    print_report(input_sales_IDs_list, input_sales_data_list)


sales_IDs_input = input("Enter the name of the sales ids file:")
sales_data_input = input("Enter the name of the sales data file:")
main()

# print(sales_data[salesperson][quarter])
# print(amount_of_digits)
# print(extra_space[:])
# print("")
# print("")
# .format(sales_data[salesperson][0], '.2f')