#!/usr/bin/env python3

# Imports
from colorama import Fore, Back, Style

from my_functions import isPrime 
"""Preferred alternative"""

#import my_functions 
"""This alternative imports all the function"""

# Global variable
maximum_number = 10


def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for number in range(1, maximum_number + 1):
        if isPrime(number):
            print(Style.BRIGHT + Back.BLUE +  Fore.BLACK + 'Number ' + str(number) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(number) + ' is not prime.')

if __name__ == "__main__":
    main()
