#Calcular números perfeitos (aqueles cuja soma dos divisores igualam o número) como por exemplo 6 = 3 + 2 + 1. Além do main() criar a função isPerfect(), que indica se o número é perfeito.

maximum_number = 100
sum1=0
def isPerfect(value):
    for divider in range(1,value):
	if   (value % divider == 0):
		sum1=sum1+divider
	if (sum1 == n):
		value == 1
	else:
		value == 0



def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()
