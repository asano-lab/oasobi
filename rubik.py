from ctypes import CDLL, c_int32, c_uint64, Structure

class Status(Structure):
    # コーナーの情報40bitとエッジの情報60bitに分けたい
    _fields_ = [("c_info", c_uint64), ("e_info", c_uint64)]

clib = CDLL("./rubik.so")

nibai = clib.nibai
nibai.restype = c_int32
nibai.argtypes = (c_int32,)

print(nibai(63278))
