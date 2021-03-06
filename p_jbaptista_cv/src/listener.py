#!/usr/bin/env python3

import argparse

import rospy
from std_msgs.msg import String
from p_jbaptista_cv.msg import PlayerLocation
import numpy as np
import sys



def callbackMsgReceived(msg):
    for i in msg.idx:
        x = np.around(msg.locations[i].pose.position.x, 3)
        y = np.around(msg.locations[i].pose.position.y, 3)
        frame = msg.locations[i].header.frame_id
        rospy.loginfo("Player found number " + str(i + 1) + " is in team " + msg.teams[i] + " and in position (" + str(x) + "," + str(y) + ")"
                      + " in the frame " + frame)




def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    # parser = argparse.ArgumentParser(description='PSR argparse example.')
    # parser.add_argument('--topic', type=str, default='chatter')
    # parser.add_argument('--name', type=str, default="Sr. Pintarolas")
    # args = vars(parser.parse_args())

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/red1/player_location", PlayerLocation, callbackMsgReceived)

    # rospy.wait_for_service('name')
    # name = rospy.ServiceProxy('name', SetDogName)

    #
    # resp1 = name(args["name"])


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()

