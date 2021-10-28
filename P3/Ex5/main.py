#!/usr/bin/python3

def addComplex(x, y):
    # add code here ...
    a = x['r']
    b = x['i']
    c = y['r']
    d = y['i']
    return {'r': a+c,'i': b+d}


def multiplyComplex(x, y):
    # add code here ...
    a = x['r']
    b = x['i']
    c = y['r']
    d = y['i']
    result_real = (a * c - b * d)
    result_im = (a * d + b * c)
    return {'r': rresult_real, 'i': result_im}


def printComplex(x, prefix=''):
    # add code here ...
    r = x['r']
    i = x['i']
    print(prefix +str(r) + '+' + str(i) + 'i')


def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = {'r': 3, 'i': 5}  # use order when not naming
    c2 = {'r': 7, 'i': -2}  # if items are names order is not relevant

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
