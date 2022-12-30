#!/usr/bin/env python3
# --------------------------------------------------
# Fábio Sousa.
# PSR, December 2022.
# --------------------------------------------------

import math
from functools import partial
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from std_msgs.msg import ColorRGBA
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from matplotlib import cm

def msgReceivedCallback(msg, publisher):

    # Create a list of colors
    my_cm = cm.Pastel1(np.linspace(0, 1, 70))    

    rospy.loginfo("I received a new laser scan msg")

    # Cluster the laser scan msg
    threshold = 0.5

    clusters = [] # list of lists of point idxs

    # Initialization 
    # Set the first point as only idx in the first cluster
    clusters.append([0])

    # Iterate over all points and decide wether to create a new cluster or add to the existing cluster
    for idx in range(1, len(msg.ranges)):
        r_current = msg.ranges[idx]
        r_previous = msg.ranges[idx-1]

        # A new cluster is created when r difference (distance of point to center) is bigger than threshold
        if abs(r_current - r_previous) < threshold: # This point belongs to the last group
            clusters[-1].append(idx) # Append the point to last cluster
        else: # This point is from a new group
            clusters.append([idx])


    print('Found' , str(len(clusters)) + ' clusters') 

    # Create a visualization_msgs marker that will contain a list of spheres
    marker = Marker()
    marker.header.frame_id = 'left_laser' #Referential
    marker.ns = 'my_drawings'
    marker.id = 0
    marker.type = Marker.SPHERE_LIST
    marker.action = Marker.MODIFY

    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0
    marker.pose.orientation.y = 0
    marker.pose.orientation.z = 0
    marker.pose.orientation.w = 1

    # Size of the spheres
    marker.scale.x = 0.4
    marker.scale.y = 0.4
    marker.scale.z = 0.4

    # Color and transparency
    marker.color.r = 1
    marker.color.g = 0
    marker.color.b = 0
    marker.color.a = 0.7


    for idx in range(0, len(msg.ranges)):
        alpha = msg.angle_min + idx * msg.angle_increment
        r = msg.ranges[idx]
        
        # Create a point and add them to points list
        point = Point()
        point.x = r * math.cos(alpha)
        point.y = r * math.sin(alpha)
        point.z = 0
        marker.points.append(point)

        cluster_count = 0
        for cluster in clusters:
            if idx in cluster:
                cluster_idx = cluster_count
                break 
            cluster_count += 1

        # print('Point idx' , str(idx) + ' belongs to cluster ' + str(cluster_idx))

        # Give each cluster a different color, using the cluster index in the created colormap
        r = my_cm[cluster_idx,0] # Get the color from the colormap of the corresponding cluster
        g = my_cm[cluster_idx,1]
        b = my_cm[cluster_idx,2]
        color = ColorRGBA(r=r, g=g, b=b, a=0.7)
        marker.colors.append(color)

    publisher.publish(marker) 


    
def main():

    # ------------------------------------
    # Initialization 
    # ------------------------------------

    # Initialization of a ros node
    rospy.init_node('lidar_subscriber', anonymous=False)

    publisher = rospy.Publisher('~clusters', Marker, queue_size=1)

    # Init the subscriber
    subscriber = rospy.Subscriber('/left_laser/laserscan', LaserScan, partial(msgReceivedCallback, publisher=publisher))

    # ------------------------------------
    # Execution 
    # ------------------------------------
    rospy.spin()

    # ------------------------------------
    # Termination 
    # ------------------------------------

if __name__ == '__main__':
    main()