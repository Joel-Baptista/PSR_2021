#!/usr/bin/python3

from colorama import Fore, Back, Style


maximum_number = 101


def isPrime(value):
    prime = True
    print("Checking number " + str(value))
    for x in range(2,value):
        remainder = value % x
        if remainder == 0:
            prime = False
            print("It's divisible by " + str(x))
    return prime

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number):
        if isPrime(i):
            print('Number ' + Fore.BLUE + Back.MAGENTA + Style.BRIGHT+ str(i) + Style.RESET_ALL + ' is prime.' )
        else:
            print('Number ' + str(i) + ' is not prime.')


if __name__ == "__main__":
    main()