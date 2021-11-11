#!/usr/bin/env python
import cv2


def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    _, image = capture.read()  # get an image from the camera

    cv2.imshow(window_name, image)# add code to show acquired image
    cv2.waitKey(20)# add code to wait for a key press


if __name__ == '__main__':
    main()