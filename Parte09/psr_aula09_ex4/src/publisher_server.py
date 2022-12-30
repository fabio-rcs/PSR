#!/usr/bin/env python3

import rospy
from functools import partial
from psr_aula09_ex4.msg import Dog
from psr_aula09_ex4.srv import SetDogName, SetDogNameResponse
from colorama import Fore, Style

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

    # Gets frequency parameter
    frequency = rospy.get_param("/frequency", 1) # Private parameter

    # Send message every x seconds
    rate = rospy.Rate(frequency) # hz

    while not rospy.is_shutdown():

        # Gets text color parameter
        highlight_text_color = rospy.get_param("/highlight_text_color", 'CYAN') # Global parameter 

        rospy.loginfo('Publishing ' + getattr(Fore, highlight_text_color) + str(dog) + Style.RESET_ALL)
        publisher.publish(dog)
        rate.sleep()

    # ----------------------------------------------
    # Termination
    # ----------------------------------------------

if __name__ == '__main__':
    main()
