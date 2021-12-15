#!/usr/bin/env python
# license removed for brevity
import random

import rospy
import visualization_msgs.msg
from std_msgs.msg import String, ColorRGBA, Header
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3


def main():
    rospy.init_node('talker', anonymous=False)
    pub = rospy.Publisher('markers', MarkerArray, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    count = 0
    increment = 0.1

    # Segundo marcador

    marker2 = Marker()

    marker2.ns = 'Sphere'
    # marker2.id = 0

    marker2.header = Header(stamp=rospy.Time.now(), frame_id='world')

    marker2.type = Marker.SPHERE_LIST

    scale = Vector3(x=1, y=1, z=1)
    marker2.scale = scale

    color = ColorRGBA(r=1, g=0, b=1, a=0.5)
    marker2.color = color

    marker2.points = []

    for i in range(0, 50):
        x = random.randint(-3, 3)
        y = random.randint(-3, 3)
        z = random.randint(-1, 1)
        marker2.points.append(Point(x=x, y=y, z=z))

    while not rospy.is_shutdown():
        marker_array = MarkerArray()

        count += increment
        marker = Marker()

        marker.ns = 'Cube'
        # marker.id = 1

        marker.header = Header(stamp=rospy.Time.now(), frame_id='world')

        marker.type = Marker.CUBE

        point = Point(x=count, y=0, z=0)
        quaternion = Quaternion(x=0, y=0, z=0, w=1)
        marker.pose = Pose(position=point, orientation=quaternion)

        scale = Vector3(x=count, y=1, z=1)
        marker.scale = scale

        color = ColorRGBA(r=1, g=0, b=0, a=1)
        marker.color = color

        marker_array.markers.append(marker)

        point = Point(x=count, y=0, z=0)
        quaternion = Quaternion(x=0, y=0, z=0, w=1)
        marker2.pose = Pose(position=point, orientation=quaternion)

        marker_array.markers.append(marker2)
        #
        # pub.publish(marker2)
        # pub.publish(marker)
        pub.publish(marker_array)

        rospy.loginfo('Publishing marco')
        rate.sleep()

        if count > 3 or count < -3:
            increment = -increment


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass