# Task3 implementing ROS2 along with a FSM to navigate a node/robot

*To create a commander and navigator node where commander sends instructions using a custom datatype and navigator node implements movemnent and uses a FSM to track its current facing direction*

## workspace setup:
1) Note since we are implementing a FSM i decided to use `python-statemachine` library to handle FSM with ease to use `StateMachine` and `State` makes handling FSM easier
2) I decided to a python virtual environment inorder to safely install statemachine library in the end it didnt turn out too well(just documented the process).
3) run: `sudo pip3 install python-statemachine --break-system-packages` break system package is what i wanted to avoid and decided to go for venv in first place but in the end i ended up doing this anyway.
4) this time you need to setup two different things:
   ```
    ros2 pkg create --build-type ament_cmake bot_interfaces
    ros2 pkg create --build-type ament_python dead_reckoning
    mkdir -p bot_interfaces/msg
   ```
6) then inside BotPose.msg we need to configure custom datastype.
7) update `CMakeLists.txt` to do this:
   ```
   find_package(rosidl_default_generators REQUIRED)
    rosidl_generate_interfaces(${PROJECT_NAME}
    "msg/BotPose.msg"
    )
    ament_export_dependencies(rosidl_default_runtime)
   ```
9) update `package.xml`' in bot_interfface and dead__Reckoning(two different ones):
    ```
    <build_depend>rosidl_default_generators</build_depend>
    <exec_depend>rosidl_default_runtime</exec_depend>
    <member_of_group>rosidl_interface_packages</member_of_group>
    ```
    inside dead_reckoning:
    ```
    <depend>bot_interfaces</depend>
    ```
11) then usual build and run...

## New things learnt:
1) How to customize and handle custom datatype like importing and using it in a topic too.
2) Implementing a statemachine from statemachines library.

## Issues faced:
The python-statemachine library is not available via apt and not native to ROS2. Multiple approaches attempted in order:

1) Installed in a .venv ROS2 uses system Python, not the venv, so import failed at runtime
2) Debugging ModuleNotFoundErrors due to venv not having custom library files lieek em r numpy.
3) Added to setup.py install_requires colcon picked it up but ROS2 runtime still couldn't find it
4) sudo pip3 install statemachine --break-system-packages , this finally worked...


