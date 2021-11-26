from ctypes import CDLL, c_int32, c_uint64, c_uint32

clib = CDLL("./rubik.so")

nibai = clib.nibai
nibai.restype = c_int32
nibai.argtypes = (c_int32,)

print(nibai(63278))
