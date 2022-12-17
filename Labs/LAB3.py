#Lab #3
#Due Date: 09/13/2019, 11:59PM
########################################
#                                      
# Name: David Hernandez
# Collaboration Statement: https://www.geeksforgeeks.org/python-string-length-len/
#(for figuring out how to find length of string)
# Note: "find_words_and_numbers" function is very similar to removePunctuation from Lab 2,
# so I reused most parts of that to create this function.
#
########################################


#Removes everything from a string except numbers and letters.
def find_words_and_numbers(txt):

    #Starts off the variables for the function.
    statement=("")

    #Checks to see if the input is a string in the first place.
    if type(txt)==str:

        #Goes through every character in the string.
        for character in txt:

        #Adds all letters to the final result. #or character.isdigit()
            if character.isalpha() or character.isdigit():
                statement+=character.lower()

        #Returns with the all the letters and numbers.
        return statement

    #Returns none if the input was not a string.
    else:
        return None


#Return false if not string
#Return true if string can be spelt the same regularly and reversed (i.e. is a palindrome)

def isPalindrome(text):

    #Checks if the input is a string.
    if type(text)==str:

        # Names variables to use later
        this_many_times = len(text)
        text = find_words_and_numbers(text)
        giving_text = find_words_and_numbers(text)
        reversed_text = ("")

        #Gives a variable (reversed_text) the last character of the string input
        reversed_text += giving_text[-1:]

        # Gives a variable (reversed_text) the last character of the string input,
        # removes that last character, and keeps repeating this process
        # until there is nothing else to give.
        while (this_many_times>1):

            giving_text = giving_text[:-1]

            reversed_text += giving_text[-1:]

            this_many_times-=1

        #Checks to see if the input is truly a palindrome
        #by comparing a variable (reversed_text) to the input.
        if text==reversed_text:

            return True
        #Returns false if the test above fails.
        else:

            return False
        #Returns false if the input isn't a string.
    else:
        return False
"""
        >>> isPalindrome("alula")
        True
        >>> isPalindrome("love")
        False
        >>> isPalindrome("Madam")
        True
        >>> isPalindrome(12.5)
        False
        >>> isPalindrome(12.21)
        False
        >>> isPalindrome("Cigar? Toss it in a can.! It is so tragic.")
        True
        >>> isPalindrome("travel.. a town in Alaska")
        False
"""

