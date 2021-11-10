#!/usr/bin/python3

import cv2
import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser(description='OpenCv Example')
    parser.add_argument('-im1', '--image1', type=str, help='Full Path to image')
    args = vars(parser.parse_args())

    # # Alinea a)
    image = cv2.imread(args['image1'], cv2.IMREAD_COLOR)
    image_gray = cv2.imread(args['image1'], cv2.IMREAD_GRAYSCALE)  # Load an image

    # retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    #
    # cv2.imshow('Ex2a', image_thresholded)  # Display the image
    #
    # # Alinea b)
    # print(type(image_gray))
    # print(image_gray.shape)
    # print(image_gray.dtype)
    #
    # image_thresholded = image_gray > 128
    #
    # cv2.imshow('Exb', 255*image_thresholded.astype('uint8'))
    #
    # # Alinea c)
    #
    # B, G, R = cv2.split(image)
    #
    # B_thresh = 255*(B > 50).astype('uint8')
    # G_thresh = 255*(G > 100).astype('uint8')
    # R_thresh = 255*(R > 150).astype('uint8')
    #
    # im_thresh = cv2.merge((B_thresh, G_thresh, R_thresh))
    # cv2.imshow('Ex2c', im_thresh)
    #
    # # Alinea d)
    # limit_high = (100, 256, 20)
    # limit_low = (0, 70, 0)
    # mask = cv2.inRange(image, limit_low, limit_high)
    # cv2.imshow('Ex2d', mask)

    # Alinea e)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    limit_high = (70, 256, 150)
    limit_low = (50, 150, 0)
    mask = cv2.inRange(image_hsv, limit_low, limit_high)
    # cv2.imshow('Main', image)
    # cv2.imshow('Ex2e', mask)

    # Alinea f)

    mask_red = cv2.bitwise_or(image, image, mask=mask)
    mask_red = mask_red*
    cv2.imshow('Mask', mask_red)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
