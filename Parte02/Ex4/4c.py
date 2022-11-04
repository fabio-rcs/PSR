#!/usr/bin/env python3

from unicodedata import numeric
from readchar import readkey

"""Function that reads a key from the keyboard and prints
all characters since space, according to the ASCII value"""

#sake_case used for variables
#camelCase used for functions

#Function will say which character was pressed until the stop character
def readAllUpTo(stop_char):

    inputs=[]
    numeric_inputs=[]
    other_inputs=[]

    while True:
        key=readkey()
        print('You entered character: ' + key)
    
        if key == stop_char:
            break

        inputs.append(key)

#function to count total number of each kind of inputs
    for input in inputs:

        if input.isnumeric():
            numeric_inputs.append(input)
        else:
            other_inputs.append(input)

        total_numbers = len(numeric_inputs)
        total_others = len(other_inputs)
    

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')


#Main function prints an introductory text and calls the rest of the code. End character is 'X'
def main():

    print('Press any key and see what happens')
    readAllUpTo('X')

if __name__ == '__main__':
    main()