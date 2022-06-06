from gps_func import GPS_data

gd = GPS_data(
    "C:\\Users\\Atsushi\\Documents\\大学ー４年\\課題\\B4_program\\gps\\log\\matsumoto-nagano-100318.log"
)

gd.print_date_time()
gd.graph_latitude_longitude()
gd.graph_elevation_time()
gd.graph_speed_time()
gd.print_moving_distance()

gd.set(
    "C:\\Users\\Atsushi\\Documents\\大学ー４年\\課題\\B4_program\\gps\\log\\nagano-matsumoto-100318.log"
)
gd.print_date_time()
gd.graph_latitude_longitude()
gd.graph_elevation_time()
gd.graph_speed_time()
gd.print_moving_distance()