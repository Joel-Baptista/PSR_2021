#!/usr/bin/python3

import cv2 as cv
import numpy as np


def paint(event, x, y, flags, o):
    pass


def main():

    global img

    # Alinea a)
    # img = cv.imread('atlascar.png', cv.IMREAD_COLOR)
    # cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 100, (0, 0, 255), -1)
    # cv.imshow('Ex1a', img)  # Display the image
    # cv.imshow('Ex1a_1', img)  # Display the image
    #
    # Alinea b)
    # img = cv.imread('atlascar.png', cv.IMREAD_COLOR)
    # img_text = cv.putText(img, 'PSR', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    # cv.imshow('Ex1b', img_text)  # Display the image

    # Alinea c)

    img = np.ones((600, 400))
    cv.imshow('Ex1c', img)
    cv.setMouseCallback('Ex1c', paint)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
