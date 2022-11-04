#!/usr/bin/env python3

from curses.ascii import isdigit
from readchar import readkey

"""Function that reads a key from the keyboard and prints
all characters since space, according to the ASCII value"""

#Function will say which character was pressed until the stop character
def readAllUpTo(stop_char):
    while True:
        key=readkey()
        print('You entered character: ' + key)
    
        if key == stop_char:
            break

#Main function prints an introductory text and calls the rest of the code. End character is 'X'
def main():

    print('Press any key and see what happens')
    readAllUpTo('X')
    

if __name__ == '__main__':
    main()