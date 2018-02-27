# ros_data_acquisition
The ros script to synchronize the data from the camera and Vicon Transform. The save association follows the form:

>- time (relative to intial) p.x p.y p.z q.x q.y q.z q.w


# python side vicon data publisher

Please follow the follow step to run.

(1) Creat a folder to save the rgb images:
> - mkdir rgbImage


(2) start roscore

(3) run the python scipt:
> - python imageSaveAndAssociate.py

(4) rosplay the bag use the command(please slow the rate, however, still big problem to synchronize the data):

>- rosbag play -r 0.1 /path/and/bag/name


## TODO
Allow more time synchronization allowance.


