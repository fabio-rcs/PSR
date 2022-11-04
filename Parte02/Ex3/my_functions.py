#!/usr/bin/env python3

# Imports
from colorama import Fore, Back, Style
import math

# This is a function to assert if number value is a prime or not.
# If the value is prime, return True, else return False.
def isPrime(value):
    max_range=int(math.sqrt(value))
    for number in range(2,max_range+1):
        remainder = value % number
        
        if remainder == 0: # I am sure number is not prime
            return False 

    # if I get here then there was no divider with remainder zero
    return True
