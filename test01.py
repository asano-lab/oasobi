#!/usr/bin/env python3
import datetime
from pytz import timezone
import pings

p = pings.Ping()  # Pingオブジェクト作成
res = p.ping("google.com")  # googleを監視

res.print_messages()
print(res.is_reached())

TZ_TOKYO = timezone("Asia/Tokyo")


def main():
    t0 = datetime.datetime.now(tz=TZ_TOKYO)
    # print(t0)
    # print(t0.tzinfo)
    print(t0.strftime("%a, %d %b %Y %H:%M:%S %z"))


if __name__ == "__main__":
    main()
