#!/usr/bin/env python3
import datetime
from pytz import timezone
import pings
import urllib.request
from urllib.error import URLError


def internet_on():
    try:
        urllib.request.urlopen("https://www.google.com", timeout=1)
        return True
    except URLError:
        return False


TZ_TOKYO = timezone("Asia/Tokyo")


def main():
    t0 = datetime.datetime.now(tz=TZ_TOKYO)
    # print(t0)
    # print(t0.tzinfo)
    print(t0.strftime("%a, %d %b %Y %H:%M:%S %z"))
    print(internet_on())


if __name__ == "__main__":
    main()
