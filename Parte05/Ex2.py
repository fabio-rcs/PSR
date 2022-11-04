#!/usr/bin/env python3

from typing import overload
import cv2
import numpy as np

def main():

    # ---------------------
    #Initialization
    #----------------------
    image_rgb = cv2.imread('images/atlascar2.png', cv2.IMREAD_COLOR)
    image_rgb_2d = cv2.imread('images/atlas2000_e_atlasmv.png')

    #Binarization limits
    threshold_level_b = 50      
    threshold_level_g = 100
    threshold_level_r = 150

    # ----------------
    # Processing
    #----------------
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY) #Converts image to grayscale
    _, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    (image_b, image_g, image_r) = cv2.split(image_rgb) #Splits the image in the 3 channels

    #Applies the limits to each channel
    _, image_thresholded_b = cv2.threshold(image_b, threshold_level_b, 255, cv2.THRESH_BINARY)   
    _, image_thresholded_g = cv2.threshold(image_g, threshold_level_g, 255, cv2.THRESH_BINARY)
    _, image_thresholded_r = cv2.threshold(image_r, threshold_level_r, 255, cv2.THRESH_BINARY)

    image_thresholded_rgb = cv2.merge([image_thresholded_b, image_thresholded_g, image_thresholded_r]) #Merges the 3 channels into a single image

    #Definition of the upper and lower bounds of binarization to get just the green in the image
    lower_bond = np.array([0,60,0]) #Bellow this is 0
    upper_bond = np.array([50, 255, 40]) #Bigger than this is 1
    image_mask = cv2.inRange(image_rgb_2d, lower_bond, upper_bond) #Applies the binarization to the image 
    
    #The same but for HSV color channels
    hsv_lower_bond = np.array([60, 80, 80]) #Bellow this is 0
    hsv_upper_bond = np.array([75, 255, 255]) #Bigger than this is 1
    image_hsv = cv2.cvtColor(image_rgb_2d, cv2.COLOR_BGR2HSV) 
    image_hsv_mask = cv2.inRange(image_hsv, hsv_lower_bond, hsv_upper_bond)

    image_mask_2f = image_mask.astype(bool)
    (b, g, r) = cv2.split(image_rgb_2d) #Splits the image in the 3 channels
    b[image_mask_2f] = 0
    g[image_mask_2f] = 0
    r[image_mask_2f] = 255

    image_rgb_2f = cv2.merge((b, g, r))
    # --------------------------
    # Visualization
    # ------------------------
    cv2.imshow('AtlasCar 2a', image_thresholded)  # Display the image
    print('OpenCV:\n\t' + 'Type ' + str(type(image_thresholded_rgb)))
    print('\tShape ' + str(image_thresholded_rgb.shape))
    print('\tDType ' + str(image_thresholded_rgb.dtype))
    if cv2.waitKey(0) == ord('q'):
        exit() 

    cv2.imshow('Thresholded Image 2c', image_thresholded_rgb)
    if cv2.waitKey(0) == ord('q'):
        exit()

    cv2.imshow('Mask 2.d)', image_mask)
    if cv2.waitKey(0) == ord('q'):
        exit()

    cv2.imshow('Mask 2.e)', image_hsv_mask)
    if cv2.waitKey(0) == ord('q'):
        exit()
    
    cv2.imshow('Mask 2.f)', image_rgb_2f)
    if cv2.waitKey(0) == ord('q'):
        exit()

if __name__ == '__main__':
    main()

    