# Task2, implementing a 3 node communication chain

*to setup three different nodes using two different topics and preforms different actions with data they recieve from publisher and publish to next channel*
## workspace setup:
1) Navigate to your appropriate directory and run this line to build pkgs `ros2 pkg create --build-type ament_python signal_pipeline`
2) open the files in `src/signal_pipeline/signal_pipeline` and edit if necessary
3) setup.py configure:
      ```
   'console_scripts': [
    'publisher_node = signal_pipeline.publisher_node:main',
    'processor_node = signal_pipeline.processor_node:main',
    'output_node = signal_pipeline.output_node:main',
    ],```
5) build the ros2 packages using `colcon build` and `source install/setup.bash` and run in each terminal `ros2 run signal_pipeline <publisher_node/processor_node/output_node>`

## Some new things learnt here:
1) used `self.timer = self.create_timer(1.0, <call back function>)` to regularly call a fun using ros2 timer
2) general pub/sub handling

## issues faced:
none for this project

