#!/usr/bin/env python3

import rospy
import argparse
from functools import partial
from psr_aula08_ex5.msg import Dog
from psr_aula08_ex5.srv import SetDogName, SetDogNameResponse


def serviceRequestCallback(request, dog):

    print('Received a request to change dog name to ' + request.new_name)
    dog.name = request.new_name # Change dog name
    response = SetDogNameResponse()
    response.result = 1

    return response


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

    dog = Dog() # Instantiating the Dog class
    dog.name = 'Isa'
    dog.color = 'Brown and white'
    dog.age = 4
    dog.brothers.append('Fabio')
    dog.brothers.append('Raquel')

    # Initialization of a ROS node
    rospy.init_node(args['node'], anonymous=False)
    
    # ----------------------------------------------
    # Execution
    # ----------------------------------------------

    # Create the publisher
    publisher = rospy.Publisher(args['topic'], Dog, queue_size=10)

    # Create service
    service = rospy.Service('set_dog_name', SetDogName, partial(serviceRequestCallback, dog= dog))

    # Send message every x seconds
    rate = rospy.Rate(args['frequency']) # hz

    while not rospy.is_shutdown():
        rospy.loginfo('Publishing ' +  str(dog))
        publisher.publish(dog)
        rate.sleep()

    # ----------------------------------------------
    # Termination
    # ----------------------------------------------

if __name__ == '__main__':
    main()
