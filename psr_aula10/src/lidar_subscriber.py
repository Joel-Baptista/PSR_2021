#!/usr/bin/env python3
import argparse
from sensor_msgs.msg import LaserScan
import rospy
import colorama


def callbackMsgReceived(msg):
    rospy.loginfo('Received Laser Scan')


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------


    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber('/left_laser/laserscan', LaserScan, callbackMsgReceived)


    # simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
