from haversine import haversine
''' 課題10の6
GPS受信器から出力されるデータから移動距離を計算します。

利用方法：
LOGSにNMEAフォーマットのGPRMCデータを含むログファイルを指定。
python3 q06.py

注意点：
事前にpython3 -m pip install haversineを行う必要があります。
'''
LOGS = ["matsumoto-nagano-100318.log", "nagano-matsumoto-100318.log"]

for logfile in LOGS:
    first_loop = True
    sum_distance = 0
    with open(logfile) as f:
        for line in f:
            if "$GPRMC" in line:
                gprmc = line.split(',')
                # 経度
                west_or_east = gprmc[6]
                longitude_dddmm_mmmm = float(gprmc[5])
                longitude_ddd = int(longitude_dddmm_mmmm/100)
                longitude = longitude_ddd + \
                    (longitude_dddmm_mmmm-longitude_ddd*100)/60
                # 緯度
                north_or_sourth = gprmc[4]
                latitude_dddmm_mmmm = float(gprmc[3])
                latitude_ddd = int(latitude_dddmm_mmmm/100)
                latitude = latitude_ddd + \
                    (latitude_dddmm_mmmm-latitude_ddd*100)/60
                if first_loop:
                    first_loop = False
                else:
                    distance = haversine(
                        (old_longitude, old_latitude), (longitude, latitude))
                    sum_distance += distance
                old_longitude = longitude
                old_latitude = latitude
    print(logfile+":GPRMC"'\t'+str(sum_distance)+" [km]")
