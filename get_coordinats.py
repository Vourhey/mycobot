from pymycobot.mycobot import MyCobot
from config import (
    SERIAL_PORT,
    BAUD_RATE
)

mc = MyCobot(SERIAL_PORT, BAUD_RATE)

# Get the current coordinates and pose of the head
coords = mc.get_coords()
print(coords)

angles = mc.get_angles()
print(angles)

