from robonomicsinterface import Subscriber, SubEvent, Account
from pymycobot.mycobot import MyCobot
import time
import json

from constants import (
SERIAL_PORT,
BAUD_RATE,
SUBSCRIBER_ADDRESS,
GOOD_POSITION,
BAD_POSITION,
MOVE_SPEED
)


def main():
    # mc = MyCobot(SERIAL_PORT, BAUD_RATE)
    account = Account()

    def callback(data_raw):
        print(data_raw)
        data = json.loads(data_raw[2])
        status = data["status"]
        if status == "success":
            print("move to good position")
            # mc.send_coords(GOOD_POSITION, MOVE_SPEED, 1)
        else:
            print("move to bad position")
            # mc.send_coords(BAD_POSITION, MOVE_SPEED, 1)

    subscriber = Subscriber(account, SubEvent.NewRecord, addr=SUBSCRIBER_ADDRESS, subscription_handler=callback)
    try:
        while True:
            print("in loop")
            time.sleep(10)
    except KeyboardInterrupt:
        print('interrupted!')

    subscriber.cancel()


if __name__ == "__main__":
    main()
