# from multiply import python_multiplication, c_multiplication

import numpy as np
import time

import ctypes
import time
from _ctypes import Structure, POINTER, byref
from ctypes import c_int, c_float
import pyximport; pyximport.install()
import multiplication

import numpy as np

def c_multiplication(a, b):
    class Collection(Structure):
        _fields_ = [("size", c_int),
                    ("data", (c_float * a.shape[1]) * a.shape[0])]

    libmatmult = ctypes.CDLL("./multiply.so")

    libmatmult.multiply.argtypes = [POINTER(Collection)]
    libmatmult.multiply.restype = None

    t_a = Collection()
    t_b = Collection()
    t_c = Collection()

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

a = np.random.rand(2000,2000)
b = np.random.rand(2000,2000)
c = np.random.rand(2000,2000)

print("Timing python multiplication:\n")
start = time.time()
python_result = python_multiplication(a, b)
end = time.time()
print(end - start)

print("Timing ctypes C multiplication:\n")
c_result = c_multiplication(a, b)

print("Timing cython multiplication:\n")
start = time.time()
python_result = multiplication.cython_multiplication(a, b, c, 2000, 2000)
end = time.time()
print(end - start)

print("Timing numpy multiplication:\n")
start = time.time()
python_result = a * b
end = time.time()
print(end - start)

np.multiply()




