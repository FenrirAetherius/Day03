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
                for n in sub_arr:
                    if r < n:
                        r = n
                        break
                for n in sub_arr:
                    if g < n:
                        g = n
                        break
                for n in sub_arr:
                    if b < n:
                        b = n
                        break
                array[i, j] = (r, g, b)
        return array

# import matplotlib.pyplot as plt
# from matplotlib import image as mpimg


# img = mpimg.imread("elon.png")
# img = ColorFilter.celluloid(img)
# imgplot = plt.imshow(img)
# plt.show()
