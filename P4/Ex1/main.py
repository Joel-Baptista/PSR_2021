#!/usr/bin/python3
import cv2
import argparse


def main():
    parser = argparse.ArgumentParser(description='OpenCv Example')
    parser.add_argument('-im', '--image1', type=str, help='Full Path to image')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image1'], cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()
