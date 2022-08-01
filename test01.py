#!/usr/bin/env python3
import datetime
from pytz import timezone
import urllib.request
from urllib.error import URLError


TZ_TOKYO = timezone("Asia/Tokyo")


def internet_on():
    """
    インターネットに接続しているかどうか
    """
    res = True
    try:
        urllib.request.urlopen("https://www.google.com", timeout=1)
    except URLError:
        res = False
    return res

def main():
    t0 = datetime.datetime.now(tz=TZ_TOKYO)
    # print(t0)
    # print(t0.tzinfo)
    print(t0.strftime("%a, %d %b %Y %H:%M:%S %z"))
    print(internet_on())


if __name__ == "__main__":
    main()
