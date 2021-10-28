#!/usr/bin/python3

class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        a = self.r
        b = self.i
        c = y.r
        d = y.i
        self.r = a + c
        self.i = b + d

    def multiply(self, y):
        a = self.r
        b = self.i
        c = y.r
        d = y.i
        self.r = a * c - b * d
        self.i = a * d + b * c

    def __str__(self):
        return str(self.r) + '+' + 'i' + str(self.i)


def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c2.add(c1)
    print(c2)  # uses the __str__ method in the class


if __name__ == '__main__':
    main()
