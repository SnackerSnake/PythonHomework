#Lab #4
#Due Date: 09/20/2019, 11:59PM EST
########################################
#                                      
# Name:David Hernandez
# Collaboration Statement:
# https://www.geeksforgeeks.org/python-format-function/ explaining format
#
########################################

#Starts the Soda Machine class.
class BadSodaMachine:
    '''
        >>> m = BadSodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.purchase(2)
        'Product out of stock'
        >>> m.restock(3)
        'Current soda stock: 3'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.purchase(2)
        'Please deposit $13'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(20)
        'Balance: $20'
        >>> m.purchase(2)
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    #Declares the variables to use later.
    def __init__(self, product, price):
        self.product=product
        self.price=price
        self.balance= 0
        self.stock=0


    #Determines if the user gets a soda.
    def purchase(self, amount_buying=1):

        #Checks if the input is an interger in the first place.
        if type(amount_buying) != int:
            return None

        #Checks if the user isn't putting a negative number or 0.
        if amount_buying <= 0:
            return None

        #Checks to see if there are drinks in stock.
        if self.stock>=amount_buying:

            # No money means no soda.
            if self.balance==0:
                return "Please deposit ${}".format(self.price*amount_buying)

            # Not enough money tells the user that he or needs needs to put more money for soda.
            if self.balance>0 and self.balance<self.price*amount_buying:
                return "Please deposit ${}".format(self.price*amount_buying-self.balance)

            # enough money to buy a soda. Yay!
            if self.balance==self.price*amount_buying:
                self.stock -= amount_buying
                self.balance -= self.price*amount_buying

                return "{} dispensed".format(self.product)

            # More than enough money to buy a soda. Returns soda and overflown money
            if self.balance>self.price*amount_buying:

                calculation_positive=self.balance
                calculation_subtraction=self.price*amount_buying

                self.stock -= amount_buying
                self.balance -= self.balance

                return "{} dispensed, take your ${}".format(self.product, calculation_positive-calculation_subtraction)

        #If the user demands more sodas than there are available, then it will tell the user how many are left.
        elif self.stock<amount_buying and self.stock!=0:
            return "Current soda stock: {}".format(self.stock)

        #If the user already put in money and there are no sodas, it will give the money back.
        elif self.stock==0 and self.balance>0:
            self.balance-=self.balance
            return "Sorry, out of stock. Take your ${} back".format(self.balance)

        #If there are no sodas in stock, it will tell the user that.
        else:
            return "Product out of stock"

    #Deposits money for the user.
    def deposit(self, amount):

    # Checks if the input is an interger in the first place.
        if type(amount) != int:
            return None

        #Checks if the deposit isn't negative.
        if amount < 0:
            return None

        #Checks if there is soda in stock.
        if self.stock==0:
            return "Sorry, out of stock. Take your ${} back".format(amount)

        #Adds money to the soda machine.
        self.balance+=amount
        return "Balance: ${}".format(self.balance)

    #Refills sodas.
    def restock(self, amount):

        # Checks if the input is an interger in the first place.
        if type(amount) != int:
            return None

        #Checks if input isn't negative.
        if amount < 0:
            return None

        #Adds sodas to the soda machine.
        self.stock+=amount
        return "Current soda stock: {}".format(self.stock)

