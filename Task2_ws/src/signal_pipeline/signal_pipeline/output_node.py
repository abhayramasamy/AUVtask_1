import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class OutputNode(Node):

    def __init__(self):
        super().__init__('output_node')
        self.sub = self.create_subscription(Int64, '/processed_signal', self.receive_cb, 10)

    def receive_cb(self, msg):
        final = msg.data + 10
        self.get_logger().info(f'Final result: {final}')

def main(args=None):
    rclpy.init(args=args)
    node = OutputNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
