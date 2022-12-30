#!/usr/bin/env python3
# --------------------------------------------------
# Fábio Sousa.
# PSR, December 2022.
# --------------------------------------------------

import rospy
import cv2
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge

def main():
    #-----------------------------
    # Initialization
    #-----------------------------
    
    # Video Capture
    capture_object      = cv2.VideoCapture(0)
    _,camera_source_img = capture_object.read() 
    bridge_class = CvBridge()

    # Initialization of a ros node
    rospy.init_node('image_publisher', anonymous=False)
    
    # ! Frequency cant be low otherwise the stream is laggy
    frequency = rospy.get_param('~frequency',30) # To change at terminal use _frequency:= x
    rate      = rospy.Rate(frequency) 
    image_pub = rospy.Publisher("/image_viewer", Image, queue_size=1)
    
    #-----------------------------
    # Processing
    #-----------------------------
    
    while not rospy.is_shutdown():

        # Frame cap and showing
        _,camera_source_img = capture_object.read() 
        cv2.imshow("Source",camera_source_img)
        
        # Image encoding to send as ros message
        image_message = bridge_class.cv2_to_imgmsg(camera_source_img, encoding="bgr8") # Must be bgr8 to send correctly
        image_pub.publish(image_message)
        
        rate.sleep()
        rospy.loginfo("Sending image")
        
        pressed_key = cv2.waitKey(1) & 0xFF # To prevent NumLock issue
        
        if pressed_key  == ord('q'): 

            print("Quitting program")
            cv2.destroyAllWindows
  
            exit()
    
    #-----------------------------
    # Termination
    #-----------------------------

if __name__=="__main__":
    main()