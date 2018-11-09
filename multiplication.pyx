import numpy as np

def cython_multiplication(double[:,:] a, double[:,:] b, double[:,:] out, int x_dims, int y_dims):
    cdef int i, j

    for i in range(x_dims):
        for j in range(y_dims):
            out[i, j] = a[i,j] * b[i,j]

    return np.asarray(out)
