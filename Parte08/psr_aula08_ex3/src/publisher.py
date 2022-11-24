#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import argparse

def main():

    # ----------------------------------------------
    # Initialization
    # ----------------------------------------------

    parser = argparse.ArgumentParser(description='Variables of ROS communication system')
    parser.add_argument('-t', '--topic', type=str, required=False, default= 'chatter')
    parser.add_argument('-n', '--node', type=str, required=False, default= 'talker')
    parser.add_argument('-f', '--frequency', type=int, required=False, default= '1')
    parser.add_argument('-m', '--msg', type=str, required=False, default= 'Hello World')

    args = vars(parser.parse_args())

    # Initialization of a ROS node
    rospy.init_node(args['node'], anonymous=False)
    
    # ----------------------------------------------
    # Execution
    # ----------------------------------------------

    # Create the publisher
    publisher = rospy.Publisher(args['topic'], String, queue_size=10)

    # Send message every x seconds
    rate = rospy.Rate(args['frequency']) # hz
    while not rospy.is_shutdown():
        msg = args['msg'] +  '\ntime: ' + str(rospy.get_time())
        rospy.loginfo('Publishing ' +  msg)
        publisher.publish(msg)
        rate.sleep()

    # ----------------------------------------------
    # Termination
    # ----------------------------------------------

if __name__ == '__main__':
    main()
    # Comments to test vim
