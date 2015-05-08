#!/usr/bin/env python

from irpos import *
import numpy as np
# DEMO FUNCTIONS

# POSTUMENT DEMOS

def irp6p_multi_trajectory():
	irpos = IRPOS("IRpOS", "Irp6p", 6)

	motor_trajectory = [JointTrajectoryPoint([0.4, -1.5418065817051163, 0.0, 1.57, 1.57, -2.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [], [], rospy.Duration(10.0)), JointTrajectoryPoint([10.0, 10.0, 0.0, 10.57, 10.57, -20.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [], [], rospy.Duration(12.0))]
        irpos.move_along_motor_trajectory(motor_trajectory)

	joint_trajectory = [JointTrajectoryPoint([0.4, -1.5418065817051163, 0.0, 1.5, 1.57, -2.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [], [], rospy.Duration(3.0)),JointTrajectoryPoint([0.0, -1.5418065817051163, 0.0, 1.5, 1.57, -2.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [], [], rospy.Duration(6.0))]
	irpos.move_along_joint_trajectory(joint_trajectory)

	rot = PyKDL.Frame(PyKDL.Rotation.EulerZYZ(0.0, 1.4, 3.14), PyKDL.Vector(0.705438961242, -0.1208864692291, 1.18029263241))
	rot2 = PyKDL.Frame(PyKDL.Rotation.EulerZYZ(0.3, 1.4, 3.14), PyKDL.Vector(0.705438961242, -0.1208864692291, 1.181029263241))
	cartesianTrajectory = [CartesianTrajectoryPoint(rospy.Duration(3.0), Pose(Point(0.705438961242, -0.1208864692291, 1.181029263241), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)), Twist()), CartesianTrajectoryPoint(rospy.Duration(6.0), pm.toMsg(rot), Twist()),CartesianTrajectoryPoint(rospy.Duration(9.0), pm.toMsg(rot2), Twist())]
	irpos.move_along_cartesian_trajectory(cartesianTrajectory)

	toolParams = Pose(Point(0.0, 0.0, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0))
	irpos.set_tool_geometry_params(toolParams)

	rot = PyKDL.Frame(PyKDL.Rotation.EulerZYZ(0.0, 1.4, 3.14), PyKDL.Vector(0.705438961242, -0.1208864692291, 1.181029263241))
	cartesianTrajectory = [CartesianTrajectoryPoint(rospy.Duration(3.0), Pose(Point(0.705438961242, -0.1208864692291, 1.181029263241), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)), Twist()),
CartesianTrajectoryPoint(rospy.Duration(6.0), pm.toMsg(rot), Twist()),CartesianTrajectoryPoint(rospy.Duration(9.0), Pose(Point(0.705438961242, -0.1208864692291, 1.181029263241), Quaternion(0.63691, 0.096783, 0.75634, -0.11369)), Twist())]
	irpos.move_along_cartesian_trajectory(cartesianTrajectory)

	toolParams = Pose(Point(0.0, 0.0, 0.25), Quaternion(0.0, 0.0, 0.0, 1.0))
	irpos.set_tool_geometry_params(toolParams)

	print "Irp6p 'multi_trajectory' test compleated"


def T1():
	irpos = IRPOS("IRpOS", "Irp6p", 6)

	
	cartesianTrajectory = [CartesianTrajectoryPoint(rospy.Duration(6.0), Pose(Point(0.8, 0.0, 1.3), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)), Twist()) , CartesianTrajectoryPoint(rospy.Duration(12.0), Pose(Point(0.8, 0.1, 1.3), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)), Twist()) , CartesianTrajectoryPoint(rospy.Duration(18.0), Pose(Point(0.8, 0.1, 1.4), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)), Twist()) , CartesianTrajectoryPoint(rospy.Duration(24.0), Pose(Point(0.8, 0.0, 1.4), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)), Twist()) , CartesianTrajectoryPoint(rospy.Duration(30.0), Pose(Point(0.8, 0.0, 1.3), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)), Twist())  ]
	irpos.move_along_cartesian_trajectory(cartesianTrajectory)


	print "Irp6p: Behavior: T1 - done."
	
