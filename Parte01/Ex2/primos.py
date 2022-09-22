#!/usr/bin/env python3

# Global variable
maximum_number = 50


# This is a function to assert if number value is a prime or not.
# If the value is prime, return True, else return False.

def isPrime(value):
    
    for number in range(2, value):
        remainder = value % number
        if remainder == 0: # I am sure number is not prime
            return False 

    # if I get here then there was no divider with remainder zero
    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for number in range(1, maximum_number + 1):
        if isPrime(number):
            print('Number ' + str(number) + ' is prime.')
        else:
            print('Number ' + str(number) + ' is not prime.')

if __name__ == "__main__":
    main()
    
#To count how many prime numbers there are with the number 3 on them, up do 10000, use: 
#python primos.py |grep "is prime" | grep "3" | wc -l
