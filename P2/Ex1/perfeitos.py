#!/usr/bin/python3
# --------------------------------------------------
# Um programa que verifica se os números entre 1 e o "maximum_number" são perfeitos
# ou seja, se a soma dos seus divisores é igual ao próprio número (6=1+2+3)
# Joel Fernando Bastos Baptista.
# PSR, Outubro 2021.
# --------------------------------------------------
from colorama import Fore, Back, Style

maximum_number = 100


def getDividers(value):
    div = [];
    for x in range(1,value):
        remainder = value % x
        if remainder == 0:
            div.append(x)
    return div


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