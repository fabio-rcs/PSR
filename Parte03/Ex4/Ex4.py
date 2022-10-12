#!/usr/bin/env python3

class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, c2):
        self.r += c2.r
        self.i += c2.i 

    def multiply(self, c2):
        #* (a+bi)(c+di) = ac + adi + bci + bdi2
        self.r = self.r*c2.r - self.i*c2.i
        self.i = self.r*c2.i + self.i*c2.r
    
    def __str__(self):
        return f'Complex {self.r} + {self.i}i'

def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    print(c2)
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class
 
    # test multiply
    c2.multiply(c1)
    print(c2)  # uses the __str__ method in the class

if __name__ == '__main__':
    main()