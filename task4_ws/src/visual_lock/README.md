# Task4) implementing a CV2 pipeline in ROS2 along with a FSM 

*Vision-based FSM that applies different visual filters based on tracked object position on screen*
## workspace setup:
1) navigate to the folder and `ros2 pkg create --build-type ament_python visual_lock`
2) open edit files
3) most importantly: `sudo apt install python3-opencv` decided to use apt not pip.
4) build and run.
5) Note: due to non availbaility of webcam in a vm i decided to use DroidCam app to virtually connect my phone camera to my VM.

## New things learnt:
1) Some important opencv functions and methods, to apply filters, contouring.
2) building a ros2 pipeline for opencv and integrating a basic FSM.

## issues faced:
1) seting up droidcam as it always jammed after multiple running and need to be cleared up.
