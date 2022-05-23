import datetime
''' 課題10の2
GPS受信器から出力されるデータから日付・時間を抽出して表示します。

利用方法：
LOGSにNMEAフォーマットのGPRMCデータを含むログファイルを指定。
python3 q02.py

注意点：
ここではGPRMCのデータだけを抽出します。
入力データはUTCと思われます。JSTにして表示します。
'''
LOGS = ["matsumoto-nagano-100318.log", "nagano-matsumoto-100318.log"]

for logfile in LOGS:
    print(logfile+":GPRMC")
    with open(logfile) as f:
        for line in f:
            if "$GPRMC" in line:
                gprmc = line.split(',')
                datetime_utc = datetime.datetime.strptime(
                    gprmc[9] + gprmc[1], '%d%m%y%H%M%S')
                datetime_jst = datetime_utc + datetime.timedelta(hours=9)
                print(datetime_jst)
