#!/usr/bin/env python3

import math
import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg


def main():
    rospy.init_node('circular_frame')

    broadcaster = tf2_ros.TransformBroadcaster()
    radius = 3
    rate = rospy.Rate(10) 
    theta = 0
    alpha = 0
    while not rospy.is_shutdown():

        t = geometry_msgs.msg.TransformStamped()
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "parent"
        t.child_frame_id = 'child'

        t.transform.translation.x = radius * math.cos(theta)
        t.transform.translation.y = radius * math.sin(theta)
        t.transform.translation.z = 0.0

        q = tf_conversions.transformations.quaternion_from_euler(0, 0, 30*math.pi/180.0)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        broadcaster.sendTransform(t)

        theta += 0.1
        if theta > 2*math.pi:
            theta = 0        

        rate.sleep()


if __name__ == '__main__':
    main()