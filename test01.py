#!/usr/bin/env python3
import datetime
import numpy as np
import pandas as pd
from pytz import timezone
import numpy as np

TZ_TOKYO = timezone("Asia/Tokyo")


def main():
    t0 = datetime.datetime.now(tz=TZ_TOKYO)
    print(t0)
    print(t0.tzinfo)


if __name__ == "__main__":
    main()
