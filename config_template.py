"""Constants list"""
#data to connect to mycobot
SERIAL_PORT = "/dev/ttyTHS1"
BAUD_RATE = 1000000

# Robonomics data
SEED = ""
DIGITAL_TWIN_NUMBER =
DIGITAL_TWIN_TOPIC = ""

# The coordinate is [x, y, z, rx, ry, rz]. [x,y,z] represents the position of the robot arm head in space (the
# coordinate system is cartesian coordinate system). [rx,ry,rz] represents the posture of such head at this point (
# the coordinate system is euler coordinates) - The coordinate value of [x, y, z, rx, ry, rz] has a length of 6,
# x, y, z ranging from - 280 to 280, and rx, ry, yz ranging from - 314 to 314
GOOD_POSITION =  # for example - [251.8, -64.2, 213.1, -90.08, 0.7, -90.7]
BAD_POSITION =
MOVE_SPEED = 10 # IN mm/s means the movement speed of the robot arm, ranging from 0 to 100.
