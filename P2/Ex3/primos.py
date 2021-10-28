#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse


def isPrime(value):
    prime = True
    print("Checking number " + str(value))
    for x in range(2, value):
        remainder = value % x
        if remainder == 0:
            prime = False
            print("It's divisible by " + str(x))
    return prime


def main():
    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--maximum_number', type=int, help='Maximum number to search for primes')
    parser.add_argument('--verbose', action='store_true', help='print stuff to the screen or not.')
    args = vars(parser.parse_args())
    print(args)

    print("Starting to compute prime numbers up to " + str(args['maximum_number']))
    for i in range(2, args['maximum_number']):
        if isPrime(i):
            print('Number ' + Fore.BLUE + Back.MAGENTA + Style.BRIGHT + str(i) + Style.RESET_ALL + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')


if __name__ == "__main__":
    main()