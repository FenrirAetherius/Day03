import numpy as np


class ColorFilter:

    @staticmethod
    def invert(array):
        return 1 - array

    @staticmethod
    def to_blue(array):
        return array * (0, 0, 1)

    @staticmethod
    def to_green(array):
        return array * (0, 1, 0)

    @staticmethod
    def to_red(array):
        return array * (1, 0, 0)

    @staticmethod
    def celluloid(array, scales=4):
        sub_arr = np.linspace(0, 1, scales, False)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                r, g, b = array[i, j]
                re = gr = bl = 0
                for n in sub_arr:
                    if r < n and re == 0:
                        r = n
                        re = 1
                    if g < n and gr == 0:
                        g = n
                        gr = 1
                    if b < n and bl == 0:
                        b = n
                        bl = 1
                    if re == 1 and gr == 1 and bl == 1:
                        break
                array[i, j] = (r, g, b)
        return array


# import matplotlib.pyplot as plt
# from matplotlib import image as mpimg
# import time


# img = mpimg.imread("elon.png")
# start_time = time.time()
# img = ColorFilter.celluloid(img)
# print(time.time() - start_time)
# imgplot = plt.imshow(img)
# plt.show()
