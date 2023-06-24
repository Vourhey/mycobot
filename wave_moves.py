from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
import time

from config import (
    SERIAL_PORT,
    BAUD_RATE
)

mc = MyCobot(SERIAL_PORT, BAUD_RATE)

# Get the current angles and pose of the head
angles = mc.get_angles()
print(angles)

# Intelligently plan the route, let the head reach the coordinates of [57.0, -107.4, 316.3] in a linear manner,
# and maintain the attitude of [-93.81, -12.71, -163.49], the speed is 80mm/s
for i in range(0, 2):
    mc.send_angles([0, 0, 0, 0, 0, 0], 10, 1)
    time.sleep(1)


    mc.send_angles([-0.08, -74.26, 0.08, -0.87, 0.35, -0.61], 10, 1)
    time.sleep(1.5)

    mc.send_angles([0, 0, 0, 0, 0, 0], 10, 1)
    time.sleep(1)

