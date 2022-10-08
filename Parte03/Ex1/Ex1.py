#!/usr/bin/env python3
from cmath import sqrt
from colorama import Fore, Back, Style 
from time import time, ctime

#time()
#Gets number od seconds that passed since 01/01/1970

#ctime()
#Gets current date

#Function to get the computing time 
def ticToc():
    #Get time before computing
    tic = time()

    #Function to calculate the square root of all int numbers until 50M
    for i in range (0,5000000+1):
        _ = sqrt(i)
    
    #Get time after computing
    toc = time()

    #Calculate elapsed time
    time_elapsed = toc-tic

    #Return the computing time
    return(time_elapsed)
    
def main():

    #Prints the current date with colored text
    print(Style.BRIGHT,'The current date is:',Style.NORMAL,Back.LIGHTMAGENTA_EX,ctime(),Style.RESET_ALL)

    #Calls the function
    ticToc()

    #Prints the computing time with colored text
    print(Style.BRIGHT, Fore.RED, Back.YELLOW,'Time elapsed:',Style.NORMAL, ticToc(), Style.RESET_ALL)

#Sees if function was called in terminal
if __name__=='__main__':
    main()