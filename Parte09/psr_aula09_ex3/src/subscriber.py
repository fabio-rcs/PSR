#!/usr/bin/env python3

import rospy
from psr_aula09_ex3.msg import Dog
from colorama import Fore, Style

def msgReceivedCallback(msg):

    # Gets necessary parameters
    highlight_text_color = rospy.get_param("/highlight_text_color", 'CYAN') # Global parameter 

    rospy.loginfo(rospy.get_caller_id() + '\nI received:\n' + getattr(Fore, highlight_text_color) + str(msg) + Style.RESET_ALL + '\n')

def main():

    # ----------------------------------------------
    # Initialization
    # ----------------------------------------------

    # Initialization of a ROS node
    rospy.init_node('subscriber', anonymous=True)

    # Initialize subscriber
    rospy.Subscriber('chatter', Dog, msgReceivedCallback)
  
    # ----------------------------------------------
    # Execution
    # ----------------------------------------------

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

   # ----------------------------------------------
    # Termination
    # ----------------------------------------------

if __name__ == '__main__':
    main()
  