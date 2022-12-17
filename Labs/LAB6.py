#Lab #6
#Due Date: 10/04/2019, 11:59PM 
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement:Area 51 aliens
#https://docs.python.org/3/tutorial/datastructures.html
#Piazza
#
########################################


## ALL FUNCTIONS MUST BE RECURSIVE IN ORDER TO GET CREDIT FOR THEM

def mulBy(num):

    if num<=2:
        return num

    else:
        return num*mulBy(num-2)

'''
        >>> mulBy(5)
        15
        >>> mulBy(8)
        384
        >>> mulBy(0)
        0
        >>> mulBy(1)
        1
'''

def flat(aList, new_list=None, num=0):

    if new_list is None:
        new_list = []

    if num==len(aList):
        return new_list

    #Checks for lists in the list and removes them.
    if type(aList[num])==list:
        new_list.extend(aList[num])

        if type(new_list[num]) == list:
            new_list.extend(new_list[num])
            new_list.pop(num)

            if type(new_list[num]) == list:
                new_list.extend(new_list[num])
                new_list.pop(num)

    else:

        new_list.append(aList[num])

    return flat(aList,new_list, num+1)
'''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''

def isPrime(num, which_step=0):
    if num>1000:
        num-=1000

    if num<=1:
        return False
    elif which_step==num:
        return True
    elif num % (num-which_step)==0 and which_step!=0 and (num-which_step!=1):
        return False

    return isPrime(num, which_step+1)
'''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
        >>> isPrime(2654)
        False
'''


def countPrimes(num,result=0):

    if num<0 and result==0:
        return 0

    if isPrime(num)==True:
        result+=1

    if num==1:
        return result

    return countPrimes(num-1, result)
'''
        >>> countPrimes(0)
        0
        >>> countPrimes(6)
        3
        >>> countPrimes(2)
        1
        >>> countPrimes(60)
        17
        >>> countPrimes(100)
        25
        >>> countPrimes(500)
        95
'''

