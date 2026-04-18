#!/home/abhay-ramasamy/AUVT1/.venv/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from bot_interfaces.msg import BotPose

from statemachine import StateMachine, State
class DirectionFSM(StateMachine):
	north = State(initial=True)
	south = State()
	west=State()
	east=State() 
	
	turn_right = north.to(east) | east.to(south) | south.to(west) | west.to(north)
	turn_left  = north.to(west) | west.to(south) | south.to(east) | east.to(north)
	reverse    = north.to(south) | south.to(north) | east.to(west) | west.to(east)
	
	def forward(self):
		pass
		#nothing here for now to add moving code later actually :)
	
"""
TEST CODE:    #this code actuallly works well enough
robot = DirectionFSM()
print(robot.configuration)
robot.turn_left()
print(robot.configuration)
robot.turn_right()
print(robot.configuration)
robot.turn_right()
print(robot.configuration)
robot.reverse()
"""
		
class Navigator(Node):
	def __init__(self):
		super().__init__('navigator')
		#initialize the state
		self.x = 0.0
		self.y = 0.0
		self.state = DirectionFSM()
		self.subscription = self.create_subscription(String, '/cmd', self.listener_callback, 10)
		self.publisher = self.create_publisher(BotPose, '/bot_pose', 10)
		
	def listener_callback(self, msg):
		command = msg.data
		if command == 'turn right':
			self.state.turn_right()
		elif command == 'turn left':
			self.state.turn_left()
		elif command == 'reverse':
			self.state.reverse()
		elif command == 'forward':
			self.move_forward()
		else:
			self.get_logger().error('Command unrecognized!!!')
		pose_msg = BotPose()
		pose_msg.x = self.x
		pose_msg.y = self.y
		pose_msg.facing_direction = (list(self.state.configuration)[0].id)
		self.publisher.publish(pose_msg) 
		self.get_logger().info(f'Pose: ({self.x}, {self.y}), Facing: {self.state}')
	def move_forward(self):
		if(list(self.state.configuration)[0].id == 'north'):
			self.y+=1.0
		elif(list(self.state.configuration)[0].id == 'east'):
			self.x+=1.0
		elif(list(self.state.configuration)[0].id == 'west'):
			self.x-=1.0
		elif(list(self.state.configuration)[0].id == 'south'):
			self.y-=1.0
		
def main(args=None):
    rclpy.init(args=args)
    node = Navigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown() 
if __name__ == "__main__":
    main()
