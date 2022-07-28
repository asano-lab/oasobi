import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd
from pytz import timezone
import numpy as np
import matplotlib.pyplot as plt

TZ_TOKYO = timezone("Asia/Tokyo")


def main():
    t0 = datetime.datetime.now(tz=TZ_TOKYO)
    print(t0)

    lambda x: timezone("UTC").localize(
        datetime.datetime.strptime(x, "%d%m%y%H%M%S")).astimezone()


if __name__ == "__main__":
    main()
