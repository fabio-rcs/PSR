#!/usr/bin/env python3

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    # (a+bi) + (c+di) = (a+c) + (b+d)i  
    a = x.r
    b = x.i
    c = y.r
    d = y.i

    real = a + c
    imaginary = b + d
    return Complex(real, imaginary)

def multiplyComplex(x, y):
    # (a+bi)(c+di) = ac + adi + bci + bdi2
    a = x.r
    b = x.i
    c = y.r
    d = y.i

    real =  a*c - b*d
    imaginary =  a*d + b*c

    return Complex(real, imaginary)

def printComplex(x):
    real = x.r
    imaginary = x.i
    print (str(real) + '+' + str(imaginary) + 'i')

def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    printComplex(c1)
    printComplex(c2)

    # Test add
    c3 = addComplex(c1, c2)
    print('\nResult of addition is:')
    printComplex(c3)

    # test multiply
    c3 = multiplyComplex(c1,c2)
    print('Result of multiplication is:')
    printComplex(c3)


if __name__ == '__main__':
    main()