#!/usr/bin/env python

"""ROS node to move robot forward until it bumps into an obstacle. When it hits an obstacle, it stops"""

import rospy
from sensor_msgs.msg import LaserScan
from neato_node.msg import Bump
from geometry_msgs.msg import Twist, Vector3
now = 0

def process_bump(msg):
	global velocity_msg
	if (msg.rightFront or
		msg.leftFront or
		msg.rightSide or
		msg.leftSide):
		velocity_msg = Twist(linear=Vector3(x=-.1))
def process_laser(msg):
	global now
	print msg.ranges[0]
	if (velocity_msg.linear.x < 0 and msg.ranges[0] >.7):
		velocity_msg.angular.z=-1
		velocity_msg.linear.x = 0
		now = rospy.get_time()

rospy.init_node('wall_bump')
rospy.Subscriber("/bump", Bump, process_bump)
rospy.Subscriber("/scan", LaserScan, process_laser)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)



velocity_msg = Twist(linear=Vector3(x=.1))
r = rospy.Rate(10)
while not rospy.is_shutdown():
	pub.publish(velocity_msg)
	print rospy.get_time()
	print now
	if rospy.get_time()-now > 1 and rospy.get_time()-now<3:
		velocity_msg.linear.x=1
		velocity_msg.angular.z=0
		now = 0
	r.sleep