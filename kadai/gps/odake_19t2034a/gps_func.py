import csv
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import math
import datetime as dt


class GPS_data:
    gps_data_list = []
    file_name = ""

    def __init__(self, gps_log_file_path):
        self.gps_data_list.clear()
        self.file_name = gps_log_file_path
        with open(gps_log_file_path, "r", encoding="UTF-8") as gps_log_file:
            log_data = csv.reader(gps_log_file)
            for data in log_data:
                self.gps_data_list.append(data)

    def set(self, gps_log_file_path):
        self.gps_data_list.clear()
        self.file_name = gps_log_file_path
        with open(gps_log_file_path, "r", encoding="UTF-8") as gps_log_file:
            log_data = csv.reader(gps_log_file)
            for data in log_data:
                self.gps_data_list.append(data)

    def get(self):
        return self.gps_data_list

    def print_date_time(self):  # 日時
        print("#" * 30)
        for log_data in self.gps_data_list:
            if log_data[0] == "$GPRMC":
                print_data = dt.datetime(2000 + int(log_data[9][4:]),
                                         int(log_data[9][2:4]),
                                         int(log_data[9][:2]),
                                         int(log_data[1][:2]),
                                         int(log_data[1][2:4]),
                                         int(log_data[1][4:6]))
                print(print_data)

    def graph_latitude_longitude(self):  # 緯度経度
        latitude = []  # 緯度
        longitude = []  # 経度
        for log_data in self.gps_data_list:
            if log_data[0] == "$GPRMC":
                latitude.append(
                    int(float(log_data[3]) / 100) +
                    ((float(log_data[3]) / 100) -
                     int(float(log_data[3]) / 100)) * 100 / 60)  # 緯度
                longitude.append(
                    int(float(log_data[5]) / 100) +
                    ((float(log_data[5]) / 100) -
                     int(float(log_data[5]) / 100)) * 100 / 60)  # 経度
        #表示
        fig = plt.figure()
        fig.canvas.set_window_title(str(self.file_name))
        # plt.plot(longitude, latitude)
        plt.scatter(longitude, latitude)
        plt.title('緯度・経度', fontname="MS Gothic")
        plt.xlabel('経度[°]', fontname="MS Gothic")
        plt.ylabel('緯度[°]', fontname="MS Gothic")
        plt.grid()

        plt.show()

    def graph_elevation_time(self):  # 標高_時間
        ####################
        # 適当
        YY_data = 2000
        MM_data = 10
        DD_data = 4
        ####################
        elevation = []  # 標高
        time = []  # 時間
        for log_data in self.gps_data_list:
            if log_data[0] == "$GPGGA":
                elevation.append(float(log_data[9]))  # 標高
                time.append(
                    dt.datetime(YY_data, MM_data, DD_data,
                                int(log_data[1][:2]), int(log_data[1][2:4]),
                                int(log_data[1][4:6])))  # 時間
        #表示
        fig = plt.figure()
        fig.canvas.set_window_title(str(self.file_name))
        plt.plot(time, elevation)
        # plt.scatter(time, elevation)
        plt.title('高度の時間推移', fontname="MS Gothic")
        plt.xlabel('時間', fontname="MS Gothic")
        plt.ylabel('高度[m]', fontname="MS Gothic")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.grid()
        plt.show()

    def graph_speed_time(self):  # 速度_時間
        speed = []  # 速度
        time = []  # 時間
        for log_data in self.gps_data_list:
            if log_data[0] == "$GPRMC":
                speed.append(float(log_data[7]) * 1.852)  # 速度（[knot]->[km/h]）
                time.append(
                    dt.datetime(2000 + int(log_data[9][4:]),
                                int(log_data[9][2:4]), int(log_data[9][:2]),
                                int(log_data[1][:2]), int(log_data[1][2:4]),
                                int(log_data[1][4:6])))  # 時間
        #表示
        fig = plt.figure()
        fig.canvas.set_window_title(str(self.file_name))
        plt.plot(time, speed)
        # plt.scatter(time, speed)
        plt.title('速度の時間推移', fontname="MS Gothic")
        plt.xlabel('時間', fontname="MS Gothic")
        plt.ylabel('速度[km/h]', fontname="MS Gothic")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.grid()
        plt.show()

    def get_l(self, ido_1, keido_1, ido_2, keido_2):
        #ヒュベニの公式

        R_x = 6378137.0  #赤道半径（長半径）
        R_y = 6356752.314245  #極半径（短半径）
        P = (math.radians(ido_2) + math.radians(ido_1)) / 2
        E = math.sqrt((R_x**2 - R_y**2) / R_x**2)  #離心率
        W = math.sqrt(1 - E**2 * math.sin(P)**2)
        N = R_x / W  #卯酉線（ぼうゆうせん）曲率半径
        M = R_x * (1 - E**2) / W**3  #子午線曲率半径
        D_y = math.radians(ido_2) - math.radians(ido_1)
        D_x = math.radians(keido_2) - math.radians(keido_1)

        D = math.sqrt((D_y * M)**2 + (D_x * N * math.cos(P))**2)  #2点間の距離
        return D / 1000  #[km]

    def moving_distance(self):  # 移動距離
        latitude = []  # 緯度
        longitude = []  # 経度
        time = []  # 時間
        elevation = {}  # 標高
        l_sum = 0
        for log_data in self.gps_data_list:
            if log_data[0] == "$GPRMC":
                latitude.append(
                    int(float(log_data[3]) / 100) +
                    ((float(log_data[3]) / 100) -
                     int(float(log_data[3]) / 100)) * 100 / 60)  # 緯度
                longitude.append(
                    int(float(log_data[5]) / 100) +
                    ((float(log_data[5]) / 100) -
                     int(float(log_data[5]) / 100)) * 100 / 60)  # 経度
                time.append(log_data[1])  # 時間
            elif log_data[0] == "$GPGGA":
                elevation[log_data[1]] = float(log_data[9])  # 標高

        for i in range(len(latitude) - 2):
            l = self.get_l(latitude[i], longitude[i], latitude[i + 1],
                           longitude[i + 1])
            if (time[i] in elevation) and (time[i + 1] in elevation):
                l_sum += math.sqrt(l**2 + (
                    abs(elevation.get(time[i + 1]) - elevation.get(time[i])) /
                    1000)**2)
            else:
                l_sum += l
            # l_sum += l
        return l_sum

    def print_moving_distance(self):
        print("#" * 30)
        print(str(self.file_name))
        print("移動距離：" + str(self.moving_distance()) + "[km]")