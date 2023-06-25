from robonomicsinterface import Subscriber, SubEvent, Account, DigitalTwin
from pymycobot.mycobot import MyCobot
import typing as tp
import time
import json

from config import (
    SERIAL_PORT,
    BAUD_RATE,
    SEED,
    DIGITAL_TWIN_NUMBER,
    DIGITAL_TWIN_TOPIC,
    DIGITAL_TWIN_COBOT_TOPIC,
    GOOD_POSITION,
    BAD_POSITION,
    MOVE_SPEED,
)


class Cobot280:
    """
    simple class to control my cobot 280jn
    """

    def __init__(self) -> None:
        self.account = Account(seed=SEED)
        self.mc = MyCobot(SERIAL_PORT, BAUD_RATE)
        self.dt = DigitalTwin(self.account)
        self.sub_address = self.dt.get_source(DIGITAL_TWIN_NUMBER, DIGITAL_TWIN_COBOT_TOPIC)
        self.subscriber = Subscriber(
            self.account,
            SubEvent.NewLaunch,
            addr=self.sub_address,
            subscription_handler=self.callback,
        )
        # At start go to "home position"
        self.go_home_position()

    def go_home_position(self) -> None:
        """
        move robot to home position - all angles to 0
        """
        self.mc.send_angles([0, 0, 0, 0, 0, 0], MOVE_SPEED)

    def callback(self, data_raw: tp.List[tp.Union[str, tp.Dict[str, str]]]) -> None:
        """
        callback function for robonomics subscribers
        :param data_raw: data from datalog
        """
        print(data_raw)
        
        angles = mc.get_angles()
        print(angles)

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

    def run(self) -> None:
        """
        infinite loop
        """
        try:
            while True:
                print("in loop")
                time.sleep(10)
        except KeyboardInterrupt:
            print("interrupted!")

        self.subscriber.cancel()


if __name__ == "__main__":
    my_cobot = Cobot280()
    my_cobot.run()
