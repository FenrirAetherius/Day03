import numpy as np


class NumPyCreator:

    def from_iterable(self, values, argtype=None):
        return np.array(values, dtype=argtype)

    def from_list(self, values, argtype=None):
        return np.array(values, dtype=argtype)

    def from_tuple(self, values, argtype=None):
        return np.array(values, dtype=argtype)

    def from_shape(self, shape, argtype=None):
        return np.zeros(shape, dtype=argtype)

    def random(self, shape):
        return np.random.rand(shape)

    def identity(self, size, argtype=None):
        return np.eye(size, dtype=argtype)
