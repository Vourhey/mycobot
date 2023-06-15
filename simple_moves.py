from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
import time

from config import (
    SERIAL_PORT,
    BAUD_RATE
)

mc = MyCobot(SERIAL_PORT, BAUD_RATE)

# Get the current coordinates and pose of the head
coords = mc.get_coords()
print(coords)

# Intelligently plan the route, let the head reach the coordinates of [57.0, -107.4, 316.3] in a linear manner,
# and maintain the attitude of [-93.81, -12.71, -163.49], the speed is 80mm/s

mc.send_coords([57.0, -107.4, 316.3, -93.81, -12.71, -163.49], 10, 1)

# Set the wait time to 1.5 seconds
time.sleep(1.5)

# Intelligently plan the route, let the head reach the coordinates of [-13.7, -107.5, 223.9] in a linear way,
# and maintain the attitude of [165.52, -75.41, -73.52], the speed is 80mm/s
mc.send_coords([-13.7, -107.5, 223.9, 165.52, -75.41, -73.52], 10, 1)

# Set the wait time to 1.5 seconds
time.sleep(1.5)

# To change only the x-coordinate of the head, set the x-coordinate of the head to -40. Let it plan the route
# intelligently and move the head to the changed position, with a speed of 70mm/s
mc.send_coord(Coord.X.value, -40, 70)
