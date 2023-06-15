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
        self.sub_address = self.dt.get_source(DIGITAL_TWIN_NUMBER, DIGITAL_TWIN_TOPIC)
        self.subscriber = Subscriber(
            self.account,
            SubEvent.NewRecord,
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
        data = json.loads(data_raw[2])
        status = data["status"]
        if status == "success":
            print("move to good position")
            self.mc.send_coords(GOOD_POSITION, MOVE_SPEED, 1)
            time.sleep(10)
            self.go_home_position()
        else:
            print("move to bad position")
            self.mc.send_coords(BAD_POSITION, MOVE_SPEED, 1)
            time.sleep(10)
            self.go_home_position()

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