def T2():
	irpos = IRPOS("IRpOS", "Irp6p", 6)

	print "Irp6p: Behavior: T2 - Starting."
	joint_trajectory = [JointTrajectoryPoint([0.0, -1.5707963268, 0.0, 0.0, 4.7123889804 , 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [], [], rospy.Duration(10.0))]
	irpos.move_along_joint_trajectory(joint_trajectory)
	
	


	print "Irp6p: Behavior: T2 - done."

def T3():
	irpos = IRPOS("IRpOS", "Irp6ot", 7)

	print "Irp6ot: Behavior: T3 - Starting."
	irpos.move_to_synchro_position(5.0)
	joint_trajectory = [JointTrajectoryPoint([0.3,0.0, -1.5707963268, 0.0, 0.0, 4.7123889804 , 0.0], [0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [], [], rospy.Duration(5.0))]
	irpos.move_along_joint_trajectory(joint_trajectory)
	
	


	print "Irp6ot: Behavior: T3 - done."

def T4():
	#irpos = IRPOS("IRpOS", "Irp6ot", 7 , "irp6ot_manager")
	irpos = IRPOS("IRpOS", "Irp6ot", 7)
	print "Irp6ot: Behavior: T4 - Starting."
	irpos.move_to_synchro_position(10.0)
	joint_trajectory = [JointTrajectoryPoint([0.0,0.0, -1.5707963268, 0.0, 0.0, 4.7123889804 , 0.0], [0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [], [], rospy.Duration(15.0))]
	irpos.move_along_joint_trajectory(joint_trajectory)
	

	print "Irp6ot: Behavior: T4 - done."
	
def T5():
	#irpos = IRPOS("IRpOS", "Irp6ot", 7 , "irp6ot_manager")
	irpos = IRPOS("IRpOS", "Irp6ot", 7)
	print "Irp6ot: Behavior: T5 - Rise!."
	
	
	irpos.move_rel_to_cartesian_pose(15.0, Pose(Point(0.0, 0.0, -0.15), Quaternion(0.0, 0.0, 0.0, 1.0)))
	#print str(irpos.get_tfg_joint_position())

	print "Irp6ot: Behavior: T5 - done."
	
def T6():
	#irpos = IRPOS("IRpOS", "Irp6ot", 7 , "irp6ot_manager")
	irpos = IRPOS("IRpOS", "Irp6ot", 7)
	print "Irp6ot: Behavior: T6 - Grabbing."
	
	irpos.tfg_to_joint_position(0.064, 10.0)
	
	print str(irpos.get_tfg_joint_position())

	print "Irp6ot: Behavior: T6 - done."

def TC():
	#irpos = IRPOS("IRpOS", "Irp6ot", 7 , "irp6ot_manager")
	irpos = IRPOS("IRpOS", "Irp6ot", 7)
	print "Irp6ot: Behavior: TC - decendt to contact."
	
	irpos.move_to_synchro_position(10.0)
	joint_trajectory = [JointTrajectoryPoint([0.0,0.0, -1.5707963268, 0.0, 0.0, 4.7123889804 , 0.0], [0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [], [], rospy.Duration(15.0))]
	irpos.move_along_joint_trajectory(joint_trajectory)
	#irpos.move_rel_to_cartesian_pose(10.0, Pose(Point(0.0, 0.0, -0.03), Quaternion(0.0, 0.0, 0.0, 1.0)))	
	irpos.move_rel_to_cartesian_pose_with_contact( 20.0, Pose(Point(0.0, 0.0, 0.20), Quaternion(0.0, 0.0, 0.0, 1.0)),Wrench(Vector3(10.0, 10.0, 4.0), Vector3(0.0, 0.0, 0.0)))
	irpos.move_rel_to_cartesian_pose(2.0, Pose(Point(0.0, 0.0, -0.01), Quaternion(0.0, 0.0, 0.0, 1.0)))
	#irpos.move_rel_to_cartesian_pose(2.0, Pose(Point(0.01, 0.0, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0)))
	irpos.move_rel_to_cartesian_pose_with_contact( 20.0, Pose(Point(0.20, 0.0, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0)),Wrench(Vector3(6.0, 6.0, 6.0), Vector3(0.0, 0.0, 0.0)))
	#time.sleep(6.0)
	P1 = irpos.get_cartesian_pose()
	print str(P1)
	P1x = P1.position.x
	P1y = P1.position.y
	P1z = P1.position.z
	time.sleep(1.0)
	irpos.move_rel_to_cartesian_pose_with_contact( 30.0, Pose(Point(-0.30, 0.0, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0)),Wrench(Vector3(8.0, 8.0, 8.0), Vector3(0.0, 0.0, 0.0)))
	P2 = irpos.get_cartesian_pose()
	print str(P2)
	P2x = P2.position.x
	P2y = P2.position.y
	P2z = P2.position.z
	time.sleep(1.0)
	irpos.move_rel_to_cartesian_pose_with_contact( 20.0, Pose(Point(0.0, -0.20, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0)),Wrench(Vector3(6.0, 6.0, 6.0), Vector3(0.0, 0.0, 0.0)))
	P3 = irpos.get_cartesian_pose()
	print str(P3)
	P3x = P3.position.x
	P3y = P3.position.y
	P3z = P3.position.z
	time.sleep(1.0)
	
	A = np.array([P1x, P1y, P1z])
	B = np.array([P2x, P2y, P2z])
	C = np.array([P3x, P3y, P3z])
	a = np.linalg.norm(C - B)
	b = np.linalg.norm(C - A)
	c = np.linalg.norm(B - A)
	s = (a + b + c) / 2
	R = a*b*c / 4 / np.sqrt(s * (s - a) * (s - b) * (s - c))
	b1 = a*a * (b*b + c*c - a*a)
	b2 = b*b * (a*a + c*c - b*b)
	b3 = c*c * (a*a + b*b - c*c)
	P = np.column_stack((A, B, C)).dot(np.hstack((b1, b2, b3)))
	P /= b1 + b2 + b3
	
	
	print P
	print P[0]
	T = P - C 
	print T
	time.sleep(1.0)
	
	irpos.move_rel_to_cartesian_pose( 20.0, Pose(Point(T[1],T[0] , 0.0), Quaternion(0.0, 0.0, 0.0, 1.0)))
	time.sleep(10.0)
	#move_to_cartesian_pose(20.0, Pose(P1))
	#irpos.move_rel_to_cartesian_pose(6.0, Pose(Point(-0.08, 0.0, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0)))
	irpos.move_rel_to_cartesian_pose(15.0, Pose(Point(0.0, 0.0, -0.14), Quaternion(0.0, 0.0, 0.0, 1.0)))
	irpos.move_to_synchro_position(10.0)
	
	print "Irp6ot: Behavior: TC - done. Current position at center"
		
def TSynch():
	#irpos = IRPOS("IRpOS", "Irp6ot", 7 , "irp6ot_manager")
	irpos = IRPOS("IRpOS", "Irp6ot", 7)
	print "Irp6ot: Behavior: TS - Synchronizing."
	irpos.move_to_synchro_position(10.0)

	print "Irp6ot: Behavior: TS - done."

def irp6p_multi_trajectory2():
	irpos = IRPOS("IRpOS", "Irp6p", 6)

	irpos.move_to_motor_position([0.4, -1.5418065817051163, 0.0, 1.57, 1.57, -2.0], 10.0)
	irpos.move_to_motor_position([10.0, 10.0, 0.0, 10.57, 10.57, -20.0], 2.0)

	irpos.move_to_joint_position([0.4, -1.5418065817051163, 0.0, 1.5, 1.57, -2.0], 3.0)
	irpos.move_to_joint_position([0.0, -1.5418065817051163, 0.0, 1.5, 1.57, -2.0], 3.0)

	rot = PyKDL.Frame(PyKDL.Rotation.EulerZYZ(0.0, 1.4, 3.14), PyKDL.Vector(0.705438961242, -0.1208864692291, 1.18029263241))
	rot2 = PyKDL.Frame(PyKDL.Rotation.EulerZYZ(0.3, 1.4, 3.14), PyKDL.Vector(0.705438961242, -0.1208864692291, 1.181029263241))
	irpos.move_to_cartesian_pose(3.0, Pose(Point(0.705438961242, -0.1208864692291, 1.181029263241), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)))
	irpos.move_to_cartesian_pose(3.0,pm.toMsg(rot))
	irpos.move_to_cartesian_pose(3.0,pm.toMsg(rot2))

	toolParams = Pose(Point(0.0, 0.0, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0))
	irpos.set_tool_geometry_params(toolParams)

	rot = PyKDL.Frame(PyKDL.Rotation.EulerZYZ(0.0, 1.4, 3.14), PyKDL.Vector(0.705438961242, -0.1208864692291, 1.181029263241))
	irpos.move_to_cartesian_pose(3.0,Pose(Point(0.705438961242, -0.1208864692291, 1.181029263241), Quaternion(0.675351045979, 0.0892025112399, 0.698321120995, 0.219753244928)))
	irpos.move_to_cartesian_pose(3.0,pm.toMsg(rot))
	irpos.move_to_cartesian_pose(3.0,Pose(Point(0.705438961242, -0.1208864692291, 1.181029263241), Quaternion(0.63691, 0.096783, 0.75634, -0.11369)))

	toolParams = Pose(Point(0.0, 0.0, 0.25), Quaternion(0.0, 0.0, 0.0, 1.0))
	irpos.set_tool_geometry_params(toolParams)

	print "Irp6p 'multi_trajectory2' test compleated"

def irp6p_get_status():
	irpos = IRPOS("IRpOS", "Irp6p", 6)

	print('[Joint position]')
	print str(irpos.get_joint_position())
	print('[Motor position]')
	print str(irpos.get_motor_position())
	print('[Cartesian pose]')
	print str(irpos.get_cartesian_pose())
	print('[Wrench]')
	print str(irpos.get_force_readings())

	print "Irp6p 'get_status test compleated"

def irp6p_synchro_position():
	irpos = IRPOS("IRpOS", "Irp6p", 6)

	irpos.move_to_synchro_position(10.0)

	print "Irp6p 'synchro_position' test compleated"

# TRACK DEMOS

def irp6otm_multi_trajectory():
		
	print "Irp6otm 'multi_trajectory' test compleated"

def irp6otm_multi_trajectory2():
	irpos = IRPOS("IRpOS", "Irp6ot", 7)

	irpos.move_to_motor_position([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 10.0)
	irpos.move_to_motor_position([50.0, 10.0, 10.0, 0.0, 10.57, 10.57, -20.0], 2.0)

	irpos.move_to_joint_position([0.0, 0.4, -1.5418065817051163, 0.0, 1.5, 1.57, -2.0], 3.0)
	irpos.move_to_joint_position([0.1, 0.0, -1.5418065817051163, 0.0, 1.5, 1.57, -1.57], 3.0)

	print "Irp6otm 'multi_trajectory2' test compleated"

def irp6otm_get_status():
	irpos = IRPOS("IRpOS", "Irp6ot", 7)

	print('[Joint position]')
	print str(irpos.get_joint_position())
	print('[Motor position]')
	print str(irpos.get_motor_position())
	print('[Cartesian pose]')
	print str(irpos.get_cartesian_pose())
	print('[Wrench]')
	print str(irpos.get_force_readings())

	print "Irp6otm 'get_status' test compleated"

def irp6otm_synchro_position():
	irpos = IRPOS("IRpOS", "Irp6ot", 7)

	irpos.move_to_synchro_position(10.0)

	print "Irp6otm 'synchro_position' test compleated"
	
def test():
	print 'START TEST'

	irpos = IRPOS("IRpOS", "Irp6p", 6)

	irpos.move_to_synchro_position(10.0)
	
	rot = PyKDL.Frame(PyKDL.Rotation.EulerZYZ(0.0, 0.1, 0.1), PyKDL.Vector(0.0, 0.0, 0.0))
	irpos.move_rel_to_cartesian_pose(3.0,pm.toMsg(rot))
	

	print 'END TEST'

#MAIN

if __name__ == '__main__':
	if sys.argv[1]=="p_m":
		irp6p_multi_trajectory()	
	elif sys.argv[1]=="p_m2":
		irp6p_multi_trajectory2()	
	elif sys.argv[1]=="p_s":
		irp6p_get_status()
	elif sys.argv[1]=="p_sp":
		irp6p_synchro_position()
	elif sys.argv[1]=="ot_m":
		irp6otm_multi_trajectory()	
	elif sys.argv[1]=="ot_m2":
		irp6otm_multi_trajectory2()	
	elif sys.argv[1]=="ot_s":
		irp6otm_get_status()	
	elif sys.argv[1]=="ot_sp":
		irp6otm_synchro_position()
	elif sys.argv[1]=="test":
		test()
	elif sys.argv[1]=="T1":
		T1()
	elif sys.argv[1]=="T2":
		T2()
	elif sys.argv[1]=="T3":
		T3()
	elif sys.argv[1]=="T4":
		T4()
	elif sys.argv[1]=="T5":
		T5()
	elif sys.argv[1]=="T6":
		T6()
	elif sys.argv[1]=="TS":
		TSynch()
	elif sys.argv[1]=="TC":
		TC()
