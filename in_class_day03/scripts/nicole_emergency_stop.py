#!/usr/bin/env python
'''Using the cmd_vel topic tells the robot to move forward turn left then
repeat 4 times then finally stops'''
import rospy
import time
from geometry_msgs.msg import Twist
from neato_node.msg import Bump

class Emergency_Stop(object):
  def __init__(self, starting_vel):
    rospy.Subscriber("/bump", Bump, self.callback)
    self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('emergency_stop')
    # self.is_bumped=false
    self.twist = Twist()
    self.x_vel = starting_vel

  def callback(self, data):
    bump_sensors = [data.leftFront, data.leftSide, data.rightFront, data.rightSide]
    for hit in bump_sensors:
      if hit:
        self.x_vel=0
  def run(self):
    self.twist.linear.x = self.x_vel; self.twist.linear.y = 0; self.twist.linear.z = 0
    self.twist.angular.x = 0; self.twist.angular.y = 0; self.twist.angular.z = 0
    self.pub.publish(self.twist)
    print self.x_vel
   
if  __name__=='__main__':
  e_stop = Emergency_Stop(1)
  while not rospy.is_shutdown():
    e_stop.run()