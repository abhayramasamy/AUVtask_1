# TASK 1: Implementing two simple chatting nodes

*Our task here is to implement two nodes in two different terminals that are able to send messages with each other using a simple publisher subscriber concept*

## Workspace setup:
1) used simple bash commands ot navigate to required directory like mkdir, cd and `ros2 pkg create --build-type ament_python comm_link`
2) after completion one must go to `setup.py` to configure console_scripts to specify executable files
```
'console_scripts': [
    'invictus_node = comm_link.invictus_node:main',
    'hawcker_node = comm_link.hawcker_node:main',
],
```
4) colcon build,source setup.bash in install folder and execute in different terminals.

## Approach:
1) Initially just used a simple rclpy.spin() in a loop with input() but faced syncing issues between two terminals since ros2 uses a queue, faced delay issues between two nodes.
2) explored how to ensure background tasks kept running while user provides input...
3) decided use threading and included rclpy.spin() in a thread in a backgroung deamon to ensure the output keeps printing while user can type input.
4) both users subscribe to same topic
5) requires self filtering since: ros2 node publishes data to publisher  too , simplyy used msg.data.startswith('[Username]:') a simpl solution

## issues faced:
1) implementing threading
2) accidentally initialized git inside task_1 instead of parent directory had to remove and reconfigure git.
3) later removed build log and install as they are not necessary
