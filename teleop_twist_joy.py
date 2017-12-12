import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class TeleopTwistJoy(Node):

    def __init__(self):
        super().__init__('teleop_twist_joy')
        self._joy_sub = self.create_subscription(Joy, 'joy', self.joy_callback)
        self._twist_pub = self.create_publisher(Twist, 'cmd_vel')
    
    def joy_callback(self, joy_msg):
        if joy_msg.buttons[0] == 1:
            twist = Twist()
            twist.linear.x = joy_msg.axes[1] * 0.2
            twist.angular.z = joy_msg.axes[0] * 3.14
            self._twist_pub.publish(twist)
        else:
            twist = Twist()
            twist.linear.x = 0.
            twist.angular.z = 0.
            self._twist_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)

    teleop_twist_joy = TeleopTwistJoy()
    rclpy.spin(teleop_twist_joy)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    teleop_twist_joy.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
