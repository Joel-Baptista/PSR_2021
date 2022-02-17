#!/usr/bin/env python3

import rospy
import tf_conversions
from geometry_msgs.msg import Quaternion
import tf2_ros
import geometry_msgs
import math


def nothing():
    pass


def main():

    rospy.init_node('dist', anonymous=False)
    sub1 = rospy.Subscriber("tf", Quaternion, nothing)
    sub2 = rospy.Subscriber("tf", Quaternion, nothing)

    rospy.spin()

if __name__ == '__main__':
    main()
