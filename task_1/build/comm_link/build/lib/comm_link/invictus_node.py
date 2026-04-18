import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class InvictusNode(Node):

    def __init__(self):
        super().__init__('invictus_node')

        self.pub = self.create_publisher(String, '/chat', 10)

        self.sub = self.create_subscription(
            String,
            '/chat',
            self.receive_cb,
            10
        )

    def receive_cb(self, msg):
        if not msg.data.startswith('[Invictus]:'):
            print(f'\n{msg.data}')
            print('>>> ', end='', flush=True)

    def send(self, text):
        msg = String()
        msg.data = f'[Invictus]: {text}'
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = InvictusNode()

    print('Invictus node started. Type your message and hit Enter.\n')

    while rclpy.ok():
        rclpy.spin_once(node, timeout_sec=0.1)

        text = input('>>> ')
        if text.strip():
            node.send(text.strip())

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
