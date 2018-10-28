import ctypes
import time
from _ctypes import Structure, POINTER, byref
from ctypes import c_int, c_float

import numpy as np

def c_multiplication(a, b):
    class TestStruct(Structure):
        _fields_ = [("size", c_int),
                    ("data", (c_float * 2000) * 2000)]

    libmatmult = ctypes.CDLL("./multiply.so")

    libmatmult.multiply.argtypes = [POINTER(TestStruct)]
    libmatmult.multiply.restype = None

    t_a = TestStruct()
    t_b = TestStruct()
    t_c = TestStruct()

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            t_a.data[i][j] = a[i][j]
            t_c.data[i][j] = a[i][j]

    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            t_b.data[i][j] = b[i][j]

    start = time.time()
    libmatmult.multiply(byref(t_a), byref(t_b), byref(t_c), a.shape[0], a.shape[1])
    end = time.time()
    print(end - start)

    c_result = np.ones(a.shape)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c_result = (t_c.data[i][j])
    return c_result


def python_multiplication(a,b):
    product = np.ones(a.shape)

    for row_index in np.arange(a.shape[0]):
        for col_index in np.arange(a.shape[1]):
            product[row_index][col_index] = a[row_index][col_index] * b[row_index][col_index]

    return product