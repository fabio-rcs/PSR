#!/usr/bin/env python3
import cv2

def main():

    #----------------------
    # Initialization
    #----------------------
    cap = cv2.VideoCapture(0) #Gets camera input

    #If capture fails, exit
    if not cap.isOpened():                 
        print("Cannot open camera") 
        exit()

    #----------------------
    # Execution
    #----------------------
    while True:
     
        ret, frame_rgb = cap.read() #Get a frame 
        if not ret: #If getting fails
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('Video', frame_rgb)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    main()