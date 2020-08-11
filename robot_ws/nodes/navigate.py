#!/usr/env python 
import rospy
from geometry_msgs.msg import Twist

#Twist are the 

class Navigator():
    def __init__(self):
        #ros publisher sends info to new nodes wheels of the robot ; fins queues to be sent ..10 is good msgs to be sent 
        self.cmd_vel_publisher = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    
    def move_forever(self):
        rotate_msg = Twist
        #liner vs angular vectors
        rotate_msg.angular.z = 0.5
        #while loop for the msg sending ...

        r = rospy.Rate(10) # 10 msgs per second 
        while not rospy.is_shutdown():
            self.cmd_vel_publisher.publish(rotate_msg)
            rospy.loginfo(" MOving forward  %s",rotate_msg) #log the information for moving forward.
            r.sleep() # robot sleeps or idle time ..



def move_forwared():
    print "moving forward"


def main():
    rospy.init_node('navigate')
    navigator = Navigator()
    navigator.move_forever() #instance of the class ...move forever forward /backward.

if __name__ == "__main__":
    main()

