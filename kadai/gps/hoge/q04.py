import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
''' 課題10の4
GPS受信器から出力されるデータから高度を抽出して、「横軸：時間、縦軸：高度」のプロットを作ります。

利用方法：
LOGSにNMEAフォーマットのGPGGAデータを含むログファイルを指定。
python3 q04.py

注意点：
ここではGPGGAのデータだけを抽出します。
日付をまたぐ場合のプロットをサポートしていません。
事前にpython3 -m pip install matplotlibを行う必要があります。
'''
LOGS = ["matsumoto-nagano-100318.log", "nagano-matsumoto-100318.log"]

fig = plt.figure()
ax = fig.add_subplot(111)
datetimes_jst = {}
heights_above_sealevel = {}
for logfile in LOGS:
    datetimes_jst[logfile] = []
    heights_above_sealevel[logfile] = []
    with open(logfile) as f:
        for line in f:
            if "$GPGGA" in line:
                gpgga = line.split(',')
                time_utc = gpgga[1]
                datetime_utc = datetime.datetime.strptime(
                    time_utc, '%H%M%S')
                datetime_jst = datetime_utc + datetime.timedelta(hours=9)
                height_above_sealevel = float(gpgga[9])
                datetimes_jst[logfile].append(datetime_jst)
                heights_above_sealevel[logfile].append(height_above_sealevel)
    ax.plot(datetimes_jst[logfile],
            heights_above_sealevel[logfile], label=logfile+":GPGGA")
plt.grid()
plt.legend()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xlabel("Time")
plt.ylabel("Height above sea level [" + gpgga[10].lower()+"]")
plt.show()
