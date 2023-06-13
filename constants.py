"""Constants list"""

SERIAL_PORT = "/dev/ttyTHS1"
BAUD_RATE = 1000000
SUBSCRIBER_ADDRESS = "4F3b1hoyFW1N4V9H7ggUq23MjXyK8C62s5v6469k9qEBktDf"
# The coordinate is [x, y, z, rx, ry, rz]. [x,y,z] represents the position of the robot arm head in space (the
# coordinate system is cartesian coordinate system). [rx,ry,rz] represents the posture of such head at this point (
# the coordinate system is euler coordinates) - The coordinate value of [x, y, z, rx, ry, rz] has a length of 6,
# x, y, z ranging from - 280 to 280, and rx, ry, yz ranging from - 314 to 314
GOOD_POSITION = [57.0, -107.4, 316.3, -93.81, -12.71, -163.49]
BAD_POSITION = [57.0, -107.4, 316.3, -93.81, -12.71, -163.49]
MOVE_SPEED = 10 # IN mm/s means the movement speed of the robot arm, ranging from 0 to 100.
