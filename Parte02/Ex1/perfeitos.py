#!/usr/bin/env python3

#Calcular números perfeitos (aqueles cuja soma dos divisores igualam o número) 
#como por exemplo 6 = 3 + 2 + 1. 
# Além do main() criar a função isPerfect(), que indica se o número é perfeito.
"""Gets the integer divider of a number"""
"""Args:
		number (int): a number to test"""
"""Return:
			perfect number"""

maximum_number = 100

#function to check is i is a perfect number
def isPerfect(i):
	
		sum=0
		for n in range(1,i):    
			if i%n == 0:
				sum+=n
				
		if sum == i:
			return True
			
#call function and print perfect numbers
def main():
	print("Starting to compute perfect numbers up to " + str(maximum_number)+':')

	for i in range(1, maximum_number+1):
		if isPerfect(i):
			print('Number ' + str(i) + ' is perfect.')

if __name__ == '__main__':
	main()
