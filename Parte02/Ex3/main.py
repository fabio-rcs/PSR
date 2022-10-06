#!/usr/bin/env python3

# Imports
from colorama import Fore, Back, Style

from my_functions import isPrime 

import argparse

"""Main Function"""

def main():

    parser = argparse.ArgumentParser(description='Parte02, Exercise 3')
    parser.add_argument('-mn','--maximum_number', type=int, required=True,
                        help='The maximum number until we will check if numbers are prime')

    args = vars(parser.parse_args())
    
    ##maximum_number = args['maximum_number']
    #instead of creating the variable, we use it directly from the argparse dictionary

    #Test for prime numbers
    print("Starting to compute prime numbers up to " + str(args['maximum_number']))


    for number in range(1, args['maximum_number'] + 1):
        if isPrime(number):
            print(Style.BRIGHT + Back.BLUE +  Fore.BLACK + 'Number ' + str(number) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(number) + ' is not prime.')

if __name__ == "__main__":
    main() 