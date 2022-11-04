#!/usr/bin/env python3

from copy import deepcopy
import cv2
import numpy as np

def main():

    #----------------------
    # Initialization
    #----------------------
    cap = cv2.VideoCapture(0) #Gets camera input
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #If capture fails, exit
    if not cap.isOpened():                 
        print("Cannot open camera") 
        exit()

    #----------------------
    # Execution
    #----------------------
    while True:
     
        ret, frame_rgb = cap.read() #Get a img_gui 
        if not ret: #If getting fails
            print("Can't receive img_gui (stream end?). Exiting ...")
            break
        
        img_gui = deepcopy(frame_rgb)   # working image in RGB
        img_gray = cv2.cvtColor(img_gui, cv2.COLOR_BGR2GRAY)    #image in GRAY

        # Detection of faces
        bboxes = face_cascade.detectMultiScale(img_gray,scaleFactor=1.2, minNeighbors=6,minSize=(20, 20))

        mask = np.zeros(frame_rgb.shape[:2], dtype="uint8")

        hsv = cv2.cvtColor(img_gui, cv2.COLOR_BGR2HSV) 
        lower_red = np.array([30,150,50]) 
        upper_red = np.array([255,255,180]) 
        mask_e = cv2.inRange(hsv, lower_red, upper_red) 
        res = cv2.bitwise_and(img_gui,img_gui,mask_e) 
        edges = cv2.Canny(img_gui,100,200) 
        #Drawing
        for bbox in bboxes:
            x, y, w, h = bbox 
            cv2.rectangle(mask, (x, y), (x+w, y+h), 255, -1)
            cv2.rectangle(img_gui,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.imshow("Rectangular Mask", mask)
            
            sub_img = img_gui[y:y+h, x:x+w]
            # sub_img = sub_img.astype(bool)
            # (b, g, r) = cv2.split(sub_img) #Splits the image in the 3 channels
            # b[sub_img] = 0
            # g[sub_img] = 255
            # r[sub_img] = 0
            # mask_rgb = cv2.merge((b, g, r))

            white_rect = np.ones(sub_img.shape, dtype=np.uint8)
            white_rect = (0, 200, 0, 3)
            res = cv2.addWeighted(sub_img, 0.5, white_rect, 0.3, 1)
            # Putting the image back to its position
            img_gui[y:y+h, x:x+w] = res
            
      
    
        
        cv2.imshow('Edges',edges) 

        #----------------------
        # Visualization
        #----------------------

        cv2.imshow('Video', img_gui)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    main()