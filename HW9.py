#Author: David Hernandez
#Description: This program reads popular names from a text files, puts them into a list, and allows users to
#search the ranking of each name.

#These lists are created to be later user in the program.
list_of_boys=[]
list_of_girls=[]

#These variables are created to be later user in the program.
name_found=0
name_rank=0
name_found_second=0
name_rank_second=0

#This part opens and reads each line in text the file. The names for boys are then put into a list. The file is then closed.
boy_file = open("BoyNames.txt", "r")

for name in boy_file:
    name = name.rstrip("\n")
    list_of_boys.append(name)

boy_file.close()

#This part opens and reads each line in text the file. The names for girls are then put into a list. The file is then closed.
girl_file = open("GirlNames.txt", "r")

for name in girl_file:
    name = name.rstrip("\n")
    list_of_girls.append(name)

girl_file.close()

#This part tells the user how the program works.
print("Enter a name to see if it is a popular girls or boys name.\n")

#This input will ask the user if he or she wants to check each list of names or stop to finish the loop and then program.
name_want=input('Enter a name to check, or "stop" to stop:')

#As long the user does not type stop, this loop will keep going.
while name_want!="stop":

        #This loop will look for the name stated by the user in the girls' list. If it is found, its rank and name is recorded.
        for searched_name in range(len(list_of_girls)):
            if (name_want==list_of_girls[searched_name]):
                name_found=list_of_girls[searched_name]
                name_rank=searched_name+1

        #If the name is found in the girls' list, it will let the user know its rank. Otherwise, it will let the user know that the name's not on the list for girls.
        if (name_want == name_found):
            print(name_want, "is a popular girls name and is ranked:", name_rank)
        else:
            print(name_want, "is not a popular girls name.")

        #This loop will look for the name stated by the user in the boys' list. If it is found, its rank and name is recorded.
        for searched_name in range(len(list_of_boys)):
            if (name_want==list_of_boys[searched_name]):
                name_found_second=list_of_boys[searched_name]
                name_rank_second=searched_name+1

        #If the name is found in the boys' list, it will let the user know its rank. Otherwise, it will let the user know that the name's not on the list for boys.
        if (name_want == name_found_second):
            print(name_want, "is a popular boys name and is ranked:", name_rank_second)
        else:
            print(name_want, "is not a popular boys name.")

        #Repeated to ask the user if he or she keep searching for names on the lists or wants to stop.
        name_want = input('\n' + 'Enter a name to check, or "stop" to stop:')