#!/usr/bin/env python3

import rospy
from psr_aula09_ex1.msg import Dog

def msgReceivedCallback(msg):

    rospy.loginfo(rospy.get_caller_id() + '\nI received:\n' + str(msg) + '\n')

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
  