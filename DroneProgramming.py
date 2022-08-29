from dronekit import connect, VehicleMode,LocationGlobalRelative,APIException

import time
import socket
import argparse
import math

def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect

    vehicle = connect(connection_string, wait_ready = True)

    return vehicle

def arm_and_takeoff(targetHeight):

	while not vehicle.is_armable:
		print("Waiting for vehicle to become armable.")
		time.sleep(1)
	print("Vehicle is now armable")

	vehicle.mode = VehicleMode("GUIDED")

	while vehicle.mode!='GUIDED':
		print("Waiting for drone to enter GUIDED flight mode")
		time.sleep(1)
	print("Vehicle now in GUIDED MODE. Have fun!!")

	vehicle.armed = True
	while vehicle.armed==False:
		print("Waiting for vehicle to become armed.")
		time.sleep(1)
	print("Look out! props are spinning!!")

	vehicle.simple_takeoff(targetHeight)

	while True:
		print("Current Altitude: %d"%vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=.95*targetHeight:
			break
		time.sleep(1)
	print("Target altitude reached!!")

	return None

vehicle = connectMyCopter()
print("About to take-off")

vehicle.mode = VehicleMode("GUIDED")
arm_and_takeoff(1)
vehicle.mode = VehicleMode("LAND")

time.sleep(2)

print("End of function")
print("Arducopter version: %s" %vehicle.version)

while True:
    time.sleep(2)

vehicle.close()
