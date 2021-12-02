#!/usr/bin/env python3
import argparse

import rospy
from psr_aula8_ex3.msg import Dog
import colorama


def callbackMsgReceived(msg):
    htc = rospy.get_param("/highlight_text_color")
    rospy.loginfo("Received a dog named " + getattr(colorama.Fore, htc) +
                  msg.name + colorama.Style.RESET_ALL +
                  ' which is ' + str(msg.age) +
                  ' years old')


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', Dog, callbackMsgReceived)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()

