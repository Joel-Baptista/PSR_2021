#!/usr/bin/python3
import cv2
import argparse


def main():
    parser = argparse.ArgumentParser(description='OpenCv Example')
    parser.add_argument('-im1', '--image1', type=str, help='Full Path to image')
    parser.add_argument('-im2', '--image2', type=str, help='Full Path to image')
    args = vars(parser.parse_args())

    count = 0
    image1 = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    image2 = cv2.imread(args['image2'], cv2.IMREAD_COLOR)  # Load an image

    while True:
        count += 1

        if divmod(count, 2)[1] == 0:
            cv2.imshow('window', image1)  # Display the image
        else:
            cv2.imshow('window', image2)

        window_open = cv2.waitKey(3000)
        if window_open != -1:
            continue
        else:
            break


if __name__ == '__main__':
    main()
