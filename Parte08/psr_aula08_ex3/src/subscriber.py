#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import argparse

def msgReceivedCallback(msg):

    rospy.loginfo(rospy.get_caller_id() + 'I received ' + str(msg.data))

def main():

    # ----------------------------------------------
    # Initialization
    # ----------------------------------------------
   
    parser = argparse.ArgumentParser(description='Names of ROS communication details')
    parser.add_argument('-t', '--topic', type=str, required=False, default= 'chatter')
    parser.add_argument('-n', '--node', type=str, required=False, default= 'subscriber')
    
    args = vars(parser.parse_args())

    # Initialization of a ROS node
    rospy.init_node(args['node'], anonymous=True)

    # Initialize subscriber
    rospy.Subscriber(args['topic'], String, msgReceivedCallback)
  
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
  