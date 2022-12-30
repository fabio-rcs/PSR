#!/usr/bin/env python3
# --------------------------------------------------
# Fábio Sousa.
# PSR, December 2022.
# Part 11, Ex.4
# --------------------------------------------------

import math
import rospy
import tf


def main():

    rospy.init_node('listener_mercury_to_moon')

    listener = tf.TransformListener() # Object from ROS, the TF listener

   
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('mercury', 'moon', rospy.Time(0))
        
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print('Could not get get the transformation')
            continue

        distance = math.sqrt(trans[0]**2 + trans[1]**2) # Distance is in xyz, to get the direct distance we need to calculate the vector distance. Z is zero, there's no need to add it
        print('Distance from mercury to moon is ' + str(distance))

        rate.sleep()

if __name__ == '__main__':
    main()