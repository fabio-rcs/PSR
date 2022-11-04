#!/usr/bin/env python3

from curses.ascii import isdigit
from readchar import readkey

"""Function that reads a key from the keyboard and prints
all characters since space, according to the ASCII value"""

#Prints all characters since the "space" key up to the pressed one
def printAllCharsUpTo(stop_char):

    last_number=ord(stop_char)
    characters=[]

    for number in range(32, last_number):
        character=chr(number)
        characters.append(character)

    text='  '.join(characters)

    print('Characters since space bar up to "'+ stop_char+'": '+'\n' +str(text))
    
    return character

#Input function reads key pressed and prints it's ASCII value
def input():
    
    key=readkey()
    printAllCharsUpTo(key)
    print('The ASCII value of "' +key+'" is: '+str(ord(key)))

#Main function prints an introductory text and calls the rest of the code
def main():

    print('Press any key and see what happens')
    input()
    

if __name__ == '__main__':
    main()