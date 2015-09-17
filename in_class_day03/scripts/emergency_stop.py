#!/usr/bin/env python

"""ROS node to move robot forward until it bumps into an obstacle. When it hits an obstacle, it stops"""

import rospy
from neato_node.msg import Bump
from geometry_msgs.msg import Twist, Vector3

def process_bump(msg):
	global velocity_msg
	if (msg.rightFront or
		msg.leftFront or
		msg.rightSide or
		msg.leftSide):
		velocity_msg = Twist()

rospy.init_node('emergency_stop')
rospy.Subscriber("/bump", Bump, process_bump)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)



velocity_msg = Twist(linear=Vector3(x=.1))
r = rospy.Rate(10)
while not rospy.is_shutdown():
	pub.publish(velocity_msg)
	r.sleep