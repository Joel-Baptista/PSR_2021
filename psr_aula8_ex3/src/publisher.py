#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_aula8_ex3.msg import Dog
from psr_aula8_ex3.srv import SetDogName, SetDogNameResponse


def ChangeName(req):
    global dog
    dog.name = req.new_name
    return SetDogNameResponse(True)


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--rate', type=float,default=1)
    args = vars(parser.parse_args())

    global dog

    dog = Dog()
    dog.name = 'max'
    dog.age = 18
    dog.color = 'black'
    dog.brothers.append('lily')
    dog.brothers.append('boby')


    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)
    ser = rospy.Service('name', SetDogName, ChangeName)

    # pub2 = rospy.Publisher('A17', String, queue_size=10)
    rate = rospy.Rate(args['rate'])  # 10hz

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    # create a dog message to sent

    while not rospy.is_shutdown():
        # text_to_send = args['message'] + str(rospy.get_time())

        rospy.loginfo(dog)
        pub.publish(dog)

        # pub2.publish('Aqui vai um para sul')
        # pub2.publish('Aqui vai um para sul')
        rate.sleep()
        # rospy.spin()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()
