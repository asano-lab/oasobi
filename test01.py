
import datetime
import numpy as np
from pytz import timezone


def main():
    a = datetime.datetime.now()
    b = timezone("UTC").localize(datetime.datetime.strptime(
        a, "%d%m%y%H%M%S")).astimezone(timezone("Asia/Tokyo"))
    print(a)
    print(b)


if __name__ == "__main__":
    main()
