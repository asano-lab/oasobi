#!/usr/bin/env python3
import datetime
from pytz import timezone
import numpy as np

TZ_TOKYO = timezone("Asia/Tokyo")


def main():
    t0 = datetime.datetime.now(tz=TZ_TOKYO)
    # print(t0)
    # print(t0.tzinfo)
    print(t0.strftime("%a, %d %b %Y %H:%M:%S %z"))


if __name__ == "__main__":
    main()
