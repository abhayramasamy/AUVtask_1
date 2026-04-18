import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class ProcessorNode(Node):

    def __init__(self):
        super().__init__('processor_node')
        self.sub = self.create_subscription(Int64, '/raw_signal', self.receive_cb, 10)
        self.pub = self.create_publisher(Int64, '/processed_signal', 10)

    def receive_cb(self, msg):
        result = msg.data * 5
        out = Int64()
        out.data = result
        self.pub.publish(out)
        self.get_logger().info(f'Received: {msg.data} → Published: {out.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ProcessorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
