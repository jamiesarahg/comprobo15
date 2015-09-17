#!/usr/bin/env python

"""ROS node to move robot forward until it bumps into an obstacle. When it hits an obstacle, it stops"""

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3

def process_laser(msg):
	global velocity_msg
	for item in msg.ranges:
		if (item < .5 and item >msg.min_range):
			print item
			velocity_msg = Twist()

rospy.init_node('new_emergency_stop')
rospy.Subscriber("/scan", LaserScan, process_laser)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)



velocity_msg = Twist(linear=Vector3(x=.1))
r = rospy.Rate(10)
while not rospy.is_shutdown():
	pub.publish(velocity_msg)
	r.sleep