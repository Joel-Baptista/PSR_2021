#!/usr/bin/python3

from colorama import Fore, Back, Style

maximum_number = 100000000


def isPerfect(value):
    print("Checking " + str(value))
    soma = 1
    for x in range(2,value):
        remainder = value % x
        if remainder == 0:
            soma = soma + x

    if soma == value:
        return True
    return False


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(2, maximum_number):
        if isPerfect(i):
            print(Fore.BLACK + Back.WHITE +'Number ' + str(i) + ' is perfect.' + Style.RESET_ALL)


if __name__ == "__main__":
    main()