import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.pub = self.create_publisher(Int64, '/raw_signal', 10)
        self.counter = 1
        self.create_timer(1.0, self.timer_cb)

    def timer_cb(self):
        msg = Int64()
        msg.data = self.counter * 2
        self.pub.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
