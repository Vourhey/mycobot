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
    mc.send_angles([0, 0, 0, 0, 0, 0], 80)
    time.sleep(0.5)

    mc.send_angles([-0.61, -0.17, -0.17, 0.79, 144.4, -48.86 ], 80)
    time.sleep(0.5)
    
    mc.send_angles([ -0.61, 27.77, -0.08, 1.49, 129.11, -46.31 ], 80)
    time.sleep(0.5)

    mc.send_angles([ -0.26, 27.94, 47.63, 1.4, 110.39, -46.23], 80)
    time.sleep(0.5)

    mc.send_angles([-0.61, -51.06, 21.53, -0.79, 91.23, -46.58], 80)
    time.sleep(0.5)
    
    mc.send_angles([ -0.61, -72.5, -12.12, -1.49, 106.69, -46.58], 80)
    time.sleep(0.5)

mc.send_angles([0, 0, 0, 0, 0, 0], 80)
time.sleep(0.5)

