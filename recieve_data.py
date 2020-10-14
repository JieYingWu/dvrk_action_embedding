import message_filters
import rospy
from std_msgs.msg import Int32, Float32
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState, Image
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
import os
import math
import sys

data_root = '/media/yhlong/DATA/Datasets/peg_transfer/2020-10-02/'
save_root = '/media/yhlong/DATA/Datasets/peg_transfer/'

bag_name = '2020-10-02-15-59-45'
count_frame = 0
save_frame = 1

if not os.path.exists(save_root+'image/'+bag_name):
	os.makedirs(save_root+'image/'+bag_name)

fw = open(save_root+'kinematics/'+bag_name+".txt", 'w')

def save_file(img_sub, psm1_cartesian_sub, psm1_state_jaw_sub, psm2_cartesian_sub, psm2_state_jaw_sub):
	global count_frame
	global save_frame

	bridge = CvBridge()
	cv_image = bridge.imgmsg_to_cv2(img_sub, "bgr8")
	cv_image = cv2.resize(cv_image,(320, 256))
	if count_frame % 3 == 0:
		cv2.imwrite(save_root+'image/'+bag_name+'/'+str(save_frame)+'.jpg', cv_image)
		save_frame += 1
		# PSM1 ========

		psm1_x = psm1_cartesian_sub.pose.position.x
		psm1_y = psm1_cartesian_sub.pose.position.y
		psm1_z = psm1_cartesian_sub.pose.position.z

		psm1_jaw = psm1_state_jaw_sub.position[0]

		w = psm1_cartesian_sub.pose.orientation.w
		x = psm1_cartesian_sub.pose.orientation.x
		y = psm1_cartesian_sub.pose.orientation.y
		z = psm1_cartesian_sub.pose.orientation.z

		psm1_angleR = math.atan2(2*(w*x+y*z),1-2*(x*x+y*y))*180/math.pi
		psm1_angleP = math.asin(2*(w*y-z*x))*180/math.pi
		psm1_angleY = math.atan2(2*(w*z+x*y),1-2*(z*z+y*y))*180/math.pi

		psm1_kinematics = '{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\t'\
							.format(psm1_x,psm1_y,psm1_z,psm1_angleR,psm1_angleP,psm1_angleY,psm1_jaw)
		
		# PSM2 ========

		psm2_x = psm2_cartesian_sub.pose.position.x
		psm2_y = psm2_cartesian_sub.pose.position.y
		psm2_z = psm2_cartesian_sub.pose.position.z

		psm2_jaw = psm2_state_jaw_sub.position[0]

		w = psm2_cartesian_sub.pose.orientation.w
		x = psm2_cartesian_sub.pose.orientation.x
		y = psm2_cartesian_sub.pose.orientation.y
		z = psm2_cartesian_sub.pose.orientation.z

		psm2_angleR = math.atan2(2*(w*x+y*z),1-2*(x*x+y*y))*180/math.pi
		psm2_angleP = math.asin(2*(w*y-z*x))*180/math.pi
		psm2_angleY = math.atan2(2*(w*z+x*y),1-2*(z*z+y*y))*180/math.pi

		psm2_kinematics = '{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\n'\
							.format(psm2_x,psm2_y,psm2_z,psm2_angleR,psm2_angleP,psm2_angleY,psm2_jaw)

		all_kinematics = psm1_kinematics + psm2_kinematics

		fw.write(all_kinematics)

	count_frame += 1

psm1_cartesian_sub = message_filters.Subscriber('/PSM1/position_cartesian_current', PoseStamped)
psm1_state_jaw_sub = message_filters.Subscriber('/PSM1/state_jaw_current', JointState)
psm2_cartesian_sub = message_filters.Subscriber('/PSM2/position_cartesian_current', PoseStamped)
psm2_state_jaw_sub = message_filters.Subscriber('/PSM2/state_jaw_current', JointState)
img_sub = message_filters.Subscriber('/jhu_daVinci/left/decklink/camera/image_raw', Image)

ts = message_filters.ApproximateTimeSynchronizer([img_sub, psm1_cartesian_sub, psm1_state_jaw_sub, psm2_cartesian_sub, psm2_state_jaw_sub],
												 10, 0.1, allow_headerless=True)
ts.registerCallback(save_file)
rospy.init_node('bag2file_node')
rospy.spin()
