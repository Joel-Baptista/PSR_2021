#!/usr/bin/python3
import colorama

def addComplex(x, y):
    # add code here ...
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    return (a+c,b+d)


def multiplyComplex(x, y):
    # add code here ...
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    result_real = (a * c - b * d)
    result_im = (a * d + b * c)
    return (result_real, result_im)


def printComplex(x, prefix=''):
    # add code here ...
    r = x[0]
    i = x[1]
    print(prefix +str(r) + '+' + str(i) + 'i')


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    printComplex(c1,prefix= colorama.Fore.RED + 'c1=' + colorama.Style.RESET_ALL)
    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()
