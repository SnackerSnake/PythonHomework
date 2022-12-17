#LAB 13
#Due Date: 12/06/2019, 11:59PM
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement: Course Material
#http://www.sjsu.edu/faculty/watkins/Digitsum.htm
#^Helped me figure out what a digit sum was.
#https://www.geeksforgeeks.org/callable-in-python/
########################################


def digitSum(num):
    #Checks to see if the input is a positive integer.
    if type(num)!=int:
        return None
    if num<0:
        return None

    def second_function(x):
        # Checks to see if the input is a positive integer.
        if type(x) != int:
            return None
        if x < 0:
            return None

        #Variable to use later.
        test=0

        # Counts the digit sum of x.
        for index in range(len(str(x))):
            test+=int(str(x)[index])

        #Checks if the digit sum of x is equal to num.
        if test==num:
            return True
        else:
            return False

    #Returns the second function.
    return second_function

'''
        >>> digitSum(15)(555)
        True
        >>> digitSum(22)(2578)
        True
        >>> digitSum(258)(1011010101010)
        False
'''

def alternate(fn1, fn2):

    def function(n):
        # Check if inputs are functions.
        if callable(fn1) != True or callable(fn1) != True:
            return "At least 1 of the inputs is not a function."

        #Starts a list and starting point.
        list = []
        #Called addition because it's always being added by +1.
        addition = 1

        #Alternates between odd and even.
        while addition != n+1:

            #If even, use function 2.
            if addition % 2 == 0:
                list.append(fn2(addition))
                addition += 1

            #If odd, use function 1.
            else:
                list.append(fn1(addition))
                addition += 1

        #Returns a list as the output.
        return list

    #Returns the function.
    return function

'''
        >>> def isEven(x):
        ...    return x % 2 == 0
        >>> ex1 = alternate(isEven, lambda x: x + 4)
        >>> ex1(5)
        [False, 6, False, 8, False]
        >>> ex2 = alternate(lambda x: x * 2, lambda x:x%5 if x<6 else x%2)
        >>> ex2(7)
        [2, 2, 6, 4, 10, 0, 14]
'''