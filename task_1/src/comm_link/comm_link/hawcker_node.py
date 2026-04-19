import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading

class HawckerNode(Node):

    def __init__(self):
        super().__init__('hawcker_node')
        self.pub = self.create_publisher(String, '/chat', 10)
        self.sub = self.create_subscription(
            String,
            '/chat',
            self.receive_cb,
            10
        )

    def receive_cb(self, msg):
        if not msg.data.startswith('[Hawcker]:'):
            print(f'\n{msg.data}')
            print('>>> ', end='', flush=True)

    def send(self, text):
        msg = String()
        msg.data = f'[Hawcker]: {text}'
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = HawckerNode()

    spin_thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    spin_thread.start()

    print('Hawcker ready. Type and hit Enter.\n')

    try:
        while True:
            text = input('>>> ')
            if text.strip():
                node.send(text.strip())
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
