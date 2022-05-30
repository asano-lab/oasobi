import matplotlib.pyplot as plt
import geopandas
''' 課題10の3
GPS受信器から出力されるデータから緯度・経度を抽出して、「横軸：経度、縦軸：緯度」のプロットを作ります。
また、背面にShapeファイルで指定した地図を表示します。

利用方法：
LOGSにNMEAフォーマットのGPRMCデータを含むログファイルを指定。
SHAPEにログの位置情報全体を含むShapeファイルを指定。
python3 q03.py

注意点：
ここではGPRMCのデータだけを抽出します。
北緯と南緯をまたいだり、東経と西経をまたいだりする移動のプロットはサポートしていません。
各都道府県・全国のShapeファイルは国土交通省が公開しています。
https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_0.html#prefecture20
デフォルトではログファイルと同じ2010年の長野県全体のデータを指定しています。
事前にpython3 -m pip install matplotlib geopandasを行う必要があります。
geopandasについては依存関係のパッケージが多いので環境を壊さないように、まずはvenvで試してみることをお勧めします。
'''
LOGS = ["matsumoto-nagano-100318.log", "nagano-matsumoto-100318.log"]
SHAPE = "N03-101001_20_GML/N03-10_20_101001.shp"

nagano = geopandas.read_file(SHAPE)
nagano.plot(color="tab:green")
longitudes = {}
latitudes = {}
for logfile in LOGS:
    longitudes[logfile] = []
    latitudes[logfile] = []
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
                longitudes[logfile].append(longitude)
                # 緯度
                north_or_sourth = gprmc[4]
                latitude_dddmm_mmmm = float(gprmc[3])
                latitude_ddd = int(latitude_dddmm_mmmm/100)
                latitude = latitude_ddd + \
                    (latitude_dddmm_mmmm-latitude_ddd*100)/60
                latitudes[logfile].append(latitude)
    plt.plot(longitudes[logfile], latitudes[logfile],
             label=logfile+":GPRMC")
plt.title("2010 Nagano Prefecture")
plt.legend()
if west_or_east == 'W':
    plt.xlabel("West longitude [°]")
elif west_or_east == 'E':
    plt.xlabel("East longitude [°]")
if north_or_sourth == 'N':
    plt.ylabel("North latitude [°]")
elif north_or_sourth == 'S':
    plt.ylabel("South latitude [°]")
plt.show()
