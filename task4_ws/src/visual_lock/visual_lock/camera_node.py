import rclpy

from rclpy.node import Node
import cv2
import numpy as np
from statemachine import StateMachine, State

class VisualFSM(StateMachine):
    lost    = State(initial=True)
    left    = State()
    centre  = State()
    right   = State()

    find        = lost.to(left) | lost.to(centre) | lost.to(right)
    align_left  = centre.to(left) | right.to(left)
    align_right = centre.to(right) | left.to(right)
    lock        = left.to(centre) | right.to(centre)
    lose        = left.to(lost) | centre.to(lost) | right.to(lost)

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.cap = cv2.VideoCapture(0)
        self.fsm = VisualFSM()
        self.create_timer(0.033, self.timer_callback)

    def get_zone(self, cx, width):
        third = width // 3
        if cx < third:
            return 'left'
        elif cx < 2 * third:
            return 'centre'
        else:
            return 'right'

    def transition(self, zone):
        current = list(self.fsm.configuration)[0].id
        if zone is None:
            if current != 'lost':
                self.fsm.lose()
        elif current == 'lost':
            self.fsm.find()
        elif zone == 'left' and current != 'left':
            self.fsm.align_left()
        elif zone == 'right' and current != 'right':
            self.fsm.align_right()
        elif zone == 'centre' and current != 'centre':
            self.fsm.lock()

    def apply_filter(self, frame):
        current = list(self.fsm.configuration)[0].id
        if current == 'left':
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        elif current == 'centre':
            return frame
        elif current == 'right':
            edges = cv2.Canny(frame, 100, 200)
            return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        elif current == 'lost':
            return cv2.bitwise_not(frame)

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error('Failed to read frame')
            return

        width = frame.shape[1]
        hsv   = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100, 150, 50])
        upper_blue = np.array([140, 255, 255])
        mask       = cv2.inRange(hsv, lower_blue, upper_blue)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        zone = None
        if contours:
            c = max(contours, key=cv2.contourArea)
            if cv2.contourArea(c) > 500:
                M    = cv2.moments(c)
                cx   = int(M['m10'] / M['m00'])
                zone = self.get_zone(cx, width)

        self.transition(zone)
        self.get_logger().info(f'State: {list(self.fsm.configuration)[0].id.upper()}')

        output = self.apply_filter(frame)
        cv2.imshow('Visual Lock', output)
        cv2.waitKey(1)

    def destroy_node(self):
        self.cap.release()
        cv2.destroyAllWindows()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
