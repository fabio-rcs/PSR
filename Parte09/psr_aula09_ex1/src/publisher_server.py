#!/usr/bin/env python3

import rospy
from functools import partial
from psr_aula09_ex1.msg import Dog
from psr_aula09_ex1.srv import SetDogName, SetDogNameResponse


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
    dog = Dog() # Instantiating the Dog class
    dog.name = 'Isa'
    dog.color = 'Brown and white'
    dog.age = 4
    dog.brothers.append('Fabio')
    dog.brothers.append('Raquel')

    # Initialization of a ROS node
    rospy.init_node('publisher', anonymous=False)
    
    # ----------------------------------------------
    # Execution
    # ----------------------------------------------

    # Create the publisher
    publisher = rospy.Publisher('chatter', Dog, queue_size=10)

    # Create service
    service = rospy.Service('set_dog_name', SetDogName, partial(serviceRequestCallback, dog= dog))

    # Send message every x seconds
    rate = rospy.Rate(1) # hz

    while not rospy.is_shutdown():
        rospy.loginfo('Publishing ' + str(dog))
        publisher.publish(dog)
        rate.sleep()

    # ----------------------------------------------
    # Termination
    # ----------------------------------------------

if __name__ == '__main__':
    main()
