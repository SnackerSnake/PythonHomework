#LAB 11
#Due Date: 11/22/2019, 11:59PM
########################################
#                                      
# Name: David Hernandez
# Collaboration Statement: Course Material
#
########################################


def selectionSort(numList):
    # Checks if the input is a list.
    if type(numList)==list:
        pass
    else:
        return None

    # Defines variables to use later.
    multiple_sorts={1: numList[:]}
    total=len(numList)

    # Checks the input X amount of times, X equal to its length (except the first).
    for index in range(total-1):

        # A variable to use later.
        lowest_value=numList[index]
        store_jindex = index

        # Checks every number in the input.
        for jindex in range(index, total):

            #Looks for the lowest value.
            if numList[jindex]<lowest_value:
                lowest_value=numList[jindex]
                store_jindex=jindex

        # Swaps the lowest number with the left most index that has not changed.
        # (I also tried the video way of checking two numbers next to each other repeatly,
        # but then I couldn't figure out of how to get the minimum value that way. So I did this.)
        numList[index], numList[store_jindex]= numList[store_jindex], numList[index]

        # Adds the passing to the final result.
        multiple_sorts[index+2]=numList[:]

    #Output
    return multiple_sorts, numList



'''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of selection sort
        2nd returned value: the sorted list

        >>> selectionSort([9,3,5,4,1,78,67])
        ({1: [9, 3, 5, 4, 1, 78, 67], 2: [1, 3, 5, 4, 9, 78, 67], 3: [1, 3, 5, 4, 9, 78, 67], 4: [1, 3, 4, 5, 9, 78, 67], 5: [1, 3, 4, 5, 9, 78, 67], 6: [1, 3, 4, 5, 9, 78, 67], 7: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
'''