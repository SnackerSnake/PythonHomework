#Author: David Hernandez
#Description: This program reads popular names from a text files, puts them into a list, and allows users to
#search the ranking of each name.

def get_name_list(text_file):
    """Gets all the names from the parameter <text_file>.
    It will open the text file, search every name in the text file, add it to a list, and close the text file."""
    #Opens the text file.
    name_file = open(text_file, "r")

    #Searches for every name in the text file and adds it to a list.
    for name in name_file:
        name = name.rstrip("\n")
        name_list.append(name)

    #Closes the text file.
    name_file.close()

def check_name(name_want, gender):
    """Checks all the names from the parameter <name_list> and tells the user if the name that is input from
    name_want is found in the list. It also uses the parameter <gender> to distinguish the girls list and boys list."""
    #Defines variables to be used later in the for loop.
    name_found = 0
    name_rank = 0

#This loop will look for the name stated by the user in the name list. If it is found, its rank and name is recorded.
    for searched_name in range(len(name_list)):
        if (name_want == name_list[searched_name]):
            name_found = name_list[searched_name]
            name_rank = searched_name + 1

    #If the name is found in the name list, it will let the user know its rank. Otherwise, it will let the user know that the name's not on the name list.
    if (name_want == name_found):
        print(name_want, "is a popular", gender,"name and is ranked:", name_rank)
    else:
        print(name_want, "is not a popular", gender , "name.")
    name_list.clear()

#These lists are created to be later used in the program.
name_list = []

#These variables are created to be used for the gender parameters.
boys="boys"
girls="girls"

#This part tells the user how the program works.
print("Enter a name to see if it is a popular girls or boys name.\n")

#This input will ask the user if he or she wants to check each list of names or stop to finish the loop and then program.
name_want=input('Enter a name to check, or "stop" to stop:')

#As long the user does not type stop, this loop will keep going.
while name_want != "stop":

    # Gets the names from the girls text file.
    get_name_list("GirlNames.txt")

    # Checks the names from the girl name list.
    check_name(name_want, girls)
    #Gets the names from the boys text file.
    get_name_list("BoyNames.txt")

    #Checks the names from the boy name list.
    check_name(name_want, boys)

    # Repeated to ask the user if he or she keep searching for names on the lists or wants to stop.
    name_want = input('\n' + 'Enter a name to check, or "stop" to stop:')