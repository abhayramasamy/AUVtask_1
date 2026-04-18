import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from bot_interfaces.msg import BotPose
import sys
import select

class CommanderNode(Node):
	def __init__(self):
		super().__init__('commander')
		self.publisher_1 = self.create_publisher(String, '/cmd', 10)
		self.timer = self.create_timer(0.1, self.timer_callback)
		self.get_logger().info('Commander Node Started. Type your command and press Enter.')
	def timer_callback(self):
		if select.select([sys.stdin], [], [], 0)[0]:
			user_input = sys.stdin.readline().strip()
			if user_input:
                		msg = String()
                		msg.data = user_input
                		self.publisher_1.publish(msg)
                		self.get_logger().info(f'Published: {msg.data}')
def main(args=None):
    rclpy.init(args=args)
    node = CommanderNode()
    rclpy.spin(node) # This stays alive and triggers the timer
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
