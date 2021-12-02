#!/usr/bin/env python3

import rospy
from psr_aula8_ex3.msg import Dog
import colorama

def print_msg(msg):
    htc = rospy.get_param("/highlight_text_color")
    rospy.loginfo("Received a dog named " + getattr(colorama.Fore, htc) +
                  msg.name + colorama.Style.RESET_ALL +
                  ' which is ' + str(msg.age) +
                  ' years old')

def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------

    dog = Dog()
    dog.name = 'max'
    dog.age = 18
    dog.color = 'black'
    dog.brothers.append('lily')
    dog.brothers.append('boby')

    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)

    # pub2 = rospy.Publisher('A17', String, queue_size=10)

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    # create a dog message to sent

    while not rospy.is_shutdown():
        # text_to_send = args['message'] + str(rospy.get_time())

        print_msg(dog)
        pub.publish(dog)

        # pub2.publish('Aqui vai um para sul')
        # pub2.publish('Aqui vai um para sul')
        f = rospy.get_param("~frequency", default=1)
        rate = rospy.Rate(f)  # 10hz
        rate.sleep()
        # rospy.spin()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()
