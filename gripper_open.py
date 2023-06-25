from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
import time

from config import (
            SERIAL_PORT,
                BAUD_RATE
                )

mc = MyCobot(SERIAL_PORT, BAUD_RATE)

mc.set_gripper_state(0, 100)

