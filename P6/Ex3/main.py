#!/usr/bin/env python
import copy

import cv2
import numpy as np


def main():

    # initial setup
    capture = cv2.VideoCapture(0)
    first = True
    while True:
        window_name = 'A5-Ex2'
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

        _, image_gui = capture.read()  # get an image from the camera
        image = copy.deepcopy(image_gui)
        if first:
            previous_img = copy.deepcopy(image_gui)
            first = False

        # Convert into grayscale
        gray = cv2.cvtColor(image_gui, cv2.COLOR_BGR2GRAY)

        # Load the cascade
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            mask = np.zeros(image.shape[:2], 'uint8')
            mask_mouth = copy.deepcopy(mask)
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
            cv2.rectangle(mask_mouth, (x, y + int(2/3*h)), (x + w, y + h), 255, -1)
            cv2.add(image, (-10, 50, -10, 0), dst=image, mask=mask)

            cv2.add(image, (50, -10, -10, 0), dst=image, mask=mask_mouth)

        np.abs
        # Display the output
        cv2.imshow('img', image)
        diff = cv2.absdiff(image_gui, previous_img)
        cv2.imshow('Window',diff)
        key = cv2.waitKey(20) # add code to wait for a key press
        if key != -1:
            break

        previous_img = copy.deepcopy(image_gui)


if __name__ == '__main__':
    main()
