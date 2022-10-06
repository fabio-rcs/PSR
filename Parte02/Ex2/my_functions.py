#!/usr/bin/env python3
###!/usr/bin/python3 # versão manual

# Imports
from colorama import Fore, Back, Style


# This is a function to assert if number value is a prime or not.
# If the value is prime, return True, else return False.
def isPrime(value):
    
    for number in range(2, value):
        remainder = value % number
        print(str(value) + '/' + str(number) + ' = '+  str(remainder))
        if remainder == 0: # I am sure number is not prime
            return False 

    # if I get here then there was no divider with remainder zero
    return True
