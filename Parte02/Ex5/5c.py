#!/usr/bin/env python3

from readchar import readkey

"""Function that reads a key from the keyboard and prints
all characters since space, according to the ASCII value"""

#sake_case used for variables
#camelCase used for functions

#Function will say which character was pressed until the stop character
def readAllUpTo(stop_char):

    inputs=[]
    other_inputs=[]

    while True:
        key=readkey()
        print('You entered character: ' + key)
    
        if key == stop_char:
            break

        inputs.append(key)

    other_inputs=[input for input in inputs if not input.isnumeric()]

    other_inputs_dic={}
    count=0
    for input in inputs:
        if not input.isnumeric():
            other_inputs_dic[count]=input
        count+=1

 #   other_inputs_dic={}
  #  for other_input in other_inputs:
   #    idx=inputs.index(other_input)
    #   other_inputs_dic[key]=other_input
    #This Solution doesn't work with repeated numbers

    print('The order at which you entered non numeric characters was:',str(other_inputs_dic))


#Main function prints an introductory text and calls the rest of the code. End character is 'X'
def main():

    print('Press any key and see what happens')
    readAllUpTo('X')

if __name__ == '__main__':
    main()