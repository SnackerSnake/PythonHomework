#Lab #2
#Due Date: 09/06/2019, 11:59PM 
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement:
# Course Material
# How to Program: Computer Science Concepts and Python Exercises (to learn lists of lists syntax)
#
########################################

#Removes none letters from a string.
def removePunctuation(txt):

    #Starts off the variables for the function.
    statement=("")

    #Checks to see if the input is a string in the first place.
    if type(txt)==str:

        #Goes through every character in the string.
        for character in txt:

        #Gets rid of numbers and replaces them with blanks.
            if character.isdigit():
                statement+=" "
                continue

        #Adds all letters to the final result.
            if character.isalpha():
                statement+=character

        #Replaces any character not a letter with a blank.
            if not character.isalpha():
                statement += " "
        print(statement)

        #Returns the original text with every alphabet with spaces where there were no alphabets.
        return statement

    #Returns none if the input was not a string.
    else:
        return None



"""
    >>> removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
    'I like chocolate cake      It s the best flavor      for real'
    >>> removePunctuation("Dots...................... many dots..X")
    'Dots                       many dots  X'
    >>> removePunctuation(55)
    >>> removePunctuation([3.5,6])
"""

#Gets the averages of the submitted grade list.
def studentGrades(grade_list):

    #Sets the variables needed for future checks.
    skip_first_list=0
    result_list=[]
    do_not_return = 0
    individual_grade_index=0
    which_list=1

    #Checks to see if the input is a list in the first place.
    if type(grade_list)==list:
        for one_list_of_many_lists_of_grades in grade_list:

            #Skips the first list because it's just a descriptive header.
            if skip_first_list==0:
                skip_first_list+=1
                continue

            #Checks each grade for each list inside the giant list.
            for individual_grade in one_list_of_many_lists_of_grades:

                individual_grade = grade_list[which_list][individual_grade_index]

                #Skips the name of the students.
                if not type(individual_grade)==int:

                    one_list_of_many_lists_of_grades.pop(individual_grade_index)
                    individual_grade_index+=1

            #Moves on to the next grade to check.
            individual_grade_index -= 1
            which_list+=1

            #Adds the mean of the grades' of one student to the list of averages.
            result_list.append(int(sum(one_list_of_many_lists_of_grades) / len(one_list_of_many_lists_of_grades)))

    #Returns none if the input was not a list.
    else:
        do_not_return+=1
        return None

    #If the input was a list, it returns the results of the computations.
    if do_not_return==0:
        return result_list

"""
    >>> grades = [
    ...     ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
    ...     ['John', 100, 90, 80],
    ...     ['McVay', 88, 99, 111],
    ...     ['Rita', 45, 56, 67],
    ...     ['Ketan', 59, 61, 67],
    ...     ['Saranya', 73, 79, 83],
    ...     ['Min', 89, 97, 101]]
    >>> studentGrades(grades)
    [90, 99, 56, 62, 78, 95]
    >>> grades = [
    ...     ['Student', 'Quiz 1', 'Quiz 2'],
    ...     ['John', 100, 90],
    ...     ['McVay', 88, 99],
    ...     ['Min', 89, 97]]
    >>> studentGrades(grades)
    [95, 93, 93]
    >>> studentGrades(55)
    >>> studentGrades('32')
"""

removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
removePunctuation("Dots...................... many dots..X")
removePunctuation(55)
removePunctuation([3.5,6])