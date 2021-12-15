#!/usr/bin/env python3

import rospy
import tf_conversions
from geometry_msgs.msg import Quaternion
import tf2_ros
import geometry_msgs
import math


def main():

    rospy.init_node('tf2_broadcaster', anonymous=False)
    pub = rospy.Publisher('world', Quaternion, queue_size=10)

    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.frame_id = rospy.get_param("~parent")
    t.child_frame_id = rospy.get_param("~name")
    rate = rospy.Rate(20*rospy.get_param("~frequency"))

    q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    theta_inc = math.pi/500
    theta = 0
    r = 3*rospy.get_param(("~radius"))
    while not rospy.is_shutdown():
        x = r*math.cos(theta)
        y = r*math.sin(theta)

        # print((x, y, theta))

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = 0

        br.sendTransform(t)

        theta = theta + theta_inc
        rate.sleep()


if __name__ == '__main__':
    main()
