import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd
from pytz import timezone
import numpy as np
import matplotlib.pyplot as plt


def decode_lat_lon(sr: pd.Series) -> pd.Series:
    """
    緯度経度を度数に変換
    """
    tmp = sr.astype(float)
    return (tmp / 100).astype(int) + (tmp % 100) / 60


# 地球の長半径 (km)
R = 6378.137
# 地球の極半径
# R = 6356.752

LOG_LIST = [
    "log/nagano-matsumoto-100318.log",
    "log/matsumoto-nagano-100318.log"
]


def calc_dist_ellipse_height(df_3d):
    use_columns = list(df_3d.columns)

    df_3d_mem = df_3d[use_columns][1:].copy()  # 先頭削除
    df_3d_prev = df_3d[use_columns][:-1].copy()  # 末尾削除

    for uc in use_columns:
        df_3d_mem[uc + "_prev"] = list(df_3d_prev[uc])

    df_3d_mem["dist_3d"] = np.sqrt(
        (df_3d_mem["x"] - df_3d_mem["x_prev"]) ** 2 +
        (df_3d_mem["y"] - df_3d_mem["y_prev"]) ** 2 +
        (df_3d_mem["z"] - df_3d_mem["z_prev"]) ** 2
    )
    # print(df_3d_mem)
    return df_3d_mem["dist_3d"].sum()


def main():
    example_lat, example_lon = 0.636, 2.408
    # 本初子午線あたりに移動
    rot_matrix1 = np.matrix([
        [np.cos(example_lon), np.sin(example_lon), 0],
        [-np.sin(example_lon), np.cos(example_lon), 0],
        [0, 0, 1]
    ])

    # 北極あたりに移動
    rot_matrix2 = np.matrix([
        [np.sin(example_lat), 0, -np.cos(example_lat)],
        [0, 1, 0],
        [np.cos(example_lat), 0, np.sin(example_lat)]
    ])

    rot_matrix3 = np.matrix([
        [0, 1, 0],
        [-1, 0, 0],
        [0, 0, 1]
    ])

    rot_matrix = rot_matrix3 * rot_matrix2 * rot_matrix1
    print("回転行列")
    print(rot_matrix)

    # Figureを追加
    fig = plt.figure(figsize=(8, 8))

    # 3DAxesを追加
    ax = fig.add_subplot(111, projection='3d')

    # Axesのタイトルを設定
    ax.set_title("plot 3D", size=20)

    # 軸ラベルを設定
    ax.set_xlabel("x", size=14)
    ax.set_ylabel("y", size=14)
    ax.set_zlabel("z", size=14)

    # 軸目盛を設定
    # ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
    # ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])

    for LOG in LOG_LIST:
        gps_table = []
        gpgga_list = [None] * 13
        gprmc_list = [None] * 9

        with open(LOG) as f:
            for line in f:
                str_list = line.split(",")
                if str_list[0] == "$GPGGA":
                    gpgga_list = str_list[1:-1]
                elif str_list[0] == "$GPRMC":
                    gprmc_list = str_list[1:-3]
                    if gpgga_list[0] != gprmc_list[0]:
                        print(gpgga_list, gprmc_list)
                        gpgga_list = [None] * 13
                    elif gpgga_list[1:5] != gprmc_list[2:6]:
                        print(gpgga_list, gprmc_list)
                        gpgga_list = [None] * 13
                    gps_table.append(gprmc_list + gpgga_list[5:])
        gps_df = pd.DataFrame(gps_table, columns=[
            "time", "status", "lat", "NS", "lon", "EW",
            "knots", "direction", "date", "quality", "sat",
            "harr", "elevation", "em", "geoid", "gm", "drp_id"
        ])
        gps_df["lat_deg"] = decode_lat_lon(gps_df["lat"])
        gps_df["lon_deg"] = decode_lat_lon(gps_df["lon"])
        gps_df["lat"] = gps_df["lat"] * ((gps_df.pop("NS") == "N") * 2 - 1)
        gps_df["lon"] = gps_df["lon"] * ((gps_df.pop("EW") == "E") * 2 - 1)

        gps_df["lat"] = np.deg2rad(gps_df["lat_deg"])
        gps_df["lon"] = np.deg2rad(gps_df["lon_deg"])

        gps_df["quality"] = gps_df["quality"].astype(pd.Int64Dtype())
        gps_df["sat"] = gps_df["sat"].astype(pd.Int64Dtype())
        gps_df["drp_id"] = gps_df["drp_id"].astype(pd.Int64Dtype())
        gps_df["knots"] = gps_df["knots"].astype(float)
        gps_df["direction"] = gps_df["direction"].astype(float)
        gps_df["harr"] = gps_df["harr"].astype(float)
        gps_df["elevation"] = gps_df["elevation"].astype(float)
        gps_df["geoid"] = gps_df["geoid"].astype(float)
        gps_df["date"] = (gps_df["date"] + gps_df["time"]).apply(lambda x: timezone("UTC").localize(
            datetime.datetime.strptime(x, "%d%m%y%H%M%S")).astimezone(timezone("Asia/Tokyo")))

        gps_df = gps_df.drop(["em", "gm", "time"], axis=1)

        # print(gps_df)

        # 簡単化のため欠損値除去
        df2 = gps_df.dropna()

        # 各点の半径 (楕円体高)
        local_R = (df2["elevation"] + df2["geoid"]) / 1000 + R
        # 各点の半径 (標高のみ)
        # local_R = df2["elevation"] / 1000 + R

        x = np.cos(df2["lat"]) * np.cos(df2["lon"]) * local_R
        y = np.cos(df2["lat"]) * np.sin(df2["lon"]) * local_R
        z = np.sin(df2["lat"]) * local_R

        df_3d = pd.DataFrame({"x": x, "y": y, "z": z})

        use_columns = list(df_3d.columns)

        df_3d_mem = df_3d[use_columns][1:].copy()  # 先頭削除
        df_3d_prev = df_3d[use_columns][:-1].copy()  # 末尾削除

        for uc in use_columns:
            df_3d_mem[uc + "_prev"] = list(df_3d_prev[uc])

        df_3d_mem["dist_3d"] = np.sqrt(
            (df_3d_mem["x"] - df_3d_mem["x_prev"]) ** 2 +
            (df_3d_mem["y"] - df_3d_mem["y_prev"]) ** 2 +
            (df_3d_mem["z"] - df_3d_mem["z_prev"]) ** 2
        )

        # print(df_3d_mem)
        print(f'総移動距離: {df_3d_mem["dist_3d"].sum():.5f}')

        xyz_matrix = np.matrix(df_3d).T
        xyz_matrix_rotated = rot_matrix * xyz_matrix
        df_3d_rotated = pd.DataFrame(
            xyz_matrix_rotated.T, columns=["x", "y", "z"])

        # 高さを最小値基準とする
        df_3d_rotated_mapped = df_3d_rotated.copy()
        df_3d_rotated_mapped["z"] -= 6378.442
        df_3d_rotated_mapped

        # print(df_3d_rotated_mapped)
        print(
            f"回転行列をかけた後の総移動距離: {calc_dist_ellipse_height(df_3d_rotated_mapped):.5f}")

        # 曲線を描画
        ax.plot(*df_3d_rotated_mapped.values.T.tolist(), label=LOG)

    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
