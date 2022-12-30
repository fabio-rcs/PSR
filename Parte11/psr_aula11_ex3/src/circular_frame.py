#!/usr/bin/env python3
# --------------------------------------------------
# Fábio Sousa.
# PSR, December 2022.
# Part 11, Ex.3 
# --------------------------------------------------

import math
import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg


def main():
    rospy.init_node('circular_frame')

    radius = rospy.get_param('~radius', 3) # '~' for internal parameter
    speed = rospy.get_param('~speed', 0.1) # we need to be able to change these values
    revolution = rospy.get_param('~revolution', 0.3) 

    broadcaster = tf2_ros.TransformBroadcaster()

    rate = rospy.Rate(10) 
    theta = 0
    alpha = 0
    while not rospy.is_shutdown():

        t = geometry_msgs.msg.TransformStamped()
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = rospy.remap_name("parent") # Allows name changing when calling the function
        t.child_frame_id = rospy.remap_name('child')

        t.transform.translation.x = radius * math.cos(theta) # Rotation speed, we transform the user defined speed to polar coordinates (object rotates faster around central axis)
        t.transform.translation.y = radius * math.sin(theta)
        t.transform.translation.z = 0.0

        q = tf_conversions.transformations.quaternion_from_euler(0, 0, alpha) # We transform Euler rotational coordinates to quaternions
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        broadcaster.sendTransform(t)

        theta += speed
        if theta > 2*math.pi:
            theta = 0

        alpha += revolution
        if alpha > 2*math.pi:
            alpha = 0
        

        rate.sleep()


if __name__ == '__main__':
    main()