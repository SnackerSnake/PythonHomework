#Lab #5
#Due Date: 09/27/2019, 11:59PM EST
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement: Course Material
# https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
#
########################################

#Defines complex number class
class Complex:
    def __init__(self, real, imag):
        #Checks if intput of complex numbers are ints or floats
        if (type(real) != (int or float)  or  type(imag) !=(int or float)):
            return None

        #Sets variables for later
        self.real = real
        self.imag = imag

    #repr and str represent the output in differnt ways in different cases
    def __str__(self):
        if self.imag<0:
            return "{}{}i".format(self.real, self.imag)
        else:
            return "{}+{}i".format(self.real, self.imag)

    def __repr__(self):
        return "({}, {}i)".format(self.real,self.imag)

    #Adds complex number inputs
    def __add__ (self, other):
        return Complex(self.real+other.real, self.imag+other.imag)

    # Subtracts complex number inputs
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # Subtracts complex number inputs and integers
    def __mul__(self, other):
        if type(self)==int:
            #first_parameter=self*other.real
            print(other.real)
            print(other.imag)
            print(self)
            return Complex(self*+other.real, self*other.imag)
        else:
            return Complex(self.real*other.real-other.imag*self.imag, self.real*other.imag+other.real*self.imag)

    #Finds the conjugate of complex number inputs.
    @property
    def conjugate(self):
        if self.imag<0:
            return Complex(self.real, abs(self.imag))
        else:
            return Complex(self.real, -self.imag)

a=Complex(5,-6)
b=Complex(2,14)
'''
        >>> a=Complex(5,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7, 8i)
        >>> a-b
        (3, -20i)
        >>> a*b
        (94, 58i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> print(a)
        5-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> a.conjugate
        (5, 6i)
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
'''