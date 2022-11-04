#!/usr/bin/env python3

def addComplex(x, y):
    # (a+bi) + (c+di) = (a+c) + (b+d)i     

    # alternative 1
    a, b = x
    c, d = y

    real = a + c
    imaginary = b + d

    #? alternative 2
    #? real = x[0] + y[0]
    #? imaginary = x[1] + y[1]

    return (real, imaginary)

def multiplyComplex(x, y):
    # (a+bi)(c+di) = ac + adi + bci + bdi2
    a, b = x
    c, d = y

    real =  a * c - b* d
    imaginary =  a* d + b * c

    return (real, imaginary)

def printComplex(x):
    real, imaginary = x
    print(str(real) + '+' + str(imaginary) + 'i')

def main():
    # Definition of the two complex numbers to operate with
    c1 = (5, 3)
    c2 = (-2, 7)
    # Printing the complex numbers
    print('1st complex number is: '), printComplex(c1) 
    print('2nd complex number is: '), printComplex(c2)
    

    # Addition
    c3 = addComplex(c1, c2)
    print('\nResult of addition is:')
    printComplex(c3)

    # Multiplication
    print('Result of multiplication is:')
    printComplex(multiplyComplex(c1, c2))

# Sees if function was called in the terminal
if __name__ == "__main__":
    main()