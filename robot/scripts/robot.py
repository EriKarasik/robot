#!/usr/bin/env python3.8

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

flag = 0
wheelsPos = [-1, -1.5, -2, -2.5, -3, 3, 2.5, 2, 1.5, 1, 0.5, 0]
sholdersPos = [0.1, 0.2, 0.3, 0.4, 0.3, 0.2, 0.1, 0]

def talker():
    global flag, wheelsPas, sholdersPos
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10) # 10hz
    state = JointState()
    state.header = Header()
    state.header.stamp = rospy.Time.now()
    state.name = ['baseToFWheels', 'BackToSholders', 'BaseToBody', 'baseToBWheels']
    state.velocity = []
    state.effort = []
    while not rospy.is_shutdown():
      i = wheelsPos[flag % len(wheelsPos)]
      j = sholdersPos[flag % len(sholdersPos)]
      state.position = [i, j, i, i]
      state.header.stamp = rospy.Time.now()
      pub.publish(state)
      flag += 1
      rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
