#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse
import readchar


def printAllCharsUpTo(stop_char):
    print('Printing all value up to stop_char ' + str(stop_char))
    for i in range(ord(' '), ord(stop_char)+1):
        print(chr(i))


def ReadAllUpTo(stop_key):


    # Ask for all the entries and put them in a list
    pressed_keys = [] # empty list to start
    while True:
        print('Type something (X to stop)')
        pressed_key = readchar.readkey()

        if pressed_key == stop_key:
            print('You typed X for terminating!')
            break
        else:
            #print('Thank you for typing ' + pressed_key)
            pressed_keys.append(pressed_key)

    print('The keys you pressed are:' + str(pressed_keys))
    # Analyse the list and count

    count_pressed_numbers = 0
    count_pressed_others = 0
    pressed_numbers = []
    pressed_others = []

    for pressed_key in pressed_keys:
        if str.isnumeric(pressed_key):
            count_pressed_numbers += 1
            pressed_numbers.append(pressed_key)
        else:
            count_pressed_others +=1
            pressed_others.append(pressed_key)

    print('You entered ' + str(count_pressed_numbers) + ' numbers:' + str(pressed_numbers))
    print('You entered ' + str(count_pressed_others) + ' others:' + str(pressed_others))


def main():

    #Ex4 a)
    #print('Give me the stop char ...')
    #pressed_char = readchar.readchar()

    #printAllCharsUpTo(pressed_char)

    #Ex4 c)
    ReadAllUpTo('X')

    #Ex4 c9


if __name__ == "__main__":
    main()