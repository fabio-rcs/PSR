#!/usr/bin/env python3

from fileinput import filename
import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='Script for opening an image') 
    parser.add_argument('-fp', '--full_path', help = 'Full path of the image to show', default = '/home/fabio/Documents/PSR/Parte05/images/atlascar.png',) 
    args = parser.parse_args()

    image = cv2.imread(args.full_path, cv2.IMREAD_COLOR)
    image_2 = cv2.imread('images/atlascar2.png', cv2.IMREAD_COLOR)

    flip_flop = True

    while True:

        flip_flop = not flip_flop
        cv2.imshow('AtlasCar', image)  # Display the image
        if cv2.waitKey(3000) == ord('q'): # wait 3sec 
            break
        
        cv2.imshow('AtlasCar', image_2)
        if cv2.waitKey(3000) == ord('q'): # wait 3sec 
            break

if __name__ == '__main__':
    main()