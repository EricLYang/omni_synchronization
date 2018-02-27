# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import message_filters
#from message_filters import ApproximateTimeSynchronizer, Subscriber
import os
import re
import numpy as np

from geometry_msgs.msg import PoseStamped, TransformStamped

#imageW=open('2018-02-22-15-38-34/imagePose.txt','w')
imageW=open('dataAssociatiion.txt','w')

init_time = 0.0
count = 1;

# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg, pose_msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
       
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        global count
        global init_time
        if count==1:
           init_time = msg.header.stamp.to_sec()
        cv2.imwrite('rgbImage/'+ str(count) +'.png', cv2_img)
     
        ## generate data association
        imageW.write(str(msg.header.stamp.to_sec() - init_time) + ' '+ str(pose_msg.transform.translation.x) + ' ' + str(pose_msg.transform.translation.y) + ' ' + str(pose_msg.transform.translation.z) +' '+str(pose_msg.transform.rotation.x) +' '+str(pose_msg.transform.rotation.y)+' '+str(pose_msg.transform.rotation.z)+' '+str(pose_msg.transform.rotation.w)+'\n')
        count = count + 1;
        

def main():
    rospy.init_node('rgbImage_listener')
    # Define your topics
    #image_topic = "/camera/rgb/image_rect_color"
    #depth_topic = "/camera/depth/image_rect"
    # Set up your subscriber and define its callback
    image_sub = message_filters.Subscriber("/camera/image_color", Image)
    pose_sub = message_filters.Subscriber("/vicon/hyperbolic_rig/hyperbolic_rig", TransformStamped)
    ts = message_filters.ApproximateTimeSynchronizer([image_sub, pose_sub], 10, 0.1)
    ts.registerCallback(image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
