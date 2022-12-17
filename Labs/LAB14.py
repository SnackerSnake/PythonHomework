#Lab #14
#Due Date: 12/13/2019, 11:59PM
########################################
#                                      
# Name: David Hernandez
# Collaboration Statement:
#https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
########################################


def genInf(aList):
    #Starts at -1
    counter=-1

    #Always runs when being called.
    while(counter!=-2):

        #If the whole list has been yielded, then the variable counter returns to the start.
       if(counter==len(aList)-1):
            counter=-1

        #Adds one to counter.
       counter+=1

        #Outputs the result.
       yield aList[counter]

'''
        >>> g = genInf([5,'a',2])
        >>> next(g)
        5
        >>> next(g)
        'a'
        >>> next(g)
        2
        >>> next(g)
        5
        >>> next(g)
        'a'
        >>> next(g)
        2
'''


def genFilter(seq, fn):
    #For every part of the generator.
    for index in seq:

        #If function is true for the index.
        if fn(index) == True:

            #Return the index in the true part.
            yield index
""" 
        >>> isEven = lambda x: x % 2 == 0 
        >>> list(genFilter(range(5), isEven)) 
        [0, 2, 4]
        >>> oddNum = (2*i-1 for i in range (10)) 
        >>> list(genFilter(oddNum, isEven)) 
        []
        >>> g = genFilter(range(1,11), isEven) 
        >>> next(g) 
        2
        >>> next(g) 
        4
        >>> next(g) 
        6
        >>> next(g) 
        8
        >>> next(g) 
        10
        >>> next(g) 
        Traceback (most recent call last):
        ...
        StopIteration
"""

def genAccum(seq, fn):
    #Goes through the entire generator list.
    for index in iter(seq):
        # Deals with the second part of the generator list.
        if (index-1)==1:
            #Defines previous,being the index before, and outputs the next index's calculation.
            previous=fn(total, seq[index - 1])
            yield fn(total, seq[index - 1])

        # Deals with all other parts of the generator list.
        elif (index-1)!=0:
            #Updates total based on previous and outputs the next index's calculation.
            total=previous
            previous = fn(total, seq[index - 1])
            yield fn(total, seq[index - 1])

        #Deals with the beginning of the generator list.
        else:
            #Starts the total at the beginning and outputs the beginning index.
            total=seq[index - 1]
            yield seq[index - 1]
'''
        >>> add = lambda x, y: x + y
        >>> mul = lambda x, y: x * y
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
'''